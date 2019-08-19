#Movie Search Engine from IMDB
import bs4
import urllib.request as url

path = "https://www.imdb.com/find?ref_=nv_sr_fn&q="
movieName = input("Enter movie name : ")
movieName = '+'.join(movieName.split())
path = path + movieName
http = url.urlopen(path)

page = bs4.BeautifulSoup(http,'lxml')
td = page.find('td',class_='result_text')
a_tag = td.find('a')

newPath = "https://www.imdb.com/"+a_tag['href']
http = url.urlopen(newPath)
page = bs4.BeautifulSoup(http,'lxml')

movie = page.find('div',class_='title_wrapper')
movie = ' '.join(movie.text.split())
print(movie)
