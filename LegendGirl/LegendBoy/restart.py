import os
import sys

from telethon import events

from .. import *

SMEX_USERS = []
for x in SUDO_USERS:
    SMEX_USERS.append(x)


@bot.on(events.NewMessage(pattern="/restart"))
@bot2.on(events.NewMessage(pattern="/restart"))
@bot3.on(events.NewMessage(pattern="/restart"))
@bot4.on(events.NewMessage(pattern="/restart"))
@bot5.on(events.NewMessage(pattern="/restart"))
@bot6.on(events.NewMessage(pattern="/restart"))
@bot7.on(events.NewMessage(pattern="/restart"))
@bot8.on(events.NewMessage(pattern="/restart"))
@bot9.on(events.NewMessage(pattern="/restart"))
@bot10.on(events.NewMessage(pattern="/restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = " 🤖𝐑𝐄𝐒𝐓𝐀𝐑𝐓𝐄𝐃🤖\n🔰𝐙𝐀𝐑𝐀 𝟐𝐌𝐈𝐍𝐓 𝐑𝐔𝐊𝐊 𝐁𝐇𝐀𝐈 𝐑𝐄𝐃𝐁𝐔𝐋𝐋 𝐏𝐈 𝐑𝐀𝐇 𝐇𝐔...."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await bot.disconnect()
        except Exception:
            pass
        try:
            await bot2.disconnect()
        except Exception:
            pass
        try:
            await bot3.disconnect()
        except Exception:
            pass
        try:
            await bot4.disconnect()
        except Exception:
            pass
        try:
            await bot5.disconnect()
        except Exception:
            pass
        try:
            await bot6.disconnect()
        except Exception:
            pass
        try:
            await bot7.disconnect()
        except Exception:
            pass
        try:
            await bot8.disconnect()
        except Exception:
            pass
        try:
            await bot9.disconnect()
        except Exception:
            pass
        try:
            await bot10.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
