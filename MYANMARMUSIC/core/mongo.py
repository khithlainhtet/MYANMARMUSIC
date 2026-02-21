# Copyright (c) 2026 khithlainhtet <khithlainhtet>
# Location: myanmar,pyin oo lwin

# All rights reserved.

# This code is the intellectual property of khithlainhtet.
# You are not allowed to copy, modify, redistribute, or use this
# code for commercial or personal projects without explicit permission.

# Allowed:
# - Forking for personal learning
# - Submitting improvements via pull requests

# Not Allowed:
# - Claiming this code as your own
# - Re-uploading without credit or permission
# - Selling or using commercially

# Contact for permissions:
# Email: bronaing371@gmail.com


from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Connecting to your Mongo Database...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Khithlainhtet
    LOGGER(__name__).info("Connected to your Mongo Database.")
except:
    LOGGER(__name__).error("Failed to connect to your Mongo Database.")
    exit()


# ©️ Copyright Reserved - @khithlainhtet  khithlainhtet

# ===========================================
# ©️ 2026 khithlainhtet (user @khithlainhtet)
# 🔗 GitHub : https://github.com/khithlainhtet/MYANMARMUSIC
# 📢 Telegram Channel :https://t.me/myanmarbot_music
# ===========================================


# ❤️ Love From myanmarbot_music
