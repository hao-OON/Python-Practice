import datetime
import json
import requests

resp = requests.get('https://api.github.com/users/hao-OON/repos',timeout=10)

resp1 = json.loads(resp.text)

stime = resp1[0]['updated_at']
st1 = datetime.datetime.strptime(stime, '%Y-%m-%dT%H:%M:%SZ')
nowtime = st1 + datetime.timedelta(hours=8)
nowtime1 = nowtime.strftime('%Y-%m-%d %H:%M:%S')

new_resp = {}
new_resp['status_code'] = resp.status_code
new_resp['name'] = resp1[0]['name']
new_resp['updated_at_bj'] = nowtime1
new_resp['stargazers_count'] = resp1[0]['stargazers_count']

records = []
records.append(new_resp)
with open('repos.json', 'w',encoding="utf-8") as outfile:
        json.dump(records, outfile, ensure_ascii=False, indent=2)