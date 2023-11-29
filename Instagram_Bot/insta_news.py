
import requests, random

news_api = input('\nEnter news_api Key : ')

source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
source = random.choice(source)

print('\n', source)
gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={news_api}'

req = requests.get(gets)
box = req.json()['articles']
cap = []

for j, i in enumerate(box):
    if i['description'] == None:
        i['description'] = 'Read More'

    tweet = f'''
({j+1}). {i['title']}

{i['description']}

{i['url']}
'''
    cap.append(tweet)

print('\n'.join(cap))
