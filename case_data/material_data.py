import pytest

from apis.base_api import BaseApi
from apis.material_category_apis import MaterialCategoryApi
from case_data.material_category_data import MaterialCategoryData
from utils.mock import Mock


class MaterialData(BaseApi):
    mock = Mock()
    name = mock.mock_data("name")
    code = mock.mock_data("code")
    versions = mock.mock_data("versions")

    def create_material_normal(self):
        material_category_data = MaterialCategoryData()
        material_category = MaterialCategoryApi()
        specification = self.mock.mock_data("specification")
        name = self.mock.mock_data("name")
        code = self.mock.mock_data("code")
        versions = self.mock.mock_data("versions")
        variables = material_category_data.create_material_category_normal(material_property="PRODUCT")
        material_category_id = material_category.create_material_category(variables=variables)
        v_material_category_id = {"id": material_category_id}
        args = [("category", v_material_category_id), ("specification", specification), ("name", name),
                ("code", code), ("versions", versions)]
        variables_temp = self.get_variables(variables_name="create_material")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    # name-code-version 假定创建的是a-a-a
    def is_material_exits_normal_1(self):
        return [self.name, self.code, self.versions]

    # name-code-version 假定创建的是a-a-f; 这个的前置是把上面那个创建了
    def is_material_exits_normal_2(self):
        versions = self.mock.mock_data("versions")
        return [self.name, self.code, versions]

    # name-code不唯一 假定是a-b-m
    def is_material_exits_abnormal_1(self):
        code = self.mock.mock_data("code")
        return [self.name, code, self.versions]

    # name-code不唯一 假定是b-a-m
    def is_material_exits_abnormal_2(self):
        name = self.mock.mock_data("name")
        return [name, self.code, self.versions]

    # 同一产品version唯一 假定是a-a-a
    def is_material_exits_abnormal_3(self):
        res = MaterialData.is_material_exits_normal_1(self)
        return res


if __name__ == '__main__':
    a = MaterialData()
    print(a.is_material_exits_normal_1())
