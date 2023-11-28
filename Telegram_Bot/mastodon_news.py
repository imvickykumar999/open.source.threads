
from mastodon import Mastodon
import requests, random

news_api = input('\nEnter news_api Key : ')
client_id = input('\nEnter client_id Key : ')
client_secret = input('\nEnter client_secret Key : ')
access_token = input('\nEnter access_token Key : ')

mastodon = Mastodon(
    client_id = client_id,
    client_secret = client_secret,
    access_token = access_token,
    api_base_url = 'https://mastodon.social'
)

source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
source = random.choice(source)

print('\n', source)
gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={news_api}'

req = requests.get(gets)
box = req.json()['articles']

for i in box:
    if i['description'] == None:
        i['description'] = 'Read More'

    tweet = f'''
    ➡️ {i['title']}

    {i['description']}

    {i['url']}
    '''

    toot = mastodon.toot(tweet)
    print('\n', toot['url'])
