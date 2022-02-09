from apis.base_api import BaseApi
from utils.mock import Mock


class Data(BaseApi):
    mock = Mock()
    name = mock.mock_data(data_name="name")
    code = mock.mock_data(data_name="code")

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


if __name__ == '__main__':
    data = Data()
    print(data.create_product_project_no_project_group())
