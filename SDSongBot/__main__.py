#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
Hey [{}](tg://user?id={}), I'm Song Downloader Bot 🎵
😉 Just send me the song name you want to download.😋
      eg:```/song Faded```
      eg:```/song Moonlight```
      
A bot by @SanilaRanatunga
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Owner", url="https://t.me/SanilaRanatunga")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/SanilaRanatunga")],
         [InlineKeyboardButton("Torrent Downloader", url="https://t.me/torrentdownloader88_bot")],
        [InlineKeyboardButton("Source Code", url="https://github.com/sanila2007/Song-Download-Bot-")],
        [InlineKeyboardButton("Powerful Chat Bot", url="https://t.me/useful_powerful_chat_bot")]
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ MusicBot is online.")
idle()
