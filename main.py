import requests
import json


class Token:
    def _get_headers(self):
        return {'accept': 'application/json', 'Content-Type': 'application/json'}

    def get_token(self):
        payload = {
            "query": '''
mutation login($input: LoginInput!) {
  login(input: $input) {
    token
  }
}
    ''',
            "variables": '''
{
  "input": {
    "account": "admin",
    "password": "teletraan"
  }
}
    '''
        }
        # r = requests.post(
        #     url="https://test2.teletraan.io/graphql",
        #     data=payload,
        #     # data=json.dumps(payload),
        #     headers=self._get_headers())
        # token = str(r.json()['data']['login']['token'])
        # return token
        print(json.dumps(payload))
        print(payload)


if __name__ == "__main__":
    r = Token()
    r.get_token()