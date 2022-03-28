from apis.base_api import BaseApi
from apis.flow_apis import FlowApis
from apis.user_apis import User
from utils.mock import Mock
from apis.project_apis import ProjectApis


class ProjectData(BaseApi):
    mock = Mock()
    project = ProjectApis()
    flow = FlowApis()
    user = User()
    company_id = user.get_user().company.id
    name = mock.mock_data(data_name="name")
    code = mock.mock_data(data_name="code")

    def _create_project(self):
        """
        desc: 设置项目研发产品的前置条件
        :return: project id
        """
        v = self.create_product_project_normal()
        res = self.project.create_product_project(variables=v)
        return res

    def _set_project_product(self, project_id: int):
        self.project.set_project_product()

    # CREATE_PRODUCT_PROJECT
    def create_product_project_normal(self):
        args = [("name", self.name), ("code", self.code)]
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
        project_id = self._create_project()
        variables = self.get_variables(module_name="project", variables_name="set_project_product")
        variables["project"]["id"] = project_id
        for i in ["name", "code", "versions", "unit"]:
            column = self.mock.mock_data(i)
            variables["product"][i] = column
        return variables

    def end_product_project(self, project_id: int):
        variables = self.get_variables(module_name="project", variables_name="end_product_project")
        variables["id"] = project_id
        return variables

    # ADD_PRODUCT_TASK；这里不太一样，一旦添加成功，页面上就不允许再添加了。但是接口层面是允许再加的，不晓得有没有问题。
    def add_product_task_normal(self):
        # 得查询一下最新的project_id是多少; 实现的方案是通过接口调用查询
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        flow_ids = self.flow.product_flows(args=["id"])
        flow_id = flow_ids[0].id
        flow_detail = self.flow.product_flow(flow_id=flow_id, args=["task_template"])
        task_name = flow_detail.task_template[0].name
        variables = self.get_variables(module_name="project", variables_name="add_product_task")
        variables["project"]["id"] = project_id
        variables["task"][0]["name"] = task_name
        variables["task"][0]["planEndAt"] = variables["task"][0]["planStartAt"] = self.mock.current_time()
        return variables


if __name__ == '__main__':
    data = ProjectData()
    print(data.set_product_project())
