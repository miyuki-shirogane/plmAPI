from apis.base_api import BaseApi
from apis.group_apis import GroupApis
from utils.mock import Mock


class GroupData(BaseApi):
    mock = Mock()
    group_name = mock.mock_data("group")
    is_name = mock.mock_data("group")

    @staticmethod
    def _group_info(num: int):
        group = GroupApis()
        group_info = group.project_group_list(args=["data"]).data[num]
        return group_info

    def create_project_group_normal(self):
        variables_temp = self.get_variables(module_name="group", variables_name="create_project_group")
        args = [("name", self.group_name)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def is_group_exists(self):
        return self.is_name

    def delete_group_normal(self):
        group_id = GroupData._group_info(num=0).id
        return [group_id]

    def update_group(self):
        group_id = GroupData._group_info(num=0).id
        group = self.mock.mock_data("group")
        args = [("id", group_id), ("name", group)]
        variables_temp = self.get_variables(module_name="group", variables_name="update_project_group")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables


if __name__ == '__main__':
    g = GroupData()
    print(g.update_group())
