import config
from DEADLYSPAM import BOT0, SUDOERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
 
hl = config.CMD_HNDLR
 
HELP_PIC = "https://telegra.ph//file/e752a752e078ea53204aa.jpg"

DEAD_HELP = "ð¥ sá´á´Êá´Ê Sá´á´á´ Bá´á´ ð¥\n\n"
 
DEAD_HELP += f"__á´á´É´á´s á´á´ á´ÉªÊá´ÊÊá´ ÉªÉ´ sá´á´Êá´Ê Êá´á´__\n\n"

DEAD_HELP += f" â§ sá´á´á´Êá´á´ ð²ð¼ð³ð â§\n\n"

DEAD_HELP += f" `!ping` - to check ping\n `!alive` - to check bot alive/version (only main userbot will reply)\n !`restart` - to restart all spam bots \n `!addecho` - to addecho \n `!rmecho` - To remove Echo \n `!addsudo` - To add sudo user using spam bot \n `!delsudo` to delete someone from sudolist\n\n"
 
DEAD_HELP += f" â§ ð»ð´ð°ðð´ ð²ð¼ð³ â§\n\n"

DEAD_HELP += f" `!leave` - to leave public/private channel/groups\n\n"
 
DEAD_HELP += f" â§ ðð¿ð°ð¼ ð²ð¼ð³ð â§\n\n"

DEAD_HELP += f" `!raid` - to raid\n `!replyraid` - to active reply raid\n `!dreplyraid` - to de-active reply raid\n `!spam` - this cmd use for Normal spam\n `!bigspam` - this cmd use for big spam\n `!bspam` - this cmd use for spamming on someone birthday!!\n `!delayspam` - this cmd use for delay spam\n\n"

DEAD_HELP += f" !pornspam - Éª á´¡ÉªÊÊ ê±á´É¢É¢á´ê±á´ á´á´É´'á´ á´ê±á´ á´ÊÉªê± á´á´á´á´á´É´á´ð â§\n\n"

DEAD_HELP += f"Â© @OWNER_IND_FYTERS\n"


@BOT0.on(events.NewMessage(incoming=True, pattern='/help'))
async def help(event):               
    if event.sender_id in SUDOERS:
       blaze = [[Button.url("á´Êá´É´É´á´Ê", "https://t.me/FUCKER_KIDSS"), Button.url("sá´á´á´á´Êá´", "https://t.me/CRACK_FIGHTER_ON_FIRE")]]
       await BOT0.send_file(event.chat_id, HELP_PIC, caption=DEAD_HELP, buttons=blaze) 
