
# https://subzeroid.github.io/instagrapi/usage-guide/story.html

from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
import getpass


USERNAME = 'vicksbot2023'
PASSWORD = getpass.getpass('\nEnter Instagram Password : ')


pid = 'C0YNQhjJDyE'
# pid = input('Enter Post ID : ')
url = f'https://www.instagram.com/p/{pid}/'


cl = Client()
cl.login(USERNAME, PASSWORD)


# media_pk = cl.media_pk_from_url(url)
# media_path = cl.video_download(media_pk)


# imvickykumar999 = cl.user_info_by_username('imvickykumar999')
# hashtag = cl.hashtag_info('imvickykumar999')


# cl.video_upload_to_story(
#     media_path,
#     "Credits @imvickykumar999",

#     mentions=[StoryMention(user=imvickykumar999, x=0.49892962, y=0.703125, width=0.8333333333333334, height=0.125)],
#     links=[StoryLink(webUri='https://github.com/imvickykumar999/open.source.threads')],

#     hashtags=[StoryHashtag(hashtag=hashtag, x=0.23, y=0.32, width=0.5, height=0.22)],
#     medias=[StoryMedia(media_pk=media_pk, x=0.5, y=0.5, width=0.6, height=0.8)]
# )

# ----------------------------------------------------

mystory = cl.photo_upload_to_story('vix.bot_3216386067029122237.mp4.jpg')
print(mystory)
