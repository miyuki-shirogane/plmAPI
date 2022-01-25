from apis.project_apis import ProjectApis


class TestProject:
    def setup(self):
        self.project = ProjectApis()

    def test_product_project(self):
        c = self.project.product_project_list(args=["id"], search="rs6", category=["CUSTOMIZATION"])
        pid = c.data[0].id
        detail = self.project.product_project(project_id=pid)
        print(detail)
        