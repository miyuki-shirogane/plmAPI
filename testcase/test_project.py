import pytest
from hamcrest import *

from apis.material_apis import MaterialApi
from apis.project_apis import ProjectApis
from case_data.get_expect import Expect
from case_data.material_data import MaterialData
from case_data.project_data import ProjectData


class TestProject:
    material = MaterialApi()
    material_data = MaterialData()
    data = ProjectData()
    expect = Expect()
    c_v1 = data.create_product_project_normal()
    c_v2 = c_v1
    c_v3 = data.create_product_project_no_project_group()
    c_v4 = data.create_product_project_not_exist_group()

    c_e1 = expect.get_expect("project", "create_product_project", "duplicate")
    c_e2 = expect.get_expect("project", "create_product_project", "miss_require")
    c_e3 = expect.get_expect("project", "create_product_project", "not_exist_group")

    bl_e1 = 13
    bl_e2 = 58

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

    def test_delete_bom(self):
        bom_id = self.data.delete_bom()
        res = self.project.delete_bom(bom_id=bom_id)
        assert_that(res, equal_to(True))

    def test_add_bom_material(self):
        material_count = len(self.material.material_list(args=["name"]).data)
        if material_count >= 2:
            pass
        elif material_count < 2:
            for i in range(2-material_count):
                c_v = self.material_data.create_material_normal()
                self.material.create_material(variables=c_v)
        # 输出形如：[150, 149]
        material_ids = [i.id for i in self.material.material_list(args=["id"]).data][0:2]
        for material_id in material_ids:
            a_v = self.data.add_bom_material(material_id=material_id)
            res = self.project.add_bom_material(variables=a_v)
            assert_that(res, equal_to(True))

    def test_remove_bom_material(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        task_id = self.project.product_task_list(args=["id"], project=[{"id": project_id}]).data[0].id
        bom_id = self.project.bom_list(args=["id"], task=[{"id": task_id}]).data[0].id
        remove_material_id = [i.id for i in self.project.bom_material_list(args=["id"], bom=[{"id": bom_id}]).data][0:1]
        res = self.project.remove_bom_material(material_id=remove_material_id)
        assert_that(res, equal_to(True))

    def test_update_bom_material(self):
        u_v = self.data.update_bom_material()
        res = self.project.update_bom_material(variables=u_v)
        assert_that(res, equal_to(True))

    def test_end_product_project(self):
        e_v = self.data.end_product_project()
        res = self.project.end_product_project(variables=e_v)
        assert_that(res, equal_to(True))

    # released BOM 筛选查询，比较常用；也是工艺优化流程中会用到的查询，相较其他更重要一点
    @pytest.mark.parametrize("is_released,expect", [[True, bl_e1], [False, bl_e2]], ids=["已定版BOM", "未定版BOM"])
    def test_bom_list(self, is_released, expect):
        res_count = len(self.project.bom_list(args=["id"], is_released=is_released).data)
        assert_that(res_count, equal_to(expect))
