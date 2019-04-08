import time
import notify2
# from topnews import topStories
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
ICON_PATH = "./News_Icon.png"

# Fetching news
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")

# newsitems = topStories()
newsitems=soup_page.findAll("item")


#D-Bus Connection
notify2.init("News Notifier")
# Ntification Object
n = notify2.Notification(
	newsitems[0].title.text, 
	newsitems[0].pubDate.text, 
	"./News_Icon.png")

n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(50000)

for newsitem in newsitems:
	n.update(newsitem.title.text, newsitem.pubDate.text)
	n.show()
	time.sleep(5)


# https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-8.php
# for news in newsitems:
#   print(news.title.text)
#   print(news.link.text)
#   print(news.pubDate.text)
#   print("-"*60)
