
from instagrapi import Client
cl = Client()

USERNAME = input('\nEnter Username : ')
PASSWORD = input('\nEnter Password : ')
cl.login(USERNAME, PASSWORD)

path = 'images/chipi.mp4'
caption = 'Chipi Chipi Chapa Chapa ...'
thumbnail = 'images/chipi.jpg'

cl.video_upload(
    path = path, 
    caption = caption, 
    thumbnail = thumbnail
)

print(f'\nUploaded on https://www.instagram.com/{USERNAME}/reels/')
