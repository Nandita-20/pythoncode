#requirement: create new entity using POST() call

import requests
import json
import jsonpath
url="https://reqres.in//api/users"
#open the file wherewe passed the header of the New Entity
file=open('C:\\Nandita\\createuser1.json','r')
#read th file
json_input = file.read()
request_json = json.loads(json_input)
#post the request
res = requests.post(url,request_json)
print(res.status_code)


'''res_load=json.loads(res.text)
id=jsonpath.jsonpath(res_load,'id')
print(id[0])'''