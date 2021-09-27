import os
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "BotNameHere",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

@bughunter0.on_message(filters.forwarded)
async def forward(bot,message):
	await message.delete()

	
bughunter0.run()