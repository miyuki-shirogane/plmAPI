from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query, Mutation


class MaterialApi(GetTokenHeader):

    """__QUERY__"""

    def material_list(self, args=None, **kwargs):
        """
        :param args: data下想要返回什么字段。for instance, ["name", "code"]
        :param kwargs: 传入filter， for instance: search="?", property=["PRODUCT"] (RAW_MATERIAL, INTERMEDIATE, BACTERIA)
        :return:try, then u'll know
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        m_list = op.material_list(
            limit=10,
            filter=eval(f"{kwargs}"),
        )
        if args:
            m_list.data.__fields__(*args)
            m_list.total_count()
        else:
            pass
        data = endpoint(op)
        res = (op + data).material_list
        return res

    def material(self, material_id: int, args=None):
        """
        :param material_id: 输入物料id
        :param args: 输入需要返回的字段，如["name", "code"]
        :return:
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        material_detail = op.material(id=material_id)
        if args:
            material_detail.__fields__(*args)
        data = endpoint(op)
        res = (op + data).material
        return res

    def is_material_exists(self, **kwargs):
        """
        :param kwargs: 传入参数，形如：
            company={"id": "1"}, name="string!", versions="string!"
        :return: BOOLEAN
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.is_material_exists(input=eval(f"{kwargs}"))
        data = endpoint(op)
        res = (op + data).is_material_exists
        return res

    """__MUTATION__"""

    def create_material(self, variables):
        """
        :param variables: 传入参数
        :return: 物料id，或错误信息
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_material(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_material
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_material(self, variables):
        """
        :param variables: 传入参数
        :return: True或者ErrorMessage
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_material(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_material
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_material(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_material(id=variables)
        data = endpoint(op)
        try:
            res = (op + data).delete_material
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    from case_data.material_data import MaterialData
    m = MaterialApi()
    d = MaterialData()
    v = d.delete_material_normal()
    print(m.material_list(args=["name"]))
