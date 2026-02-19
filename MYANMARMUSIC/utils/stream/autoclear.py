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


import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if "vid_" not in rem or "live_" not in rem or "index_" not in rem:
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass


# ©️ Copyright Reserved - @khithlainhtet  khithlainhtet

# ===========================================
# ©️ 2026 khithlainhtet (user @khithlainhtet)
# 🔗 GitHub : https://github.com/khithlainhtet/MYANMARMUSIC
# 📢 Telegram Channel :https://t.me/myanmarbot_music
# ===========================================


# ❤️ Love From myanmarbot_music
