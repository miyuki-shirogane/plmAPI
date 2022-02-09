import pytest
from apis.project_apis import ProjectApis
from case_data.project_data import Data


class TestProject:
    data = Data()
    c_v1 = data.create_product_project_normal()
    c_v2 = data.create_product_project_duplicate()
    c_v3 = data.create_product_project_no_project_group()

    def setup(self):
        self.project = ProjectApis()

    @pytest.mark.parametrize("variables", [c_v1, c_v2, c_v3], ids=["正常", "重复名称编码", "执行小组为空"])
    def test_create_product_project(self, variables):
        res = self.project.create_product_project(variables=variables)
        print(res)
