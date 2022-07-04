import os

import pytest
import yaml

from apis.user_apis import User
from case_data.user_data import UserData


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# def pytest_addoption(parser):
#     mygroup = parser.getgroup("teletraan")
#     mygroup.addoption("--env",
#                       default='test',
#                       dest='env',
#                       help='set your run env'
#                       )
#
#
# @pytest.fixture(scope='session')
# def cmd_option(request):
#     return request.config.getoption("--env")
#
#
# @pytest.fixture(scope="session")
# def cmd_option(request):
#     url = "https://env.teletraan.io/graphql"
#     my_env = request.config.getoption("--env", default="test")
#     current_path = os.getcwd()
#     data_path = os.path.join(current_path, "util/env.yaml")
#     with open(data_path) as f:
#         datas = yaml.safe_load(f)
#     if my_env == "test":
#         url.replace("env", datas["env"]["test2"]["name"])
#         return url, datas["env"]["test2"]
#     if my_env == "teamsit":
#         url.replace("env", datas["env"]["teamsit"]["name"])
#         return url, datas["env"]["teamsit"]


data = UserData()
user = User()
user_count = data.user_count()
role_count = data.role_count()


# 创建一下用户、角色
@pytest.fixture(scope="session", autouse=True)
def pre_condition_for_the_satiation():
    if role_count >= 2:
        pass
    elif role_count < 2:
        for i in range(2-role_count):
            v_create_role = data.create_role()
            user.create_role(variables=v_create_role)
    if user_count >= 5:
        pass
    elif user_count < 5:
        for i in range(5-user_count):
            v_create_user = data.create_user()
            user.create_user(variables=v_create_user)

