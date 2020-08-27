import requests
import json
import sys

trigger_name = sys.argv[1]
host_name = sys.argv[2]
print(trigger_name)
print(host_name)

rundeck_url = 'http://x.x.x.x:4440/api/35'

findpayload = {
            'jobExactFilter': trigger_name
            }
headers = {
    'Accept': 'application/json',
    'X-Rundeck-Auth-Token': 'xxxxxxxxxxxxxxxxx'
}
resp = requests.get (
    rundeck_url + '/project/pro2/jobs', params=findpayload, headers=headers
)
result = resp.content.decode('utf8').replace("'", '"')
result = json.loads(result)
id = result[0]['id']
print (result[0]['id'])

runpayload = {
	"filter": host_name
}

run = requests.post(
    rundeck_url + '/job/' + id + '/run', params=runpayload, headers=headers
)
