from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query, Mutation


class FlowApis(GetTokenHeader):
    """__QUERY__"""
    def product_flows(self, args=None, **kwargs):
        """
        返回的是全量的数据
        :param args: 想要返回的值，比如：args=["id", "name"]
        :param kwargs: 传入filter，已经定死为以下2种：search="xxx", company=[{"id": "11"}]
        :return:list, 形如:
        [ProductFlow(id=96, name='flow_name', task_template=[ProductTaskTemplate(id=1, name='task_name'),...]), ...]
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        product_flows = op.product_flows(
            filter=eval(f"{kwargs}"),
        )
        if args:
            product_flows.__fields__(*args)
        data = endpoint(op)
        res = (op + data).product_flows
        return res

    def product_flow(self, flow_id: int, args=None):
        """
        :param flow_id: 输入流程id
        :param args: 需要返回的字段，["id", "name", "task_template"] 中选
        :return:class, ProductFlow(id=96, name=flow_name, task_template=[...], ...)
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        flow_detail = op.product_flow(id=flow_id)
        if args:
            flow_detail.__fields__(*args)
        data = endpoint(op)
        res = (op + data).product_flow
        return res

    def is_product_flow_exists(self, **kwargs):
        """
        :param kwargs: 传入参数, name: string!, company: id
        :return: BOOLEAN
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.is_product_flow_exists(input=eval(f"{kwargs}"))
        data = endpoint(op)
        res = (op + data).is_product_flow_exists
        return res

    """__MUTATION__"""
    def create_product_flow(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_product_flow(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_product_flow
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_product_flow(self, variables):
        """
        :param variables: 传入参数
        :return: True or errMessage
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_product_flow(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_product_flow
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_product_flow(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_product_flow(id=variables)
        data = endpoint(op)
        try:
            res = (op + data).delete_product_flow
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    f = FlowApis()
    res_data = f.delete_product_flow(variables=[103])
    print(res_data)
