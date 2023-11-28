
from mastodon import Mastodon
import requests, json

client_id = input('\nEnter client_id Key : ')
client_secret = input('\nEnter client_secret Key : ')
access_token = input('\nEnter access_token Key : ')

def mastodon_post(access_token, tweet):
    url = 'https://mastodon.social/api/v1/statuses'
    auth = {'Authorization': f'Bearer {access_token}'}

    params = {'status': tweet}
    r = requests.post(url, data=params, headers=auth)

    res = json.loads(r.text)
    print('\n', res['url'])

mastodon = Mastodon(
    client_id = client_id,
    client_secret = client_secret,
    access_token = access_token,
    api_base_url = 'https://mastodon.social'
)

media_post = mastodon.media_post("static/1701169387.4632928.png", "image/png")
tweet = "Look Mom, I can update my status via Mastodon's API!"
mastodon_post(access_token, tweet + '\n' + media_post['url'])

# toot = mastodon.toot(media_post['url'])
# print(toot['url'])
