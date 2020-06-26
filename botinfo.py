import sys
import asyncio
from telethon import events,functions, __version__
from uniborg.util import admin_cmd

@borg.on(events.NewMessage(pattern="mybot ?(.*)",outgoing=True))
async def _(event):
	help_string = """@UniBorg ( **Custom Built By** @ahrned ) \n**Verified Account**: ✅
Python {}
Telethon {}
 
**Custom Built Fork**: https://github.com/faquario/pepeborg""".format(
        sys.version,
        __version__
    )
	await event.delete()
	await event.reply(help_string+"\n\n\n"+"[ . . . . . . . . . . . . . . . . . . . ](https://telegra.ph/file/f315d3098b86381e03bd3.mp4)", link_preview=True)
