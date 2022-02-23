from hamcrest import *

from apis.material_apis import MaterialApi
from case_data.material_data import MaterialData


class TestMaterial:
    data = MaterialData()
    c_v1 = data.create_material_normal()

    def setup(self):
        self.material = MaterialApi()

    def test_create_material_normal(self):
        res = self.material.create_material(variables=self.c_v1)
        assert_that(type(res), equal_to(int))

    def test_is_material_exits(self):
        pass
