
# https://platform.openai.com/account/api-keys

'''
openai.error.RateLimitError: Rate limit exceeded for images per minute 
in organization org-PL2jxjAPPRDL0KEqREmSg8Bw. 

Limit: 5/1min. 
Current: 8/1min. 

Please visit https://help.openai.com/en/articles/6696591 
to learn how to increase your rate limit.
'''

from instagrapi import Client
import requests, random
from PIL import Image
import openai, os

try: os.mkdir('openai')
except: pass

user = 'vicksbot2023'
passwd = input('\nEnter Instagram Password : ')

API_Key = input('\nEnter OpenAI API Key : ')
openai.api_key = API_Key

print('\nUploading ...')
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
                messages=[{"role": "user", 
                           "content": "List of Most Happiest Bird Paintings"}])

topics = completion.choices[0].message.content

try:
    topic = random.choice(topics.split('\n')[2:-2]).split('. ')[1]
except:
    topics = '''1. Minecraft 1.17: Caves and Cliffs Update - This upcoming update to Minecraft is highly anticipated by players. It introduces new underground features, biomes, mobs, and blocks, enhancing the exploration and mining experience.

2. Minecraft Dungeons - This spin-off game combines the Minecraft universe with action-packed dungeon crawling gameplay. Players can team up with friends to defeat mobs and bosses, collect gear, and explore various levels.

3. Minecraft Earth - A mobile augmented reality game that allows players to build and explore Minecraft creations in the real world. It incorporates real-world locations and encourages collaboration with other players.

4. Minecraft: Story Mode - Developed by Telltale Games, this episodic adventure game takes players on an interactive story-driven journey set in the Minecraft universe. Players make choices that affect the outcome and can shape the narrative.

5. Minecraft Education Edition - Designed for educational purposes, this version of Minecraft provides a platform for teachers to engage students in learning activities. It offers various features, including lesson plans, collaborative building, and coding exercises.

6. Minecraft Skyblock - This popular Minecraft game mode challenges players to survive on a floating island with limited resources. They must use their creativity and problem-solving skills to expand their island, gather resources, and survive.

7. Minecraft Bed Wars - A multiplayer game mode where players compete to destroy each other's beds while defending their own. It requires strategic planning, teamwork, and quick reflexes to outsmart opponents and emerge victorious.

8. Minecraft Survival Games - Inspired by the "Hunger Games" series, this game mode throws players into a map where they must scavenge for weapons and armor, eliminate opponents, and be the last one standing.

9. Minecraft Hypixel - Hypixel is a popular Minecraft server that offers a wide range of custom mini-games, including Bed Wars, Skyblock, and Survival Games. It attracts a large player base due to its diverse and engaging gameplay options.

10. Minecraft Creative Mode - Although not new, Minecraft's Creative Mode remains a favorite among players. It allows them unlimited resources, the ability to fly, and the freedom to create and build whatever they imagine in the game.
'''
    topic = random.choice(topics.split('\n')[2:-2]).split('. ')[1]

print(topic)

n=5
image_resp = openai.Image.create(prompt=topic + ' Make it more Happier.', n=n, size="512x512")

def make_square(im, min_size=256, fill_color=(255,255,255,0)):
    img = Image.open(im)
    x, y = img.size

    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)

    new_im = new_im.convert("RGB")
    new_im.paste(img, (int((size - x) / 2), int((size - y) / 2)))
    new_im.save(im)
    
for i in range(n):
    img = list(image_resp['data'][i].values())[0]
    r = requests.get(img, allow_redirects=True)

    path = f'openai/{i}.jpg'
    open(path, 'wb').write(r.content)
    make_square(path)

bot = Client()
bot.login(username = user, password = passwd)
album_path = ['openai/'+i for i in os.listdir('openai')]

bot.album_upload(
    album_path,
    caption = topics
)
