import requests
from datetime import datetime
username = "pranaydommati"
token = "xyz123ABC"
pixela_endpoint = " https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
n_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/graph1"
update_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/graph1/20240119"
delete_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/graph1/20240119"
headers = {
    "X-USER-TOKEN":token
}
# user_parameters = {
#     "token":token,
#     "username":username,
#     "agreeTermsOfService":"yes",
#     "notMinor":"yes"
# }

# response = requests.post(url=pixela_endpoint,json=user_parameters)
# graph_params =  {
#     "id":"graph1",
#     "name":"cycling graph",
#     "unit":"Km",
#     "type":"float",
#     "color":"ajisai"
# }

# response_graph = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
# print(response_graph.text)
now = datetime.now()
n_pixel_params = {
    "date": now.strftime("%Y%m%d"),
    "quantity": input("Enter how many km you cycled:")
}
response = requests.post(url=n_pixel_endpoint,json=n_pixel_params,headers=headers)
print(response.text)
# update_params = {
#     "quantity":"2.0"
# }
# update_params = {
#     "quantity":"2.0"
# }
# response_pixel_update = requests.put(url=update_pixel_endpoint,json=update_params,headers=headers)
# print(response_pixel_update.text)
# response_pixel_delete = requests.delete(url=update_pixel_endpoint,headers=headers)
# print(response_pixel_delete.text)