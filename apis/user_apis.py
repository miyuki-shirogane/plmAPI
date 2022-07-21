import jmespath
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Mutation, Query


class User(GetTokenHeader):
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

    def users_info(self, args=None, **kwargs):
        """
        常用用法： users_info(search="Jayce").data[0].id
        :param args:
        :param kwargs:
        :return:
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        user_list = op.user_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            user_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).user_list
        return res

    def roles_info(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        users_info = op.role_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            users_info.__fields__(*args)
        data = endpoint(op)
        res = (op + data).role_list
        return res

    def create_user(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_user(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_user
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def create_role(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_role(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_role
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def organization_tree_nodes(self):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.organization_tree_nodes()
        data = endpoint(op)
        res = (op + data).organization_tree_nodes
        return res

    def create_organization(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_organization(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_organization
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def department_tree(self):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.department_tree(filter={})
        data = endpoint(op)
        res = (op + data).department_tree
        return res

    def department_list(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        department_info = op.department_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            department_info.__fields__(*args)
        data = endpoint(op)
        res = (op + data).department_list
        return res

    def organization_list(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        organization_info = op.organization_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            organization_info.__fields__(*args)
        data = endpoint(op)
        res = (op + data).organization_list
        return res


if __name__ == '__main__':
    a = User()
    # name = a.organization_list(id="0bb2ace2-5633-3913-bc67-cedae567a943").data[0].name
    # con = a.department_list(args=["id", "name"], ids=[{"id": 62640}])
    con = a.get_user()
    print(con)
    # con = a.create_user()
    # print(con)
    # print(json.loads(con)["id"])
