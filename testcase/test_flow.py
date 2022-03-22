import pytest
from hamcrest import *

from apis.flow_apis import FlowApis
from case_data.flow_data import FlowData


class TestFlow:
    data = FlowData()

    def setup(self):
        self.flow = FlowApis()

    @pytest.fixture(scope="function")
    def _pre_condition(self):
        self.flow = FlowApis()
        variables_temp = self.data.get_variables(module_name="flow", variables_name="create_product_flow")
        args = [("name", self.data.is_name), ("taskConfiguration", [{"name": self.data.task_name}])]
        variables = self.data.modify_variables(target_json=variables_temp, args=args)
        self.flow.create_product_flow(variables=variables)

    def test_create_flow(self):
        c_v = self.data.create_product_flow_normal()
        res = self.flow.create_product_flow(variables=c_v)
        assert_that(type(res), equal_to(int))

    def test_is_flow_exits_normal(self):
        name = self.data.is_flow_exists()
        res = self.flow.is_product_flow_exists(name=name)
        assert_that(res, equal_to(False))

    # 严格来说，这也不算abnormal。只是预期结果是"已存在"，即True
    def test_is_flow_exits_abnormal(self, _pre_condition):
        name = self.data.is_flow_exists()
        res = self.flow.is_product_flow_exists(name=name)
        assert_that(res, equal_to(True))

    def test_update_flow(self):
        u_v = self.data.update_flow()
        res = self.flow.update_product_flow(variables=u_v)
        assert_that(res, equal_to(True))

    def test_delete_category(self):
        d_v = self.data.delete_flow_normal()
        res = self.flow.delete_product_flow(variables=d_v)
        assert_that(res, equal_to(True))