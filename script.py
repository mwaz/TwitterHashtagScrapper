'''
This will be able to scrap twitter hashtags and send them to a bot on slack	
'''
#import lib to parse urls 

import requests

'''
Import Beautiful Soup package for scrapping
'''

from bs4 import BeautifulSoup

twitter_url = 'http://github.com/mwaz'

page = requests.get(twitter_url)

soup = BeautifulSoup(page.content, 'html.parser')

twitter_trends = soup.find('ol', {'class': 'pinned-repos-list'} )

for i in twitter_trends.find_all('li', {'class': 'pinned-repo-item'}):
    for x in i.find_all('span', {'class': 'd-block position-relative'}):
        print(x.text)

    # if(i != None):
    #     print('okay')
    # else:
    #     print('nothing here')


# print(twitter_trends)
