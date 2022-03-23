from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.base_api import BaseApi
from schema.platform_schema import Mutation, Query


class GetTokenHeader(BaseApi):
    def get_token(self, account=BaseApi.account, password=BaseApi.password):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        variables = {
            "account": account,
            "password": password
        }
        op = Operation(Mutation)
        login = op.login(input=variables)
        login.token()
        data = endpoint(op)
        res = (op + data).login
        token = "Token " + res.token
        return token

    def get_headers(self, account=BaseApi.account, password=BaseApi.password):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        headers.setdefault("authorization", self.get_token(account, password))
        return headers

    def get_user(self):
        """
        :return:class User; 如果想要company_id, 可以使用:
            res.company.id, res = return
        """
        headers = GetTokenHeader.get_headers(self)
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.me()
        data = endpoint(op)
        res = (op + data).me
        return res

    def users_info(self, num: int, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        users_info = op.users(
            filter=eval(f"{kwargs}"),
        )
        if args:
            users_info.__fields__(*args)
        data = endpoint(op)
        res = (op + data).users.data[num]
        return res


if __name__ == '__main__':
    a = GetTokenHeader()
    # res1 = a.get_user()
    # print(res1.company.id)
    # res2 = a.get_headers(account="admin", password="teletraan@2022")
    res2 = a.users_info(num=0).id
    print(res2)
