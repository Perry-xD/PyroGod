# All rights reserved.
# Made by @Perry_xD

from config import PREFIX
import asyncio
import time
from datetime import datetime
from pyrogram import filters
from pyrogod import app, StartTime
from pyrogod.modules.help import add_command_help
from sys import version_info

from pyrogram import __version__ as __pyro_version__
from pyrogram.types import Message, User



add_command_help(
    
        "alive", [
  ["`alive`", "Show off to people with your bot using this command."],
  ["`ping`", "Shows you the response speed of the bot."],
               ],
    
)

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@app.on_message(filters.command("alive", PREFIX) & filters.me)
async def alive(_, m):
    start_time = time.time()
    uptime = get_readable_time((time.time() - StartTime))
    username = m.from_user.first_name
    userid = m.from_user.id
    reply_msg = f"**[PyroGod](https://github.com/GODBOYX/PYROGOD)**\n"
    reply_msg += f"**[PyroGod-Beta](https://github.com/GODBOYX/PYROGOD-BETA)**\n"
    reply_msg += f"__Moi Sweet Master__ : [{username}](tg://user?id={userid})\n"
    reply_msg += f"__Python Version__ : `{__python_version__}`\n"
    reply_msg += f"__PyroGram Version__ : `{__pyro_version__}`\n"
    end_time = time.time()
    reply_msg += f"__pyrogod uptime__: {uptime}"
    photo = "https://telegra.ph/file/a76de9682c4525d418058.jpg"
    await m.delete()
    if m.reply_to_message:
        await app.send_photo(
            m.chat.id,
            photo,
            caption=reply_msg,
            reply_to_message_id=m.reply_to_message.message_id,
        )
    else:
        await app.send_photo(m.chat.id, photo, caption=reply_msg)


@app.on_message(filters.command("ping", PREFIX) & filters.me)
async def pingme(_, message: Message):
    start = datetime.now()
    await message.edit("`Pong!!!`")
    end = datetime.now()
    m_s = (end - start).microseconds / 1000
    await message.edit(f"[Deploy PyroGod](https://github.com/GODBOYX/PyroGod)\n\n**Pong!**\n`{m_s} ms`", disable_web_page_preview=True)
