from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base_api import BaseApi
from schema.platform_schema import Mutation


class GetTokenHeader(BaseApi):
    def get_token(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        variables = {
            "account": self.account,
            "password": self.password
        }
        op = Operation(Mutation)
        login = op.login(input=variables)
        login.token()
        data = endpoint(op)
        res = (op + data).login
        token = "Token " + res.token
        return token

    def get_headers(self):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        headers.setdefault("authorization", self.get_token())
        return headers


if __name__ == '__main__':
    a = GetTokenHeader()
    res1 = a.get_headers()
    print(res1)
