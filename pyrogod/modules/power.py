# MADE BY @PERRY_XD, GODBOYX
# KANG WITH CREDITS ELSE GAY!!
import asyncio
import os
import sys
import heroku3
from pyrogram import filters
from pyrogram.types import Message
from pyrogod import app
from pyrogod.modules.help import add_command_help
from config import PREFIX
from config import *

add_command_help(
    
        "power", [
                ["`{PREFIX}restart`", "To update PyroGod Userbot"],
                ],

    
)


@app.on_message(filters.command("restart", PREFIX) & filters.me)
async def restart(client, message):
    try:
        await message.edit("Restarting your Userbot, It will take few minutes, Please Wait")
        heroku_conn = heroku3.from_key(HEROKU_API)
        server = heroku_conn.app(HEROKU_APP_NAME)
        server.restart()
    except Exception as e:
        await message.edit(f"Your `HEROKU_APP_NAME` or `HEROKU_API` is Wrong or Not Filled, Please Make it correct or fill it \n\nError: ```{e}```")
