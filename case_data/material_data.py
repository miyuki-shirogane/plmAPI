from apis.base_api import BaseApi
from apis.material_category_apis import MaterialCategoryApi
from case_data.material_category_data import MaterialCategoryData
from utils.mock import Mock


class MaterialData(BaseApi):
    def create_material_normal(self):
        material_category_data = MaterialCategoryData()
        material_category = MaterialCategoryApi()
        mock = Mock()
        specification = mock.mock_data("specification")
        name = mock.mock_data("name")
        code = mock.mock_data("code")
        versions = mock.mock_data("versions")
        variables = material_category_data.create_material_category_normal(material_property="PRODUCT")
        material_category_id = material_category.create_material_category(variables=variables)
        v_material_category_id = {"id": material_category_id}
        args = [("category", v_material_category_id), ("specification", specification), ("name", name),
                ("code", code), ("versions", versions)]
        variables_temp = self.get_variables(variables_name="create_material")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    a = MaterialData()
    print(a.create_material_normal())
