""".alive Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "`Chal raha hu Bsdk...\nAb Hoga Tera Account Ban\n\nTelethon version: 1.10.10\nPython: 3.7.5\nUser: @kirito6969\nDatabase Status: Telegram Databases functioning normally!`"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
