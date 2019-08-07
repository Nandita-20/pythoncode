import requests
import json
import jsonpath

response=requests.get("https://reqres.in/api/users?page=2")

#parse the contents into json format

json_format=json.loads(response.text)
print(json_format)

#fetch values using jsonpath

result=jsonpath.jsonpath(json_format,'total_pages')
print(result[0]) #or
#assert result[0]==4 #user assert to validate the result