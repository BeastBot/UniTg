""".alive Plugin for @UniBorg"""
import asyncio
import io
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


DEFAULTUSER = Config.ALIVE_NAME
    
@borg.on(admin_cmd(pattern=r"\.(.*)", outgoing=True, allow_sudo=True))
async def _(event):
           input_str = event.pattern_match.group(1)
           if input_str == "alive":
                 await event.reply(""
                     "Me Iz Running \n\n"
                     "XD"
                     "")
                
                 await event.delete()
