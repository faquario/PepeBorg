"""
responds with an expression for an incoming meow message

"""
import telethon
from telethon import TelegramClient, sync, events
import asyncio
import time
import random


my_messages=["(•‿•)", "meowww~~", " ʘ‿ʘ(✷‿✷)" ," ( ╹▽╹ )" , "meowww~~","(◍•ᴗ•◍)","(｡•̀ᴗ-)✧" ,"(✯ᴗ✯)",
"(*´ω｀*)","(◡ ω ◡)  ","  (●♡∀♡) " , "meowww~~" ," (◍•ᴗ•◍)" ," ( ◜‿◝ )♡ ",
"(｡♡‿♡｡)" , "meowww~~"," ⊂((・▽・))⊃", "(づ｡◕‿‿◕｡)づ"," V●ᴥ●V ", "(ᵔᴥᵔ)"]

@borg.on(events.NewMessage)
async def handle_new_message(event):
    if event.text == 'meow' or event.text == 'Meow' or event.text.startswith('meow') or \
    event.text.startswith('Meow'):
        await event.respond(random.choice(my_messages))

borg.start()
borg.run_until_disconnected()