import yaml


class Api:
	env = yaml.safe_load(open("env.yaml"))
	url = "www.sss.com"

	def print_env(self):
		a = self.url.replace("sss", self.env["env_name"]["test2"])
		print(a)


if __name__ == "__main__":
	api = Api()
	api.print_env()
