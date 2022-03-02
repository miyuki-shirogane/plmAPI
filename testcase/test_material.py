import pytest
from hamcrest import *
from apis.material_apis import MaterialApi
from case_data.get_expect import Expect
from case_data.material_data import MaterialData


class TestMaterial:
    data = MaterialData()
    expect = Expect()
    c_v1 = data.create_material_normal()

    exits_l1 = data.is_material_exits_normal_1()
    exits_l2 = data.is_material_exits_normal_2()
    exits_l3 = data.is_material_exits_abnormal_1()
    exits_l4 = data.is_material_exits_abnormal_2()
    exits_l5 = data.is_material_exits_abnormal_3()

    update_v1 = data.update_material_normal_1()
    update_v2 = data.update_material_normal_2()
    update_v3 = data.update_material_abnormal_1()
    update_v4 = data.update_material_abnormal_2()

    def setup(self):
        self.material = MaterialApi()

    @pytest.fixture(scope="function")
    def post_condition(self):
        print("需要做点后置操作")
        yield
        variables_temp = self.data.get_variables(variables_name="create_material")
        pop_keys = ["category", "specification"]
        [variables_temp.pop(k) for k in pop_keys]
        args = [("name", self.data.name), ("code", self.data.code), ("versions", self.data.versions)]
        variables = self.data.modify_variables(target_json=variables_temp, args=args)
        self.material.create_material(variables=variables)

    def test_create_material_normal(self):
        res = self.material.create_material(variables=self.c_v1)
        assert_that(type(res), equal_to(int))

    def test_is_material_exits_normal(self, post_condition):
        res = self.material.is_material_exists(name=self.exits_l1[0], code=self.exits_l1[1], versions=self.exits_l1[2])
        assert_that(res, equal_to(False))

    @pytest.mark.parametrize(
        "v_list,expect", [[exits_l2, False], [exits_l3, True], [exits_l4, True], [exits_l5, True]],
        ids=["正常_相同物料不同版本", "name-code不唯一,同name", "name-code不唯一,同code", "同一产品,版本不唯一"])
    def test_is_material_exits_abnormal(self, v_list, expect):
        res = self.material.is_material_exists(name=v_list[0], code=v_list[1], versions=v_list[2])
        assert_that(res, equal_to(expect))

    @pytest.mark.parametrize(
        "variables, expect", [[update_v1, True], [update_v2, True], [update_v3, "名称、编码不匹配"], [update_v4, "名称、编码不匹配"]],
        ids=["正常", "修改版本", "修改已有名称", "修改已有代码"])
    def test_update_material(self, variables, expect):
        res = self.material.update_material(variables=variables)
        assert_that(res, equal_to(expect))
