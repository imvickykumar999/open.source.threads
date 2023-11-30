
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


'''pk explained.
>>> print(comment.dict())

{
    'pk': '18000995948258042', # this unique for specific comment or reply

    'text': '2986078510956945297_51752007080', # this is f"{media_id}" as text, means before _ "2986..." is media_id part of, and after _ "5175..." is user_id who commented.
    
    'user': {
        'pk': '51752007080', # this user_id, who commented.

        'username': 'vix.bot', 
        'full_name': 'Home Automation Kit', 
        'profile_pic_url': HttpUrl('https://instagram.fdel5-2.fna.fbcdn.net/v/t51.2885-19/404613653_1369210980350061_1861343944569643401_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fdel5-2.fna.fbcdn.net&_nc_cat=109&_nc_ohc=8Zbg3VEiEy0AX-TY1gI&edm=ABQSlwABAAAA&ccb=7-5&oh=00_AfCPwYqBuziuth-GWRCh00iAkSNaeWBX_67298TFwNo3Ug&oe=656DD182&_nc_sid=9985a1', ), 
        'profile_pic_url_hd': None, 
        'is_private': False, 
        'stories': []
    }, 
    'created_at_utc': datetime.datetime(2023, 11, 30, 10, 50, 3, tzinfo=datetime.timezone.utc), 
    'content_type': 'comment', 
    'status': 'Active', 
    'has_liked': None, 
    'like_count': None
}
'''
