import os
from pyromod import listen
from pyrogram import Client, filters


bughunter0 = Client(
    "Instant-Caption-Adder",
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
        caption = await get_caption(bot, message)
        if caption is True:
            return
        await message.copy(chat_id=chat_id, caption=caption, reply_to_message_id=message.message_id)


async def get_caption(bot, message):
    caption = await bot.ask(message.chat.id, "Send a caption for the media or send /cancel for cancelling this process")
    if not caption.text:
        await caption.reply("No caption found", quote=True)
        return await get_caption(bot, message)
    if caption.text.startswith("/cancel"):
        await caption.reply("Process cancelled", quote=True)
        return True
    else:
        return caption.text


bughunter0.run()
