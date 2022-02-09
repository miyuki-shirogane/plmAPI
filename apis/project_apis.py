from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.get_token_headers import GetTokenHeader
from case_data.project_data import Data
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
    def create_product_project(self, variables):
        """
        :param variables: 输入传参
        :return: project_id, type = str; or error message, type = str
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_product_project(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_product_project
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    # 需整改，届时参照下上面的兄弟
    def add_product_task(self, project_id: int, task_name: str):
        mock = Mock()
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        variables = self.get_variables(variables_name="add_product_task")
        variables["project"]["id"] = project_id
        variables["task"][0]["name"] = task_name
        variables["task"][0]["planEndAt"] = variables["task"][0]["planStartAt"] = mock.current_time()
        op = Operation(Mutation)
        op.add_product_task(input=variables)
        data = endpoint(op)
        res = (op + data).add_product_task
        return res


if __name__ == '__main__':
    project = ProjectApis()
    data = Data()
    variables = data.create_product_project_normal()
    project.create_product_project(variables=variables)
    consequence = project.create_product_project(variables=variables)
    # consequence = project.add_product_task(project_id=209, task_name="task_name_a_QbcF1h")
    print(len(consequence))
