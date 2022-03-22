from apis.base_api import BaseApi
from apis.flow_apis import FlowApis
from utils.mock import Mock


class FlowData(BaseApi):
    mock = Mock()
    flow_name = mock.mock_data("flow")
    task_name = mock.mock_data("task")
    is_name = mock.mock_data("flow")

    @staticmethod
    def _flow_info(num: int):
        flow = FlowApis()
        flow_info = flow.product_flows(args=["id", "name"])[num]
        return flow_info

    def create_product_flow_normal(self):
        variables_temp = self.get_variables(module_name="flow", variables_name="create_product_flow")
        args = [("name", self.flow_name), ("taskConfiguration", [{"name": self.task_name}])]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def is_flow_exists(self):
        return self.is_name

    def delete_flow_normal(self):
        flow_id = FlowData._flow_info(num=0).id
        return [flow_id]

    def update_flow(self):
        flow_id = FlowData._flow_info(num=0).id
        flow = self.mock.mock_data("flow")
        task = self.mock.mock_data("task")
        args = [("id", flow_id), ("name", flow), ("taskConfiguration", [{"name": task}])]
        variables_temp = self.get_variables(module_name="flow", variables_name="update_product_flow")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    f = FlowData()
    print(f.update_flow())
