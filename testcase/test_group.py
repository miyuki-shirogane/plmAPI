import pytest
from hamcrest import *

from apis.group_apis import GroupApis
from case_data.group_data import GroupData


class TestGroup:
    data = GroupData()

    def setup(self):
        self.group = GroupApis()

    @pytest.fixture(scope="function")
    def _pre_condition_for_is_group_exits(self):
        self.group = GroupApis()
        variables_temp = self.data.get_variables(module_name="group", variables_name="create_project_group")
        args = [("name", self.data.is_name)]
        variables = self.data.modify_variables(target_json=variables_temp, args=args)
        self.group.create_project_group(variables=variables)

    @pytest.fixture(scope="function")
    def _pre_condition_for_remove_member(self):
        self.group = GroupApis()
        variables = self.data.add_member(num=1)
        self.group.add_project_group_member(variables=variables)

    def test_create_group(self):
        c_v = self.data.create_project_group_normal()
        res = self.group.create_project_group(variables=c_v)
        assert_that(type(res), equal_to(int))

    def test_is_group_exits_normal(self):
        name = self.data.is_group_exists()
        res = self.group.is_project_group_name_exists(name=name)
        assert_that(res, equal_to(False))

    # 严格来说，这也不算abnormal。只是预期结果是"已存在"，即True
    def test_is_group_exits_abnormal(self, _pre_condition_for_is_group_exits):
        name = self.data.is_group_exists()
        res = self.group.is_project_group_name_exists(name=name)
        assert_that(res, equal_to(True))

    def test_update_group(self):
        u_v = self.data.update_group()
        res = self.group.update_project_group(variables=u_v)
        assert_that(res, equal_to(True))

    def test_delete_group(self):
        d_v = self.data.delete_group_normal()
        res = self.group.delete_project_group(variables=d_v)
        assert_that(res, equal_to(True))

    def test_add_member(self):
        a_v = self.data.add_member()
        res = self.group.add_project_group_member(variables=a_v)
        assert_that(res, equal_to(True))

    def test_remove_member(self, _pre_condition_for_remove_member):
        r_v = self.data.remove_member()
        res = self.group.remove_project_group_member(variables=r_v)
        assert_that(res, equal_to(True))
