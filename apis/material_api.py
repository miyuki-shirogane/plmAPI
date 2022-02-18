from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query


class MaterialApi(GetTokenHeader):
    """__QUERY__"""
    def material_list(self, args=None, **kwargs):
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


if __name__ == '__main__':
    m = MaterialApi()
    print(m.material_list())
