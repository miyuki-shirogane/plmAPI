from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from apis.get_token_headers import GetTokenHeader
from schema.platform_schema import Query


class ProjectApis(GetTokenHeader):
    def list_project(self, **kwargs) -> list:
        headers = self.get_headers()
        endpoint = HTTPEndpoint(url=self.url, base_headers=headers, timeout=3)
        op = Operation(Query)
        pro = op.product_project_list(
            limit=10,
            filter=eval(f"{kwargs}")
        )
        # 要返回哪些值
        pro.data.__fields__("name", "code")
        data = endpoint(op)
        res = (op + data).product_project_list.data
        return res


if __name__ == '__main__':
    project = ProjectApis()
    consequence = project.list_project(search="rs6", category=["CUSTOMIZATION"])
    print(consequence)
