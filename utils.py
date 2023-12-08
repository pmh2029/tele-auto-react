from pyrogram import filters
from client import app

@app.on_message(filters.text)
async def echo(_, message):
    print(message)

app.run()