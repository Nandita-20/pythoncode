import requests

response = requests.get("https://reqres.in/api/users?page=2")
print(response) #it will return the status code

print(response.content) #it will display the contents of response
print("\n")
print(response.headers) #it will display the header information

