
# https://www.pythonanywhere.com/user/autouploadoninsta/files/var/log/autouploadoninsta.pythonanywhere.com.error.log
# instagrapi.exceptions.ProxyAddressIsBlocked: Instagram has blocked your IP address, use a quality proxy provider (not free, not shared)

# https://stackoverflow.com/a/67028932/11493297
# https://stackoverflow.com/a/68746288/11493297

from PIL import Image
from instagrapi import Client

def resize_me(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    new_image = image.resize((1080, 1080))
    new_image.save(image_path)

resize_me("images/1701157530.2756922.jpg")
resize_me("images/1701104587.4618087.jpg")

bot = Client()
bot.login('vix.bot', 'Hellovix999@')

album_path = ["images/1701157530.2756922.jpg", "images/1701104587.4618087.jpg"]
text =  "Multiple Uploads"

# bot.photo_upload("images/1701157530.2756922.jpg" , "hello this is a test from instagrapi")
bot.album_upload(
    album_path,
    caption = text
)
