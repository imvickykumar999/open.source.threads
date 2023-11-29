
import random, time
import openai, urllib.request
from mastodon import Mastodon

def generate_image(API_Key):
    openai.api_key = API_Key

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{
                "role": "user", 
                "content": "Trending Video Games"
        }])
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

    image_resp = openai.Image.create(prompt=topic, n=1, size="512x512")
    my_image = image_resp['data'][0]['url']

    file = f'static/{time.time()}.png'
    urllib.request.urlretrieve(my_image, file)
    return topic, file

def media_link(generated_image):
    mastodon = Mastodon(
        client_id = client_id,
        client_secret = client_secret,
        access_token = access_token,
        api_base_url = 'https://mastodon.social'
    )

    media_post = mastodon.media_post(generated_image[1], "image/png")
    toot = mastodon.toot(generated_image[0] + '\n' + media_post['url'])
    print(toot['url'])

if __name__ == '__main__':
    openai_api = input('\nEnter openai_api Key : ')
    client_id = input('\nEnter client_id Key : ')
    client_secret = input('\nEnter client_secret Key : ')
    access_token = input('\nEnter access_token Key : ')

    print('\nProcessing ...\n')
    generated_image = generate_image(openai_api)

    media_link(generated_image)
    # mastodon_post(access_token)
