import urllib.request as url
import bs4

res = url.urlopen('https://www.marvel.com/movies')
page = bs4.BeautifulSoup(res)
images = page.find_all('img')
for i in range(len(images)):
    path = images[i]['src']
    url.urlretrieve(path,'img_{}.jpg'.format(i))
