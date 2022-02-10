import os
import yaml


class Expect:
    def get_expect(self, module, interface, situation):
        root_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(root_path, "expect.yaml")
        with open(config_path, encoding='utf-8') as f:
            datas = yaml.safe_load(f)
            res = datas.get(module).get(interface).get(situation)
            return res


if __name__ == '__main__':
    e = Expect()
    print(e.get_expect("project", "create_product_project", "duplicate"))