import ssl
import urllib.request as UR
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from utils.env import Env
from utils.switch import Switch
from schema.platform_schema import Mutation, Query


# # 这是简单的发GraphQL请求示例，不依赖自动生成的schema
# def login_simple():
#     url = "https://test2.teletraan.io/graphql"
#     headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
#     query = 'mutation login($input: LoginInput!) {login(input: $input) {token}}'
#     variables = '''
#     {
#       "input": {
#         "account": "admin",
#         "password": "teletraan@2022"
#       }
#     }
#         '''
#     endpoint = HTTPEndpoint(url, headers)
#     data = endpoint(query, variables)
#     print(data, type(data))

# 走代理时，全局取消证书验证，避免报错


class Request:
    get_env = Env()
    url = get_env.get_env()
    account = get_env.get_account()
    password = get_env.get_pwd()

    def __init__(self, proxy_=None):
        switch = Switch()
        is_switch_on = switch.is_proxy_on()
        if is_switch_on is True:
            ssl._create_default_https_context = ssl._create_unverified_context
            proxy_ = "127.0.0.1:8080"
        else:
            pass
        if proxy_:
            proxy = {
                "http": 'http://' + proxy_,
                "https": 'http://' + proxy_
            }
        else:
            proxy = None
        proxy_support = UR.ProxyHandler(proxy)
        # build a new opener that adds authentication and caching FTP handlers
        opener = UR.build_opener(proxy_support, UR.CacheFTPHandler)
        # install it
        UR.install_opener(opener)

    # 这是sgqlc提供的更优雅的请求方式
    def login_right(self):
        headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        variables = {
            "account": self.account,
            "password": self.password
          }
        op = Operation(Mutation)
        login = op.login(input=variables)
        # 指定返回token，不要userid
        login.token()
        data = endpoint(op)
        res = (op + data).login
        '''
        res = AuthInfo(token=34CkAS3qWpt5xw0O7QX5teMjKUwUnoTh)
        如果res = op + data
        res = Mutation(⬆️res)
        '''
        return res.token

    def query_project(self):
        token = 'Token ' + self.login_right()
        headers = {'accept': 'application/json', 'Content-Type': 'application/json', 'authorization': token}
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        op = Operation(Query)
        pro = op.product_project_list(limit=10)
        pro.data.attachment()
        data = endpoint(op)
        res = (op + data).product_project_list.data
        print(res)



if __name__ == "__main__":
    r = Request()
    # login_simple()
    r.login_right()
    # r.query_project()
