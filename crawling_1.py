import bs4
import urllib.request as url

http = url.urlopen("https://www.flipkart.com/search?q=macbook&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7&as-pos=1&as-type=RECENT&suggestionId=macbook&requestId=72ce3474-78f3-467e-a170-1f4539dfe89f&as-searchtext=macbook")
#print(http)

page = bs4.BeautifulSoup(http,'lxml')
div = page.find_all('div',class_='_3wU53n')
'''
for item in div:
    print(item.text)
'''

prices = page.find_all('div',class_='_1vC4OE _2rQ-NK')

'''
for price in prices:
    print(price.text)
'''
for i in range(len(div)):
    print(div[i].text)
    print(prices[i].text)
    print("########################")
