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


import random
from pyrogram import Client, filters
from pyrogram.types import Message
from MYANMARMUSIC import app
import asyncio

Love = [
     "🌟 <b>မင်းရဲ့အပြုံးက လောကကြီးကို အလှဆင်ပေးနိုင်တယ်ဆိုတာ သိရဲ့လား?</b> ဘယ်လောက်ပဲ ပင်ပန်းပါစေ မင်းရဲ့အပြုံးလေးကိုတော့ အပျောက်မခံပါနဲ့။ ဒီနေ့မှာ အကောင်းဆုံးတွေပဲ ဖြစ်လာမှာပါ {mention}",
    
    "🌈 <b>မိုးတိမ်တွေ ကုန်လွန်သွားရင် သာယာတဲ့ မိုးကုတ်စက်ဝိုင်းကြီး ပေါ်လာမှာပါ။</b> မင်းရဲ့ ဘဝမှာလည်း အခက်အခဲတွေ ရှိနေရင်တောင် အဲ့ဒါတွေက မင်းကို ပိုတောက်ပြောင်စေမယ့် သင်ခန်းစာတွေပါပဲ။ အားတင်းထားပါ {mention}",
    
    "✨ <b>မင်းဟာ ဒီကမ္ဘာပေါ်မှာ တစ်ယောက်တည်းပဲရှိတဲ့ အဖိုးတန်ရတနာလေးပါ။</b> ဘယ်သူနဲ့မှ နှိင်းယှဉ်စရာမလိုအောင် မင်းရဲ့ ကိုယ်ပိုင်အရည်အချင်းတွေက တောက်ပနေပါတယ်။ ကိုယ့်ကိုယ်ကိုယ် ချစ်ဖို မမေ့နဲ့နော် {mention}",
    
    "🌸 <b>ပန်းလေးတွေဟာ သူတိုပွင့်ရမယ့် အချိန်ကျရင် အလှဆုံး ပွင့်လန်းလာကြတာပါ။</b> မင်းရဲ့ အောင်မြင်မှုတွေကလည်း လမ်းခုလတ်မှာ ရောက်နေပါပြီ။ စိတ်ရှည်ရှည်နဲ့ ဆက်ကြိုးစားရင် အလှဆုံးနေ့ရက်တွေကို ပိုင်ဆိုင်ရမှာပါ {mention}",
    
    "🍀 <b>ကံကောင်းခြင်းဆိုတာ မင်းရဲ့ ကြိုးစားမှုနောက်ကို တိတ်တဆိတ် လိုက်နေတတ်ပါတယ်။</b> ဒီနေ့မှာ လုပ်ဆောင်သမျှ အရာရာတိုင်းက မင်းအတွက် ကောင်းကျိုးတွေပဲ သယ်ဆောင်လာပါစေလို ဆုတောင်းပေးပါတယ် {mention}",
    
    "🕊️ <b>စိတ်အေးချမ်းမှုဆိုတာ အပြင်လောကမှာ မဟုတ်ဘဲ မင်းရဲ့ စိတ်ထဲမှာပဲ ရှိတာပါ။</b> ဒီနေ့မှာ စိတ်ရှုပ်စရာတွေ ကြုံလာရင် မျက်စိလေးခဏမှိတ်ပြီး အသက်ဝဝရှူလိုက်ပါ။ အရာရာ အဆင်ပြေသွားမှာပါ {mention}",
    
    "☀️ <b>မနက်ခင်း နေခြည်ဟာ အသစ်တဖန် စတင်ခြင်းရဲ့ သင်္ကေတပါ။</b> မနေ့က ဘာတွေပဲ မှားခဲ့မှားခဲ့ ဒီနေ့မှာ အသစ်ကပြန်စဖို အခွင့်အရေးရှိပါတယ်။ ယုံကြည်ချက်ရှိရှိ ရှေ့ဆက်လိုက်ပါ {mention}",
    
    "🍯 <b>ချိုမြိန်တဲ့ စကားလုံးလေးတစ်ခွန်းက လူတစ်ယောက်ရဲ့ နေ့တစ်နေ့ကို ပြောင်းလဲပေးနိုင်ပါတယ်။</b> မင်းကိုလည်း အခု ဒီစာလေးဖတ်ပြီး ပျော်ရွှင်သွားစေချင်ပါတယ်။ စိတ်ချမ်းသာစရာတွေပဲ ကြုံပါစေ {mention}",
    
    "🦋 <b>လိပ်ပြာလေးတစ်ကောင် ဖြစ်လာဖို ပိုးအိမ်ထဲမှာ အကြာကြီး အားယူခဲ့ရတာပါ။</b> အခု မင်းဖြတ်သန်းနေရတဲ့ ပင်ပန်းမှုတွေက မင်းကို အင်အားကြီးတဲ့သူ ဖြစ်လာအောင် ပုံဖော်ပေးနေတာပါ {mention}",
    
    "🎁 <b>ဒီနေ့ရဲ့ စက္ကန့်တိုင်းက မင်းအတွက် လက်ဆောင်တွေပါပဲ။</b> မင်းချစ်တဲ့သူတွေနဲ့အတူ ပျော်ရွှင်စရာ အမှတ်တရလေးတွေ ဖန်တီးလိုက်ပါ။ ဘဝဆိုတာ ပျော်ရွှင်ဖိုအတွက်ပဲလေ {mention}",
    
    "💎 <b>စိန်တစ်လုံးဖြစ်ဖို ဖိအားဒဏ်တွေကို အများကြီး ခံခဲ့ရပါတယ်။</b> မင်းလည်း အခက်အခဲတွေ ကြုံနေရရင် မင်းဟာ အဖိုးတန်စိန်တစ်လုံး ဖြစ်လာတော့မယ်ဆိုတာကို သတိရလိုက်ပါ {mention}",
    
    "🎵 <b>ဘဝဆိုတာ သီချင်းတစ်ပုဒ်လိုပါပဲ။</b> နိမ့်တုံ မြင့်တုံ ရှိနေမှသာ သာယာတဲ့ တေးသံ ထွက်ပေါ်လာမှာပါ။ မင်းရဲ့ ဘဝသီချင်းလေးကို အပျော်ဆုံး သီဆိုလိုက်ပါ {mention}",
    
    "🌙 <b>ညဘက်မှာ ကြယ်လေးတွေ ရှိနေသလိုမျိုး မင်းရဲ့ အမှောင်မိုက်ဆုံး အချိန်တွေမှာလည်း အားပေးမယ့်သူတွေ ရှိနေမှာပါ။</b> မင်းဟာ တစ်ယောက်တည်း မဟုတ်ဘူးဆိုတာ အမြဲယုံကြည်ထားပါ {mention}",
    
    "🍃 <b>သစ်ရွက်လေးတွေ လေတိုက်ရာ စီးမျောသလိုမျိုး တစ်ခါတလေမှာ လောကကြီးကို လွှတ်ပေးလိုက်ပါ။</b> အတင်းအကျပ် ဆုပ်ကိုင်မထားဘဲ စိတ်အေးအေးလေး ထားကြည့်ရင် ပိုပြီး နေပျော်လာပါလိမ့်မယ် {mention}",
    
    "🚀 <b>မင်းရဲ့ ရည်မှန်းချက်တွေက ကောင်းကင်ထက် မြင့်မားနေပါစေ။</b> ကြိုးစားမှု လေယာဉ်လေးနဲ့အတူ အမြင့်ဆုံးကို ပျံသန်းနိုင်ပါစေလို ဆုတောင်းပေးလိုက်ပါတယ် {mention}"
]

@app.on_message(
    filters.command(["Love", ".Love"], prefixes=["/", "."]) & filters.private
)
async def Love_private(client: Client, message: Message):
    await message.reply_text(
        text=random.choice(Love),
    )

@app.on_message(filters.command(["Love", ".Love"]) & filters.group)
async def Love_group(client: Client, message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    
    try:
        member = await client.get_chat_member(chat_id, user_id)
    except:
        return
        
    if member.status in ["administrator", "creator"]:
        if message.reply_to_message:
            reply_msg = await message.reply(f"{message.reply_to_message.from_user.mention} {random.choice(Love)}")
        else:
            reply_msg = await message.reply(random.choice(Love))
        
        await asyncio.sleep(60)
        try:
            await reply_msg.delete()
            await message.delete()
        except:
            pass
    else:
        reply_msg = await message.reply("**🚫 This command is only for admins!**\n\n💬 Try this in my DMs instead.")
        await asyncio.sleep(10)
        try:
            await reply_msg.delete()
        except:
            pass


__MODULE__ = "𝓛𝓞𝓥𝓔"
__HELP__ = """
**�𝐨𝐯� 𝐂𝐨𝐦𝐦𝐚𝐧𝐝**

This command provides random abusive language (Love) when used in private chats. In groups, only admins can use it.

Features:
- Works in bot's DM for any user
- Only group admins/owners can use in groups
- Auto-deletes after 1 minute in groups
- Supports both /Love and .Love commands

Commands:
- /Love - Send random Love (works in DM)
- .Love - Alternative command format

Note: This command is restricted in groups to maintain decorum.
"""


# ©️ Copyright Reserved - @khithlainhtet  khithlainhtet

# ===========================================
# ©️ 2026 khithlainhtet (user @khithlainhtet)
# 🔗 GitHub : https://github.com/khithlainhtet/MYANMARMUSIC
# 📢 Telegram Channel :https://t.me/myanmarbot_music
# ===========================================


# ❤️ Love From myanmarbot_music
