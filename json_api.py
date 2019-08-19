import json
import urllib.request as url

http = url.urlopen('https://cricapi.com/api/playerStats?apikey=b7CYzlyYOrUCIIdbSlU753oGKN12&pid=35319')
data = json.load(http)

name = data["fullName"]
print("Name :",name)
profile = data['profile']
print("Profile :",profile)

batting = data['data']['batting']['tests']
for item in batting.items():
    print(item[0],"-",item[1])
