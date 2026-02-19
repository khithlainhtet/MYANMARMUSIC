# Copyright (c) 2026 khithlainhtet <khithlainhtet>
# Location: myanmar,pyin oo lwin
#
# All rights reserved.
#
# This code is the intellectual property of khithlainhtet.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.
#
# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests
#
# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially
#
# Contact for permissions:
# Email: bronaing371@gmail.com


import re

from pymongo import MongoClient
from pyrogram import filters
from pyrogram.types import Message

from MYANMARMUSIC import app

mongo_url_pattern = re.compile(r"mongodb(?:\+srv)?:\/\/[^\s]+")


@app.on_message(filters.command("mongochk"))
async def mongo_command(client, message: Message):
    if len(message.command) < 2:
        await message.reply(
            "ᴘʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴍᴏɴɢᴏᴅʙ ᴜʀʟ ᴀғᴛᴇʀ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ  /mongochk your_mongodb_url"
        )
        return

    mongo_url = message.command[1]
    if re.match(mongo_url_pattern, mongo_url):
        try:
            # Attempt to connect to the MongoDB instance
            client = MongoClient(mongo_url, serverSelectionTimeoutMS=5000)
            client.server_info()  # Will cause an exception if connection fails
            await message.reply("ᴍᴏɴɢᴏᴅʙ ᴜʀʟ ɪs ᴠᴀʟɪᴅ ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛɪᴏɴ sᴜᴄᴇssғᴜʟ ✅")
        except Exception as e:
            await message.reply(f"ғᴀɪʟᴇᴅ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ᴍᴏɴɢᴏᴅʙ: {e}")
    else:
        await message.reply("ᴜᴘs! ʏᴏᴜʀ ᴍᴏɴɢᴏᴅʙ ғᴏʀᴍᴀᴛ ɪs ɪɴᴠᴀʟɪᴅ")


__MODULE__ = "Mᴏɴɢᴏᴅʙ"
__HELP__ = """
**ᴍᴏɴɢᴏᴅʙ ᴄʜᴇᴄᴋᴇʀ:**

• `/mongochk [mongo_url]`: Cʜᴇᴄᴋs ᴛʜᴇ ᴠᴀʟɪᴅɪᴛʏ ᴏғ ᴀ ᴍᴏɴɢᴏᴅʙ URL ᴀɴᴅ ᴄᴏɴɴᴇᴄᴛɪᴏɴ ᴛᴏ ᴛʜᴇ ᴍᴏɴɢᴏᴅʙ ɪɴsᴛᴀɴᴄᴇ.
"""


# ©️ Copyright Reserved - @khithlainhtet  khithlainhtet

# ===========================================
# ©️ 2026 khithlainhtet (user @khithlainhtet)
# 🔗 GitHub : https://github.com/khithlainhtet/MYANMARMUSIC
# 📢 Telegram Channel :https://t.me/myanmarbot_music
# ===========================================


# ❤️ Love From myanmarbot_music
