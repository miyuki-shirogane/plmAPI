from apis.base_api import BaseApi
from utils.mock import Mock
from apis.project_apis import ProjectApis


class Data(BaseApi):
    mock = Mock()
    project = ProjectApis()
    name = mock.mock_data(data_name="name")
    code = mock.mock_data(data_name="code")

    # CREATE_PRODUCT_PROJECT
    def create_product_project_normal(self):
        args = [("name", self.name), ("code", self.code)]
        variables_temp = self.get_variables(variables_name="create_product_project_temp")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_product_project_duplicate(self):
        res = self.create_product_project_normal()
        return res

    def create_product_project_no_project_group(self):
        name = self.mock.mock_data(data_name="name")
        code = self.mock.mock_data(data_name="code")
        args = [("name", name), ("code", code), ("projectGroup", [])]
        variables_temp = self.get_variables(variables_name="create_product_project_temp")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def create_product_project_not_exist_group(self):
        name = self.mock.mock_data(data_name="name")
        code = self.mock.mock_data(data_name="code")
        args = [("name", name), ("code", code), ("projectGroup", [{"id": 10000}])]
        variables_temp = self.get_variables(variables_name="create_product_project_temp")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    # ADD_PRODUCT_TASK
    def add_product_task_normal(self):
        # 得查询一下最新的project_id是多少; 实现的方案是通过接口调用查询
        project_id = self.project.product_project_list(args=["id"]).data[0].id
        variables = self.get_variables(variables_name="add_product_task")
        variables["project"]["id"] = project_id
        # variables["task"][0]["name"] = task_name
        variables["task"][0]["planEndAt"] = variables["task"][0]["planStartAt"] = self.mock.current_time()
        return variables


if __name__ == '__main__':
    data = Data()
    data.add_product_task_normal()
