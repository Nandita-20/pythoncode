import requests

respons = "https://reqres.in/api/users/2"
print(respons)

res=requests.delete(respons)
print(res.status_code)

assert res.status_code==204
#result if the delete all executed successfully then 204 code will be returned.