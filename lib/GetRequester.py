import requests
import json


class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):

        response = requests.get(self.url)
        return response.content

    def load_json(self):

        return json.loads(self.get_response_body())


get_requester = GetRequester(
    'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()
print(get_requester)


# url = "https://jsonplaceholder.typicode.com/todos/1"
# requester = GetRequester(url)
# response_body = requester.get_response_body()
# todo = requester.load_json()

# for response in set(response_body):

#     print(response)
