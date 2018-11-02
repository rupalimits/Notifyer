import time
import notify2
from topnews import topStories

ICON_PATH = "Message.png"
# Fetching news
newsitems = topStories()
#D-Bus Connection
notify2.init("News Notifier")
# Ntification Object
n = notify2.Notification(, , "Message.png")
n.set_urgency(notify2.URGENCY_NORMAL)
n.set_timeout(50000)

for newsitem in newsitems:
	n.update(newsitem['title'], newsitem['description'])
	n.show()
	time.sleep(15)
