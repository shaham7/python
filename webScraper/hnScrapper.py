import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titleline > a')
subtexts = soup.select('.subtext')

def sort_by_votes(hnlist):
    return sorted(hnlist, key= lambda k:k['votes'])

def create_custom_hm(link, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = link[idx].getText()
        href = link[idx].get('href',None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title':title, 'link':href, 'votes':points})
    return sort_by_votes(hn)
#more mode left
pprint.pprint(create_custom_hm(links,subtexts))
