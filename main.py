import requests
from datetime import datetime
USERNAME = "fforfebstar"
TOKEN = "1machukwu1234"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    'id': 'graph1',
    'name': 'Coding graph',
    'unit': 'Commit',
    'type': 'int',
    'color': 'sora'
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_post_endpoint = f"{graph_endpoint}/{graph_config['id']}"
today = datetime.today()


pixel_config = {
    'date': today.strftime("%Y%m%d"),
    'quantity': '9',
}

# response = requests.post(url=pixel_post_endpoint, json=pixel_config, headers=headers)
# print(response.text)
#

graph_change_endpoint = f"{pixel_post_endpoint}/{pixel_config['date']}"

response = requests.put(url=graph_change_endpoint, json=pixel_config, headers=headers)
print(response.text)

