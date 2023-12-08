from pyrogram import filters
from client import app
from dotenv import load_dotenv
import os

load_dotenv()

user_ids = os.getenv('USER_IDS')
group_ids = os.getenv('GROUP_IDS')

if not (user_ids or group_ids):
    raise Exception('Must specify user_ids and group_ids')


@app.on_message(
    filters.chat(list(map(int, group_ids.split(',')))) &
    filters.user(list(map(int, user_ids.split(','))))
)
async def react(_, message):
    try:
        await message.react(emoji='💩')
    except Exception as e:
        print(e)


app.run()