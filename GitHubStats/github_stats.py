import datetime
import json
import requests
def d_resp(repo,code):

        stime = repo['updated_at']
        st1 = datetime.datetime.strptime(stime, '%Y-%m-%dT%H:%M:%SZ')
        nowtime = st1 + datetime.timedelta(hours=8)
        nowtime1 = nowtime.strftime('%Y-%m-%d %H:%M:%S')

        new_resp = {}
        new_resp['status_code'] = code
        new_resp['name'] = repo['name']
        new_resp['updated_at_bj'] = nowtime1
        new_resp['stargazers_count'] = repo['stargazers_count']

        return new_resp
user = input('请输入你要请求的用户：')
resp = requests.get(f'https://api.github.com/users/{user}/repos',timeout=10)

if resp.status_code != 200:
        exit("没找到这个用户，请检查用户名")

resp1 = json.loads(resp.text)

li = []
for i in resp1:
        li.append(d_resp(i,resp.status_code))

with open('repos.json', 'w',encoding="utf-8") as outfile:
        json.dump(li, outfile, ensure_ascii=False, indent=2)