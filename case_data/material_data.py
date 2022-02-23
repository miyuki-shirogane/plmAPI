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
        variables_temp = self.get_variables(variables_name="create_material")
        pop_keys = ["category", "specification"]
        [variables_temp.pop(k) for k in pop_keys]
        args = [("name", self.name), ("code", self.code), ("versions", self.versions)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    # name-code-version 假定创建的是a-a-f
    def is_material_exits_normal_2(self):
        versions = self.mock.mock_data("versions")
        variables_temp = MaterialData.is_material_exits_normal_1()
        variables = self.modify_variables(target_json=variables_temp, args=[("versions", versions)])
        return variables

    # name-code不唯一 假定是a-b-m
    def is_material_exits_abnormal_1(self):
        code = self.mock.mock_data("code")
        versions = self.mock.mock_data("versions")
        variables_temp = MaterialData.is_material_exits_normal_1()
        variables = self.modify_variables(target_json=variables_temp, args=[("code", code), ("versions", versions)])
        return variables

    # name-code不唯一 假定是b-a-m
    def is_material_exits_abnormal_2(self):
        name = self.mock.mock_data("name")
        versions = self.mock.mock_data("versions")
        variables_temp = MaterialData.is_material_exits_normal_1()
        variables = self.modify_variables(target_json=variables_temp, args=[("name", name), ("versions", versions)])
        return variables

    # 同一产品version唯一 假定是a-a-a
    def is_material_exits_abnormal_3(self):
        variables = MaterialData.is_material_exits_normal_1()
        return variables


if __name__ == '__main__':
    a = MaterialData()
    print(a.is_material_exits_normal_1())
