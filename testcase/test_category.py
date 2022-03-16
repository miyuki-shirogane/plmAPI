import pytest
from hamcrest import *
from apis.material_category_apis import MaterialCategoryApi
from case_data.material_category_data import MaterialCategoryData


class TestCategory:
    data = MaterialCategoryData()

    def setup(self):
        self.category = MaterialCategoryApi()

    @pytest.fixture(scope="function")
    def _pre_condition(self):
        self.category = MaterialCategoryApi()
        variables_temp = self.data.get_variables(module_name="category", variables_name="create_material_category")
        args = [("name", self.data.is_name), ("property", "PRODUCT")]
        variables = self.data.modify_variables(target_json=variables_temp, args=args)
        self.category.create_material_category(variables=variables)

    def test_create_category(self):
        c_v = self.data.create_material_category_normal(material_property="PRODUCT")
        res = self.category.create_material_category(variables=c_v)
        assert_that(type(res), equal_to(int))

    def test_is_category_exits_normal(self):
        i_l = self.data.is_category_exits()
        res = self.category.is_material_category_exists(name=i_l[0], property=i_l[1])
        assert_that(res, equal_to(False))

    def test_is_category_exits_abnormal(self, _pre_condition):
        i_l = self.data.is_category_exits()
        res = self.category.is_material_category_exists(name=i_l[0], property=i_l[1])
        assert_that(res, equal_to(True))

    def test_update_category(self):
        u_v = self.data.update_category()
        res = self.category.update_material_category(variables=u_v)
        assert_that(res, equal_to(True))

    def test_delete_category(self):
        d_v = self.data.delete_category_normal()
        res = self.category.delete_category(variables=d_v)
        assert_that(res, equal_to(True))
