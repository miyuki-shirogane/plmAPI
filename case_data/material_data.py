from apis.base_api import BaseApi
from apis.material_apis import MaterialApi
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
        variables_temp = self.get_variables(module_name="material", variables_name="create_material")
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

    @staticmethod
    def _material_info(num: int):
        """
        用法：比如 _material_info(num=0).id
        :param num: list请求中第num个物料信息
        :return: class, 含attribute如下：id, name, code, version
        """
        material = MaterialApi()
        material_info = material.material_list(args=["id", "name", "code", "versions"]).data[num]
        return material_info

    def update_material_normal_1(self):
        material_name = self.mock.mock_data("name")
        material_code = self.mock.mock_data("code")
        material_versions = self.mock.mock_data("versions")
        material_id = MaterialData._material_info(num=0).id
        args = [("id", material_id),
                ("name", material_name), ("code", material_code), ("versions", material_versions)]
        variables_temp = self.get_variables(module_name="material", variables_name="update_material")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_material_normal_2(self):
        info_0 = MaterialData._material_info(0)
        material_versions = self.mock.mock_data("versions")
        args = [("id", info_0.id), ("name", info_0.name), ("code", info_0.code), ("versions", material_versions)]
        variables_temp = self.get_variables(module_name="material", variables_name="update_material")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_material_abnormal_1(self):
        info_0 = MaterialData._material_info(0)
        info_1 = MaterialData._material_info(1)
        args = [("id", info_0.id), ("name", info_1.name), ("code", info_0.code), ("versions", info_0.versions)]
        variables_temp = self.get_variables(module_name="material", variables_name="update_material")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_material_abnormal_2(self):
        info_0 = MaterialData._material_info(0)
        info_1 = MaterialData._material_info(1)
        args = [("id", info_0.id), ("name", info_0.name), ("code", info_1.code), ("versions", info_0.versions)]
        variables_temp = self.get_variables(module_name="material", variables_name="update_material")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def delete_material_normal(self):
        material_id = MaterialData._material_info(num=0).id
        return [material_id]


if __name__ == '__main__':
    a = MaterialData()
    print(a.delete_material_normal())
