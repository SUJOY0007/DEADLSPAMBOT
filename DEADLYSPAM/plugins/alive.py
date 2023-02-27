import config
from DEADLYSPAM import BOT0, deadlyversion, SUDOERS
from telethon import events, version, Button
from telethon.tl.custom import button

PIC = config.ALIVE_PIC

if config.ALIVE_PIC:
    DEADLY_PIC = PIC
else:
    DEADLY_PIC = "https://telegra.ph//file/e752a752e078ea53204aa.jpg"

hl = config.CMD_HNDLR


DEADLY = "✯ 🥵𝘽𝙃𝙊𝙎𝘿𝙄𝙒𝘼𝙇𝘼 𝙎𝙋𝘼𝙈 𝘽𝙊𝙏 𝙁𝙄𝙍𝙀🥵 ✯\n\n"
DEADLY += f"═══════════════════\n"
DEADLY += f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `4.0.0`\n"
DEADLY += f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"
DEADLY += f"• **sᴘᴀʀᴋʏʙᴏᴛ ᴠᴇʀsᴏɴ**  : `{deadlyversion}`\n"
DEADLY += f"═══════════════════\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("ᴄʜᴀɴɴᴇʟ", "https://t.me/FUCKER_KIDSS"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/CRACK_FIGHTER_ON_FIRE")], [Button.url("• ʀᴇᴘᴏ •", "https://te.legra.ph/file/db7c6b18567b5e81165ad.mp4")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=SPARKY, buttons=Blaze) 
  else:
      await event.reply("**𝐃𝐄𝐏𝐋𝐎𝐘 𝐘𝐎𝐔𝐑 𝐋𝐀𝐔𝐍𝐃 𝐒𝐏𝐀𝐌𝐁𝐎𝐓!**") 
