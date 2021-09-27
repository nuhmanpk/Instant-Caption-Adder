import os
from pyromod import listen
from pyrogram import Client, filters
from pyrogram.types import Message, User

bughunter0 = Client(
    "BotNameHere",
     bot_token = os.environ["BOT_TOKEN"],
     api_id = int(os.environ["API_ID"]),
     api_hash = os.environ["API_HASH"]
)

CAPTION = os.environ.get("CAPTION", None)

# Better to add caption through config vars / app.json


@bughunter0.on_message(filters.media)
async def caption(bot, message):
    chat_id = message.chat.id
    if CAPTION:
        caption = CAPTION
    else:
        caption = await get_caption(message)
        return if caption is True else pass
    await message.copy(chat_id=chatid, caption=caption)


async def get_caption(message):
    caption = await bot.ask("Send a caption for the media")
    if not caption.text:
        await caption.reply("No caption found", quote=True)
        return await get_caption(message)
    if caption.text.startswith("/cancel"):
        await caption.reply("Process cancelled", quote=True)
        return True
    else:
        return caption.text


bughunter0.run()
