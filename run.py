import requests
from personalToken import api_key, user_token
api_key = api_key(); user_token = user_token()

url = f"https://api.trello.com/1/members/me/boards?key={api_key}&token={user_token}"


response = requests.request("GET", url)

print(response.text)

