import pytest
from hamcrest import *
from apis.project_apis import ProjectApis
from case_data.get_expect import Expect
from case_data.project_data import ProjectData


class TestProject:
    data = ProjectData()
    expect = Expect()
    c_v1 = data.create_product_project_normal()
    c_v2 = c_v1
    c_v3 = data.create_product_project_no_project_group()
    c_v4 = data.create_product_project_not_exist_group()

    c_e1 = expect.get_expect("project", "create_product_project", "duplicate")
    c_e2 = expect.get_expect("project", "create_product_project", "miss_require")
    c_e3 = expect.get_expect("project", "create_product_project", "not_exist_group")

    def setup(self):
        self.project = ProjectApis()

    # CREATE PRODUCT PROJECT
    def test_create_product_project_normal(self):
        res = self.project.create_product_project(variables=self.c_v1)
        assert_that(type(res), equal_to(int))

    """
    以下的异常场景部分依赖上面的normal场景。
    比如 duplicate 场景，需要拷贝上面的参数，那你上面如果不执行，也就谈不上重复了。
    """
    @pytest.mark.parametrize(
        "variables,expect", [[c_v2, c_e1], [c_v3, c_e2], [c_v4, c_e3]], ids=["重复名称编码", "执行小组为空", "不存在的小组id"])
    def test_create_product_project_abnormal(self, variables, expect):
        res = self.project.create_product_project(variables=variables)
        assert_that(res, equal_to(expect))

    def test_set_project_product(self):
        variables = self.data.set_project_product()
        res = self.project.set_project_product(variables=variables)
        assert_that(res, equal_to(True))

    # ADD PRODUCT TASK
    def test_add_product_task_normal(self):
        a_v1 = self.data.add_product_task_normal()
        res = self.project.add_product_task(variables=a_v1)
        assert_that(res, equal_to(True))

    def test_update_product_task(self):
        u_v = self.data.update_product_task()
        res = self.project.update_product_task(variables=u_v)
        assert_that(res, equal_to(True))

    def test_start_project(self):
        project_id = self.data.start_product_project()
        res = self.project.start_product_project(project_id=project_id)
        assert_that(res, equal_to(True))

    def test_create_task_bom(self):
        c_v = self.data.create_task_bom()
        res = self.project.create_task_bom(variables=c_v)
        assert_that(type(res), equal_to(int))

    def test_update_bom(self):
        u_v = self.data.update_bom()
        res = self.project.update_bom(variables=u_v)
        assert_that(res, equal_to(True))
