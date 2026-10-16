import requests
url = "https://jsonplaceholder.typicode.com/users"
response=requests.get(url)
data=response.json()
for user in data:
    print("Name:",user['name'])
    print("Email:",user['email'])
    print("Company:",user['company']['name'])