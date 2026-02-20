# Project - Habit Tracker via Pixela
# -----------------------------------

import requests
from datetime import datetime

My_Piixela_API_Token = "ENTER YOUR OWN CUSTOM API or TOKEN KEY"
My_Pixela_User_Name = "ENTER YOUR OOWN CUSTOM USER NAME"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# --------------- USER DATA ---------------- #
pixela_endpoint = "https://pixe.la/v1/users"

# ---------------- CREATE USER ---------------- #

user_params = {
    "token": My_Piixela_API_Token,
    "username": My_Pixela_User_Name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Uncomment only first time
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# ---------------- CREATE GRAPH ---------------- #
graph_endpoint = f"{pixela_endpoint}/{My_Pixela_User_Name}/graphs"

headers = {
    "X-USER-TOKEN": My_Piixela_API_Token}

graph_config = {
    "id": GRAPH_ID,
    "name": "cycling",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

# Uncomment only once
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# ---------------- UPDATE GRAPH ---------------- #
update_endpoint = f"{pixela_endpoint}/{My_Pixela_User_Name}/graphs/{GRAPH_ID}"

update_data = {
    "name": "Python Coding Tracker",
    "unit": "hours",
    "color": "ajisai",
    "type": "int"
}

response = requests.put(
    url=update_endpoint,
    json=update_data,
    headers=headers
)

print("Update:", response.text)

# ------------------DELETE PIXEL--------------#
today = datetime.now().strftime("%Y%m%d")

delete_pixel_endpoint = f"{pixela_endpoint}/{My_Pixela_User_Name}/graphs/{GRAPH_ID}/{today}"

# response = requests.delete(url=delete_pixel_endpoint,headers=headers)
# print(response.text)

# ---------------- ADD PIXEL ---------------- #
today = datetime.now().strftime("%Y%m%d")

pixel_endpoint = f"{pixela_endpoint}/{My_Pixela_User_Name}/graphs/{GRAPH_ID}"

pixel_data = {
    "date": today,
    "quantity": input("Enter Your Total Hours that you Spent Time")
}

response = requests.post(url=pixel_endpoint,json=pixel_data,headers=headers)
print("Add Pixel:", response.text)