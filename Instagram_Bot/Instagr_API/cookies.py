
import requests
client = requests.get("https://www.instagram.com/")
print(client.cookies.get_dict())
