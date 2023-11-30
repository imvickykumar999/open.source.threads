
# https://subzeroid.github.io/instagrapi/usage-guide/comment.html

from instagrapi import Client
from pprint import pprint
import getpass, json


USERNAME = 'vix.bot'
PASSWORD = getpass.getpass('\nEnter Instagram Password : ')


# pid = 'C0O3JPZJ3UN'
pid = input('Enter Post ID : ')
url = f'https://www.instagram.com/p/{pid}/'


cl = Client()
cl.login(USERNAME, PASSWORD)


media_pk = cl.media_pk_from_url(url)
media_id = cl.media_id(media_pk)


comment = cl.media_comment(
    media_id, 
    f"MediaID = (PostID_UserID) : {media_id}"
)

cl.comment_like(comment.pk)
# cl.comment_unlike(comment.pk)


reply = cl.media_comment(
    media_id, 
    f"Replying Comment ID : {comment.pk}", 
    replied_to_comment_id=comment.pk
)

cl.comment_like(reply.pk)
# cl.comment_unlike(reply.pk)


(comments_part, next_min_id) = cl.media_comments_chunk(media_id, 100)
bulk_delete = []


for i in comments_part:
    i = json.loads(i.json())
    pprint(i['pk'], i['text'])
    bulk_delete.append(i['pk'])


bulk_delete.pop(comment.pk)
bulk_delete.pop(reply.pk)
cl.comment_bulk_delete(media_id, bulk_delete)


'''
    raise RateLimitError(**last_json)
instagrapi.exceptions.RateLimitError: Please wait a few minutes before you try again.

API rate limit
--------------

Every third-party application connected to Instagram's API 
has a restriction on how many times it may access its data. 

Instagram has recently decreased its API restriction from 
5,000 to 200 requests per hour.
'''
