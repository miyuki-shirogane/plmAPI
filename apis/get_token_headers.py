from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base_api import BaseApi
from schema.platform_schema import Mutation


class GetTokenHeader(BaseApi):
    token = None

    def get_token(self, account=BaseApi.account, password=BaseApi.password, tenant_code=BaseApi.tenant_code):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        variables = {
            "account": account,
            "password": password,
            "tenantCode": tenant_code
        }
        op = Operation(Mutation)
        login = op.login(input=variables)
        login.token()
        data = endpoint(op)
        res = (op + data).login
        token = "Token " + res.token
        return token

    def get_headers(self, account=BaseApi.account, password=BaseApi.password, tenant_code=BaseApi.tenant_code):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

        if not self.token:
            token = self.get_token(account, password, tenant_code)
            self.token = token
        headers.setdefault("authorization", self.token)
        return headers


if __name__ == '__main__':
    g = GetTokenHeader()
    print(g.get_headers())
