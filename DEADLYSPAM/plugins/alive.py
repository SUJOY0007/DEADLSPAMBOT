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


DEADLY = "β― π₯΅π½ππππΏπππΌππΌ πππΌπ π½ππ πππππ₯΅ β―\n\n"
DEADLY += f"βββββββββββββββββββ\n"
DEADLY += f"β’ **α΄Κα΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `4.0.0`\n"
DEADLY += f"β’ **α΄α΄Κα΄α΄Κα΄Ι΄ α΄ α΄ΚsΙͺα΄Ι΄** : `{version.__version__}`\n"
DEADLY += f"β’ **sα΄α΄Κα΄ΚΚα΄α΄ α΄ α΄Κsα΄Ι΄**  : `{deadlyversion}`\n"
DEADLY += f"βββββββββββββββββββ\n\n"   


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%salive(?: |$)(.*)" % hl))
async def alive(event): 
  if event.sender_id in SUDOERS:
     Blaze = [[Button.url("α΄Κα΄Ι΄Ι΄α΄Κ", "https://t.me/FUCKER_KIDSS"), Button.url("sα΄α΄α΄α΄Κα΄", "https://t.me/CRACK_FIGHTER_ON_FIRE")], [Button.url("β’ Κα΄α΄α΄ β’", "https://te.legra.ph/file/db7c6b18567b5e81165ad.mp4")]]
     await BOT0.send_file(event.chat_id, DEADLY_PIC, caption=SPARKY, buttons=Blaze) 
  else:
      await event.reply("**ππππππ ππππ πππππ πππππππ!**") 
