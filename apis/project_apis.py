from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query, Mutation


class ProjectApis(GetTokenHeader):
    """__QUERY__"""
    def product_project_list(self, args=None, order_by=["-created_at"], **kwargs):
        """
                limit 10, if not satisfied, update the method.

        :param order_by: ["-create_at"] or ["create_at"]
        :param args: data下要返回哪些值, for instance: ["name", "code"] (NOTICE: data下的一级字段，如果要更深层的子字段，将不支持。)
        :type args: list
        :param kwargs: filter, for instance:
            search="rs6", category=["CUSTOMIZATION"]/(OPTIMIZATION, RESEARCH), projectGroup=[{"id": "11"}]
        :return: class, for instance:
            ProductProjectList(data=[ProductProject(name='project_name_Urs6Se', code='project_code_QBHymL')], total_count=1)
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        project_list = op.product_project_list(
            limit=10,
            filter=eval(f"{kwargs}"),
            order_by=order_by
        )
        if args:
            project_list.data.__fields__(*args)
            project_list.total_count()
        else:
            pass
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
            project_detail.data.__fields__(*args)
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

    def product_task_list(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        task_list = op.product_task_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            task_list.data.__fields__(*args)
        else:
            pass
        data = endpoint(op)
        res = (op + data).product_task_list
        return res

    def bom_list(self, args=None, **kwargs):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        bom_list = op.bom_list(
            filter=eval(f"{kwargs}"),
        )
        if args:
            bom_list.data.__fields__(*args)
        else:
            pass
        data = endpoint(op)
        res = (op + data).bom_list
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

    def set_project_product(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.set_project_product(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).set_project_product
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def start_product_project(self, project_id):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.start_product_project(id=[project_id])
        data = endpoint(op)
        try:
            res = (op + data).start_product_project
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def end_product_project(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.end_product_project(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).end_product_project
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def add_product_task(self, variables):
        """
        :param variables: 传入参数
        :return: True 或者报错
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.add_product_task(input=variables)
        data = endpoint(op)
        res = (op + data).add_product_task
        return res

    def update_product_task(self, variables):
        """
        :param variables:
        :return: True or error message
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_product_task(input=variables)
        data = endpoint(op)
        res = (op + data).update_product_task
        return res

    def create_task_bom(self, variables):
        """
        :param variables:
        :return: bom id
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_task_bom(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_task_bom
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_bom(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_bom(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_bom
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    project = ProjectApis()
    v = {"id": 84, "versions": "???"}
    con = project.update_bom(variables=v)
    # con = project.bom_list(args=["id"], task=[{"id": 87}]).data[0].id
    print(con)
