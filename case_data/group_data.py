from apis.base_api import BaseApi
from apis.group_apis import GroupApis
from apis.user_apis import User
from utils.mock import Mock


class GroupData(BaseApi):
    mock = Mock()
    group = GroupApis()
    g_th = User()

    is_name = mock.mock_data("group")

    def _group_info(self, num: int):
        group_info = self.group.project_group_list(args=["data"]).data[num]
        return group_info

    def _group_members_info(self):
        group_id = self._group_info(num=0).id
        members_info = self.group.project_group_member_list(group_id=group_id)
        return members_info

    def create_project_group_normal(self):
        group_name = self.mock.mock_data("group")
        variables_temp = self.get_variables(module_name="group", variables_name="create_project_group")
        args = [("name", group_name)]
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def is_group_exists(self):
        return self.is_name

    def delete_group_normal(self):
        group_id = self._group_info(num=0).id
        return [group_id]

    def update_group(self):
        group_id = self._group_info(num=0).id
        group = self.mock.mock_data("group")
        args = [("id", group_id), ("name", group)]
        variables_temp = self.get_variables(module_name="group", variables_name="update_project_group")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def add_member(self, num=0):
        # 第一个小组id
        group_id = self._group_info(num=0).id
        # 第num个人员id
        member_id = self.g_th.users_info().data[num].id
        args = [("member", [{"id": member_id}]), ("projectGroup", {"id": str(group_id)})]
        variables_temp = self.get_variables(module_name="group", variables_name="add_project_group_member")
        variables = self.modify_variables(target_json=variables_temp, args=args)
        return variables

    def remove_member(self, num=0):
        member_id = self._group_members_info()[num].id
        return [member_id]


if __name__ == '__main__':
    g = GroupData()
    print(g.add_member())
