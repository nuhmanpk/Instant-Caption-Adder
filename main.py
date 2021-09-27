import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "BotNameHere",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

CAPTION=""" Add Your Caption Here """

# Better to add caption through config vars / app.json


@bughunter0.on_message(filters.media)
async def caption(bot,message):
	chatid=message.chat.id
	await message.copy(chat_id=chatid,caption=CAPTION)
	
bughunter0.run()
