from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query, Mutation


class MaterialCategoryApi(GetTokenHeader):
    """__QUERY__"""
    def material_category_list(self, args=None, **kwargs):
        """
        :param args: 想要返回的参数，比如 args=["id", "name"]
        :param kwargs: filter, 比如 property=["PRODUCT"]
        :return: class, MaterialCategoryList(data=[MaterialCategory(id=31, name='category_name_CsD2Kq'), ..])
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        mc_list = op.material_category_list(
            limit=10,
            filter=eval(f"{kwargs}")
        )
        if args:
            mc_list.data.__fields__(*args)
            mc_list.total_count()
        else:
            pass
        data = endpoint(op)
        res = (op + data).material_category_list
        return res

    def material_category(self, category_id: int, args=None):
        """
        :param category_id: 输入物料id
        :param args: 输入需要返回的字段，如["name", "code"]
        :return:
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        category_detail = op.material_category(id=category_id)
        if args:
            category_detail.__fields__(*args)
        data = endpoint(op)
        res = (op + data).material_category
        return res

    def is_material_category_exists(self, **kwargs):
        """
        :param kwargs: 传入参数，形如：
            name="string!", property="string!"
            material_property:PRODUCT, RAW_MATERIAL, INTERMEDIATE, BACTERIA
        :return: BOOLEAN
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Query)
        op.is_material_category_exists(input=eval(f"{kwargs}"))
        data = endpoint(op)
        res = (op + data).is_material_category_exists
        return res

    """__MUTATION__"""
    def create_material_category(self, variables):
        """
        :param variables: 传入参数
        :return:
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.create_material_category(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).create_material_category
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def update_material_category(self, variables):
        """
        :param variables: 传入参数
        :return: True or errMessage
        """
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.update_material_category(input=variables)
        data = endpoint(op)
        try:
            res = (op + data).update_material_category
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res

    def delete_category(self, variables):
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers)
        op = Operation(Mutation)
        op.delete_material_category(id=variables)
        data = endpoint(op)
        try:
            res = (op + data).delete_material_category
            return res
        except:
            res = data.get("errors")[0].get("message")
            return res


if __name__ == '__main__':
    m = MaterialCategoryApi()
    print(m.material_category(category_id=10))

