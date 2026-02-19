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


import io

from gtts import gTTS
from pyrogram import filters

from MYANMARMUSIC import app


@app.on_message(filters.command("tts"))
async def text_to_speech(client, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "Please provide some text to convert to speech."
        )

    text = message.text.split(None, 1)[1]
    tts = gTTS(text, lang="hi")
    audio_data = io.BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    audio_file = io.BytesIO(audio_data.read())
    audio_file.name = "audio.mp3"
    await message.reply_audio(audio_file)


__HELP__ = """
**ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ**

ᴜsᴇ ᴛʜᴇ `/tts` ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ ᴛᴇxᴛ ɪɴᴛᴏ sᴘᴇᴇᴄʜ.

- `/tts <ᴛᴇxᴛ>`: ᴄᴏɴᴠᴇʀᴛs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ ᴛᴏ sᴘᴇᴇᴄʜ ɪɴ ʜɪɴᴅɪ.

**ᴇxᴀᴍᴘʟᴇ:**
- `/tts Radhe Radhe`

**ɴᴏᴛᴇ:**
ᴍᴀᴋᴇ sᴜʀᴇ ᴛᴏ ᴘʀᴏᴠɪᴅᴇ sᴏᴍᴇ ᴛᴇxᴛ ᴀғᴛᴇʀ ᴛʜᴇ `/tts` ᴄᴏᴍᴍᴀɴᴅ.
"""

__MODULE__ = "Tᴛs"


# ©️ Copyright Reserved - @khithlainhtet  khithlainhtet

# ===========================================
# ©️ 2026 khithlainhtet (user @khithlainhtet)
# 🔗 GitHub : https://github.com/khithlainhtet/MYANMARMUSIC
# 📢 Telegram Channel :https://t.me/myanmarbot_music
# ===========================================


# ❤️ Love From myanmarbot_music
