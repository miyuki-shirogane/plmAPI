from apis.base_api import BaseApi
from apis.flow_apis import FlowApis
from apis.group_apis import GroupApis
from apis.user_apis import User
from case_data.group_data import GroupData
from utils.mock import Mock
from apis.project_apis import ProjectApis


class ProjectData(BaseApi):
    mock = Mock()
    project = ProjectApis()
    group = GroupApis()
    group_data = GroupData()
    flow = FlowApis()
    user = User()
    company_id = user.get_user().company.id
    name = mock.mock_data(data_name="name")
    code = mock.mock_data(data_name="code")

    def _create_project_get_group_id(self, member_num: int):
        c_v = self.group_data.create_project_group_normal()
        group_id = self.group.create_project_group(variables=c_v)
        for i in range(member_num):
            a_v = self.group_data.add_member(num=i)
            self.group.add_project_group_member(variables=a_v)
            i += 1
        return group_id

    def _get_member_info(self, member_num: int):
        group_id = self.group.project_group_list(args=["data"]).data[0].id
        member_info = self.group.project_group_member_list(group_id=group_id, args=["member"])
        res = []
        for i in range(member_num):
            res.append(member_info[i].member.id)
            i += 1
        return res

    # CREATE_PRODUCT_PROJECT
    def create_product_project_normal(self):
        # 创建小组，内含3个成员。返回小组id
        group_id = ProjectData._create_project_get_group_id(self, member_num=3)
        args = [("name", self.name), ("code", self.code), ("projectGroup", [{"id": group_id}])]
        variables_temp = self.get_variables(module_name="project", variables_name="create_product_project")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_product_project_no_project_group(self):
        name = self.mock.mock_data(data_name="name")
        code = self.mock.mock_data(data_name="code")
        args = [("name", name), ("code", code), ("projectGroup", [])]
        variables_temp = self.get_variables(module_name="project", variables_name="create_product_project")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_product_project_not_exist_group(self):
        name = self.mock.mock_data(data_name="name")
        code = self.mock.mock_data(data_name="code")
        args = [("name", name), ("code", code), ("projectGroup", [{"id": 10000}])]
        variables_temp = self.get_variables(module_name="project", variables_name="create_product_project")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def set_project_product(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        variables = self.get_variables(module_name="project", variables_name="set_project_product")
        variables["project"]["id"] = project_id
        for i in ["name", "code", "versions", "unit"]:
            column = self.mock.mock_data(i)
            variables["product"][i] = column
        return variables

    # def end_product_project(self):
    #     project_id = self.project.product_project_list(args=["id"]).data[0].id
    #     variables = self.get_variables(module_name="project", variables_name="end_product_project")
    #     variables["id"] = project_id
    #     return variables

    # ADD_PRODUCT_TASK；这里不太一样，一旦添加成功，页面上就不允许再添加了。但是接口层面是允许再加的，不晓得有没有问题。
    def add_product_task_normal(self):
        # 得查询一下最新的project_id是多少; 实现的方案是通过接口调用查询
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        flow_ids = self.flow.product_flows(args=["id"])
        flow_id = flow_ids[0].id
        flow_detail = self.flow.product_flow(flow_id=flow_id, args=["task_template"])
        task_name = flow_detail.task_template[0].name
        mem_id_list = ProjectData._get_member_info(self, member_num=3)
        executive = mem_id_list[0]
        mem_id_list.pop(0)
        participant_list = mem_id_list
        variables = self.get_variables(module_name="project", variables_name="add_product_task")
        variables["project"]["id"] = project_id
        variables["task"][0]["name"] = task_name
        variables["task"][0]["planEndAt"] = variables["task"][0]["planStartAt"] = self.mock.current_time()
        variables["task"][0]["executive"] = {"id": executive}
        variables["task"][0]["participant"] = [{"id": participant_list[0]}, {"id": participant_list[1]}]
        return variables

    def update_product_task(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        variables = self.get_variables(module_name="project", variables_name="update_product_task")
        task_info = self.project.product_task_list(
            args=["id", "name", "plan_start_at", "plan_end_at"], project=[{"id": project_id}]).data[0]
        mem_id_list = ProjectData._get_member_info(self, member_num=3)
        executive = mem_id_list[0]
        mem_id_list.pop(0)
        participant_list = mem_id_list
        variables["executive"] = {"id": executive}
        variables["participant"] = [{"id": participant_list[0]}, {"id": participant_list[1]}]
        variables["id"] = task_info.id
        variables["name"] = task_info.name
        variables["planEndAt"] = task_info.plan_end_at
        variables["planStartAt"] = self.mock.current_time()-86400000
        return variables

    def start_product_project(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        return project_id

    def create_task_bom(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        variables_temp = self.get_variables(module_name="project", variables_name="create_task_bom")
        task_id = self.project.product_task_list(args=["id"], project=[{"id": project_id}]).data[0].id
        bom_versions = self.mock.mock_data("versions")
        args = [("task", {"id": task_id}), ("versions", bom_versions)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_bom(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        task_id = self.project.product_task_list(args=["id"], project=[{"id": project_id}]).data[0].id
        bom_id = self.project.bom_list(args=["id"], task=[{"id": task_id}]).data[0].id
        variables_temp = self.get_variables(module_name="project", variables_name="update_bom")
        bom_versions = self.mock.mock_data("versions")
        args = [("id", bom_id), ("versions", bom_versions)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def delete_bom(self):
        c_v = self.create_task_bom()
        bom_id = self.project.create_task_bom(variables=c_v)
        return bom_id

    def add_bom_material(self, material_id: int):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        task_id = self.project.product_task_list(args=["id"], project=[{"id": project_id}]).data[0].id
        bom_id = self.project.bom_list(args=["id"], task=[{"id": task_id}]).data[0].id
        variables_temp = self.get_variables(module_name="project", variables_name="add_bom_material")
        args = [("bom", {"id": bom_id}), ("material", [{"id": material_id}])]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def update_bom_material(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        task_id = self.project.product_task_list(args=["id"], project=[{"id": project_id}]).data[0].id
        bom_id = self.project.bom_list(args=["id"], task=[{"id": task_id}]).data[0].id
        material_info = self.project.bom_material_list(args=["material"], bom=[{"id": bom_id}])
        material_id = material_info.data[0].material.id
        research_unit = self.mock.mock_data("researchUnit")
        variables = self.get_variables(module_name="project", variables_name="update_bom_material")
        variables["bom"]["id"] = bom_id
        variables["bomMaterial"][0]["material"]["id"] = material_id
        variables["bomMaterial"][0]["researchUnit"] = research_unit
        return variables

    def end_product_project(self):
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        task_id = self.project.product_task_list(args=["id"], project=[{"id": project_id}]).data[0].id
        bom_id = self.project.bom_list(args=["id"], task=[{"id": task_id}]).data[0].id
        description = self.mock.mock_data("description")
        variables_temp = self.get_variables(module_name="project", variables_name="end_product_project")
        args = [("bom", {"id": bom_id}), ("id", project_id), ("description", description)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    data = ProjectData()
    print(data.end_product_project())
