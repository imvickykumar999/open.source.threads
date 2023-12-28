
# https://subzeroid.github.io/instagrapi/usage-guide/media.html

from datetime import date
from instagrapi import Client

cl = Client()
d0 = date(2023, 12, 26)

today = date.today()
today = date.timetuple(today)

d1 = date(
    int(today.tm_year), 
    int(today.tm_mon), 
    int(today.tm_mday)
)
x = d1 - d0
print(x.days)

USERNAME = '**************'
PASSWORD = '**************'
cl.login(USERNAME, PASSWORD)

path = 'video.mp4'
thumbnail = 'photo.jpg'

caption = f'''
Day {x.days}
Follow me!
'''

cl.video_upload(
    path = path, 
    caption = caption, 
    thumbnail = thumbnail
)

print(f'\nUploaded on https://www.instagram.com/{USERNAME}/reels/')
