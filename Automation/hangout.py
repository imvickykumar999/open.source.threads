
from json import dumps
import requests, random
from httplib2 import Http

def main(url, photo, title, description, link):
    bot_message = {
        'text' : title,
          "cards": [
            {
              "sections": [
                {
                  "widgets": [
                    {
                      "textParagraph": {
                        "text": f"{description}"
                      }
                    }
                  ]
                }
              ]
            },
            {
          "sections": [
            {
              "widgets": [
                {
                  "image": {
                    "imageUrl": f"{photo}",
                    "onClick": {
                      "openLink": {
                        "url": f"{link}"
                      }
                    }
                  }
                }
              ]
            }
          ]
        }
      ]
    }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )
    return response

if __name__ == '__main__':
  url = 'https://chat.googleapis.com/v1/spaces/AAAAhFoSnVc/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=-lk4YKNyDNIUuLBlgGAtkryt9sJ5G2FzgAD-NGX_NBk'
  news_api = 'b3b11f4b5a46426b8ffab29eae5ca2eb'

  source = ['bbc-news', 'cnn', 'the-verge', 'time', 'the-wall-street-journal']
  source = random.choice(source)
  gets = f'https://newsapi.org/v1/articles?source={source}&sortBy=top&apiKey={news_api}'

  req = requests.get(gets)
  box = req.json()['articles']

  for j, i in enumerate(box):
    if i['description'] == None:
        i['description'] = 'Read More'

    title = f"{j+1}). {i['title']}"
    photo = i['urlToImage']
    description = i['description']
    link = i['url']
    main(url, photo, title, description, link)

