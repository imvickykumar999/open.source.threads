
import requests, random, os, json
from instagrapi import Client
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image

def fetch_news(news_api):
    source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
    source = random.choice(source)
    print('\n', source)
    gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={news_api}'

    req = requests.get(gets)
    box = req.json()['articles']
    return box, source

def make_square(im, j, min_size=256, fill_color=(255,255,255,0)):
    img = Image.open(im)
    x, y = img.size

    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)

    new_im = new_im.convert("RGB")
    new_im.paste(img, (int((size - x) / 2), int((size - y) / 2)))

    I1 = ImageDraw.Draw(new_im)
    myFont = ImageFont.truetype("arial.ttf", 30)

    I1.text((15, 15), f'[ {j+1} ]', font=myFont, fill=(0, 0, 0))
    new_im.save(im)

def upload_news(user, passwd):
    try:
        news_api = '********************************'
        box, source = fetch_news(news_api)

    except Exception as e:
        print(e)
        news_api = '********************************'
        box, source = fetch_news(news_api)

    cap = []
    for j, i in enumerate(box):
        tweet = f'({j+1}). {i["title"]}\n'
        cap.append(tweet)
        img = i['urlToImage']
        r = requests.get(img, allow_redirects=True)

        path = f'images/{j}.jpg'
        open(path, 'wb').write(r.content)
        make_square(path, j)

    bot = Client()
    bot.login(username = user, password = passwd)
    album_path = ['images/'+i for i in os.listdir('images')]

    text = f'Read More:\n https://imvickykumar999.pythonanywhere.com/news/{source}\n\n'
    post_url = bot.album_upload(
        album_path,
        caption = text + '\n'.join(cap)
    )
    media_id = json.loads(post_url.json())['id']

    comment = bot.media_comment(
        media_id, 
        f"MediaID = (PostID_UserID) : {media_id}"
    )
    bot.comment_like(comment.pk)

    reply = bot.media_comment(
        media_id, 
        f"Comment ID : {comment.pk}", 
        replied_to_comment_id=comment.pk
    )
    bot.comment_like(reply.pk)

try: upload_news('**********', '**********')
except Exception as e: print(e)
