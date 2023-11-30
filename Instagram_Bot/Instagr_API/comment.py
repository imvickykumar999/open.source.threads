
# https://subzeroid.github.io/instagrapi/usage-guide/comment.html

from instagrapi import Client

USERNAME = 'vix.bot'
PASSWORD = input('\nEnter Instagram Password : ')
pid = 'C0O3JPZJ3UN'

cl = Client()
cl.login(USERNAME, PASSWORD)

media_pk = cl.media_pk_from_url(f'https://www.instagram.com/p/{pid}/')
media_id = cl.media_id(media_pk)

comment = cl.media_comment(media_id, f"Media ID : {media_id}")
cod = comment.dict()
print(cod.keys())
