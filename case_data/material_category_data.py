from apis.base_api import BaseApi
from apis.material_category_apis import MaterialCategoryApi
from utils.mock import Mock


class MaterialCategoryData(BaseApi):
    mock = Mock()
    name = mock.mock_data("category_name")
    is_name = mock.mock_data("category")

    def create_material_category_normal(self, material_property: str):
        """
        :param material_property:PRODUCT, RAW_MATERIAL, INTERMEDIATE, BACTERIA
        :return:
        """
        args = [("name", self.name), ("property", material_property)]
        variables_temp = self.get_variables(module_name="category", variables_name="create_material_category")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def is_category_exits(self):
        return [self.is_name, "PRODUCT"]

    @staticmethod
    def _category_info(num: int):
        category = MaterialCategoryApi()
        category_info = category.material_category_list(args=["id", "name", "property"]).data[num]
        return category_info

    def update_category(self):
        category_id = MaterialCategoryData._category_info(num=0).id
        name = self.mock.mock_data("name")
        args = [("id", category_id), ("name", name), ("property", "RAW_MATERIAL")]
        variables_temp = self.get_variables(module_name="category", variables_name="update_material_category")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def delete_category_normal(self):
        category_id = MaterialCategoryData._category_info(num=0).id
        return [category_id]


if __name__ == '__main__':
    d = MaterialCategoryData()
    print(d.delete_category_normal())
