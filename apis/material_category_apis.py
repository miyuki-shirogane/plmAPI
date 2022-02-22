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
            filter=eval(f"{kwargs}"),
        )
        if args:
            mc_list.data.__fields__(*args)
            mc_list.total_count()
        else:
            pass
        data = endpoint(op)
        res = (op + data).material_category_list
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


if __name__ == '__main__':
    m = MaterialCategoryApi()
    # re = m.material_category_list(args=["id", "name"], property=["PRODUCT"])
    # print(re)
    v = m.get_variables(variables_name="create_material_category")
    re = m.create_material_category(variables=v)
    print(re)
