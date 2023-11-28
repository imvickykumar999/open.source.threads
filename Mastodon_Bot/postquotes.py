
import json, getpass, random, time
import requests, openai, urllib.request

def mastodon_post(
        access_token, 
        tweet = "Look Mom, I can update my status via Mastodon's API!"
    ):
    
    url = 'https://mastodon.social/api/v1/statuses'
    auth = {'Authorization': f'Bearer {access_token}'}

    params = {'status': tweet}
    r = requests.post(url, data=params, headers=auth)

    res = json.loads(r.text)
    print(res['url'])

def generate_image(API_Key):
    openai.api_key = API_Key

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{
                "role": "user", 
                "content": "Trending Minecraft Games"
        }])
    topics = completion.choices[0].message.content

    try:
        topic = random.choice(topics.split('\n')[2:-2]).split('. ')[1]
    except Exception as e:
        print('\nTry again ... ', e)

    image_resp = openai.Image.create(prompt=topic, n=1, size="512x512")
    my_image = image_resp['data'][0]['url']

    file = f'static/{time.time()}.png'
    urllib.request.urlretrieve(my_image, file)
    return topic + '\n' + my_image

API_Key = getpass.getpass('\nEnter OpenAI API Key : ')
access_token = getpass.getpass('Enter Mastodon API Key : ')

print('\nProcessing ...\n')
generated_image = generate_image(API_Key)
mastodon_post(access_token, generated_image)
