from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query, Mutation
from utils.mock import Mock


class ProjectApis(GetTokenHeader):
    """__QUERY__"""
    def product_project_list(self, args=None, **kwargs):
        """
        limit 10, if not satisfied, update the method.

        :param args: data下要返回哪些值, for instance: ["name", "code"] (NOTICE: data下的一级字段，如果要更深层的子字段，将不支持。)
        :type args: list
        :param kwargs: filter, for instance:
            search="rs6", category=["CUSTOMIZATION"]
        :return: class, for instance:
            ProductProjectList(data=[ProductProject(name='project_name_Urs6Se', code='project_code_QBHymL')], total_count=1)
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        project_list = op.product_project_list(
            limit=10,
            filter=eval(f"{kwargs}")
        )
        if args:
            project_list.data.__fields__(*args)
        project_list.total_count()
        data = endpoint(op)
        res = (op + data).product_project_list
        return res

    def product_project(self, project_id: int, args=None):
        """
        :param project_id: 输入项目id
        :param args: 需要返回的字段名称
        :return: class, for instance:
            ProductProject(attachment=[File(id='197', length=339065, name='create_project.jpeg', url='https:..')], ...)
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        project_detail = op.product_project(id=project_id)
        if args:
            project_detail.__fields__(*args)
        data = endpoint(op)
        res = (op + data).product_project
        return res

    def is_product_project_exists(self, **kwargs):
        """
        :param kwargs: 传入参数，形如：
            code="code", company={"id": "1"}, name="name"
        :return: BOOLEAN
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.is_product_project_exists(input=eval(f"{kwargs}"))
        data = endpoint(op)
        res = (op + data).is_product_project_exists
        return res

    """__MUTATION__"""
    def create_product_project(self, args):
        """
        :param args: 列表形式的参数, 记录variables目标参数和修改后的效果。for instance:
            args=[("name", "jojo"), ("code", "jojo")]; CAUTION: 只支持一级字段;
        :return: project_id, type = str
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        variables_temp = self.get_variables(variables_name="create_product_project_temp")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        op = Operation(Mutation)
        op.create_product_project(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_product_project
            return res
        except:
            return None


if __name__ == '__main__':
    project = ProjectApis()
    consequence = project.create_product_project(args=[("name", "Jolyn"), ("code", "看不懂")])
    print(consequence)
