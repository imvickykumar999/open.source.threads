
# https://github.com/duxovni/imagebot
# https://dev.to/bitsrfr/getting-started-with-the-mastodon-api-41jj

import requests
import json, getpass

access_token = getpass.getpass('Enter Access Token : ')
url = 'https://mastodon.social/api/v1/statuses'

auth = {'Authorization': f'Bearer {access_token}'}
params = {'status': 'Hello World!'}

r = requests.post(url, data=params, headers=auth)
# https://mastodon.social/@imvickykumar999

res = json.loads(r.text)
print(res['url'])
