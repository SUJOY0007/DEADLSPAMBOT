import os
import sys
import config
from datetime import datetime
from DEADLYSPAM import  BOT0, BOT1, BOT2, BOT3, BOT4, BOT5, BOT6, BOT7, BOT8, BOT9, SUDOERS
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events
hl = config.CMD_HNDLR

@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@BOT9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(event):
    if event.sender_id in SUDOERS:
        start = datetime.now()
        text = await event.reply(f"» 𝗭𝗜𝗡𝗗𝗔 𝗛𝗨!", parse_mode=None, link_preview=None)
        end = datetime.now()
        result = (end - start).microseconds / 1000
        await text.edit(f"» 🎉 𝗕𝗛𝗢𝗦𝗗𝗜𝗪𝗔𝗟𝗔 ✘𝗦𝗣𝗔𝗠 🤖!
 😈𝙍𝙀𝘼𝘿𝙔 𝙁𝙊𝙍 𝙎𝙀𝙈𝙓🤧 🔥\n\n💫 ᴘᴏɴɢ: {result} ms🥀`")
