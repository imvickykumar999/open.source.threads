
# https://subzeroid.github.io/instagrapi/usage-guide/comment.html

from instagrapi import Client

USERNAME = 'vix.bot'
PASSWORD = input('\nEnter Instagram Password : ')

pid = 'C0O3JPZJ3UN'
# pid = input('Enter Post ID : ')

cl = Client()
cl.login(USERNAME, PASSWORD)

media_pk = cl.media_pk_from_url(f'https://www.instagram.com/p/{pid}/')
media_id = cl.media_id(media_pk)

comment = cl.media_comment(
    media_id, 
    f"{media_id}"
)
cl.comment_like(comment.pk)

print('\nComment Dictionary\n')
print(comment.dict())

reply = cl.media_comment(
    media_id, 
    f"{comment.dict()}", 
    replied_to_comment_id=comment.pk
)
cl.comment_like(reply.pk)

print('\nReply Dictionary\n')
print(reply.dict())
