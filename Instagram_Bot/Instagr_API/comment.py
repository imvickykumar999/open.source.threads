
# https://subzeroid.github.io/instagrapi/usage-guide/comment.html

from instagrapi import Client
from pprint import pprint
import getpass, json


USERNAME = 'vix.bot'
PASSWORD = getpass.getpass('\nEnter Instagram Password : ')


pid = 'C0O3JPZJ3UN'
# pid = input('Enter Post ID : ')
url = f'https://www.instagram.com/p/{pid}/'


cl = Client()
cl.login(USERNAME, PASSWORD)


media_pk = cl.media_pk_from_url(url)
media_id = cl.media_id(media_pk)


comment = cl.media_comment(
    media_id, 
    f"MediaID = (PostID_UserID) : {media_id}"
) # do comment


cl.comment_like(comment.pk) # like comment
# cl.comment_unlike(comment.pk) # like comment


reply = cl.media_comment(
    media_id, 
    f"Replying Comment ID : {comment.pk}", 
    replied_to_comment_id=comment.pk
) # do reply


cl.comment_like(reply.pk) # unlike reply
# cl.comment_unlike(reply.pk) # unlike reply


(comments_part, next_min_id) = cl.media_comments_chunk(media_id, 100)
bulk_delete = []


for i in comments_part:
    i = json.loads(i.json())
    pprint(i['pk'], i['text']) # show comments
    bulk_delete.append(i['pk'])


bulk_delete.pop(comment.pk) # don't delete comment
bulk_delete.pop(reply.pk) # don't delete reply
cl.comment_bulk_delete(media_id, bulk_delete) # delete appended


'''
    raise RateLimitError(**last_json)
instagrapi.exceptions.RateLimitError: Please wait a few minutes before you try again.
'''
