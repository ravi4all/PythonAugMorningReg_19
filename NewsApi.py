import json
import urllib.request as url

res = url.urlopen('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=695e07af402f4b119f0703e9b19f4683')
data = json.load(res)
# print(data)

articles = data['articles']
# print(articles[0]['title'])
for i in range(len(articles)):
    print(articles[i]['title'])