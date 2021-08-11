import requests
from datetime import datetime


pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = 'asdhjh4h5u8973fhjkdsh3h4980'
USERNAME = 'murodild'
GRAPH_ID = "graph1"
user_parametres = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#Create user
#response = requests.post(url=pixela_endpoint, json=user_parametres)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":GRAPH_ID,
    "name":"Reading book graph",
    "unit":"pages",
    "type":"int",
    "color":"shibafu"
}
headers = {
    "X-USER-TOKEN":TOKEN
}

#Create pixel for graph
#response = requests.post(url=graph_endpoint,json=graph_params, headers=headers)
#print(res.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()

post_graph_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity":"100"
}

#Add value to pixel for graph
#response_add_value = requests.post(url=pixel_creation_endpoint, json=post_graph_params, headers=headers)
#print(response_add_value.text)


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210810"
update_pixel_params = {
    "quantity":"150"
}

#Update value of pixel for graph
#update_pix_response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
#print(update_pix_response.text)

#Delete pixel on the graph

delete_res = requests.delete(url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20200809", headers=headers)
print(delete_res.text)