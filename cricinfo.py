from urllib2 import urlopen
from bs4 import BeautifulSoup
import time
import os
while True:
    url = 'http://www.espncricinfo.com/ci/engine/match/index.html'
    data = urlopen(url)
    soup = BeautifulSoup(data, 'html.parser')
    result = soup.find('title')
    innings1 = soup.find("div", {"class": "innings-info-1"})
    innings2 = soup.find("div", {"class": "innings-info-2"})
    print (innings1.text)
    print (innings2.text)
    time.sleep(5)
    clear=lambda :os.system('cls')
    clear()
    #print(soup.div['innings-info-2'])
#print(result.get_text())