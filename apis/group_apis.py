from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query, Mutation


class GroupApis(GetTokenHeader):
    """__QUERY__"""
    def project_group_list(self, args=None, **kwargs):
        """
        :param args: what you need; args=["data", "total_count"]
        :param kwargs: 传入filter：search="xxx"
        :return:
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        project_group_list = op.project_group_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            project_group_list.__fields__(*args)
        data = endpoint(op)
        res = (op + data).project_group_list
        return res

    def project_group(self, group_id: int, args=None):
        """
        :param group_id:
        :param args: ["id", "name"]
        :return: ProjectGroup(id=10, name=group_auKphi)
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        group_detail = op.project_group(id=group_id)
        if args:
            group_detail.__fields__(*args)
        data = endpoint(op)
        res = (op + data).project_group
        return res

    def is_project_group_name_exists(self, **kwargs):
        """
        :param kwargs: name="string!"
        :return: BOOLEAN
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.is_project_group_name_exists(input=eval(f"{kwargs}"))
        data = endpoint(op)
        res = (op + data).is_project_group_name_exists
        return res

    def project_group_member_list(self, group_id: int, args=None):
        """
        :param group_id:
        :param args: 需要返回的字段, ["id", "member", "project_group"]
        :return:
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        group_member_detail = op.project_group_member_list(id=[group_id])
        if args:
            group_member_detail.__fields__(*args)
        data = endpoint(op)
        res = (op + data).project_group_member_list
        return res

    """__MUTATION__"""
    def create_project_group(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_project_group(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_project_group
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_project_group(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_project_group(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_project_group
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_project_group(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_project_group(id=variables)
        data = endpoint(op)
        try:
            res = (op + data).delete_project_group
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def add_project_group_member(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.add_project_group_member(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).add_project_group_member
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def remove_project_group_member(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.remove_project_group_member(id=variables)
        data = endpoint(op)
        try:
            res = (op + data).remove_project_group_member
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    g = GroupApis()
    print(g.project_group_member_list(group_id=24, args=["member"]))
    # print(g.project_group_member_list(group_id=10, args=["member"]).member.account)
