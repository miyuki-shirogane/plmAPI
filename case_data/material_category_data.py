from apis.base_api import BaseApi
from utils.mock import Mock


class MaterialCategoryData(BaseApi):
    mock = Mock()
    name = mock.mock_data("category_name")

    def create_material_category_normal(self, material_property: str):
        """
        :param material_property:PRODUCT, RAW_MATERIAL, INTERMEDIATE, BACTERIA
        :return:
        """
        args = [("name", self.name), ("property", material_property)]
        variables_temp = self.get_variables(variables_name="create_material_category")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    d = MaterialCategoryData()
    print(d.create_material_category_normal(material_property="PRODUCT"))
