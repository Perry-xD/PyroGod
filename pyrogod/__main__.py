# (C) 2021 Paramendra Singh

from pyrogram import idle, Client, filters
from pyrogram.types import Message
from pyrogod import app, LOGGER
from config import *
from pyrogod.modules import *
from pyrogod import *
import os


async def pyro_on_fire(_, message: Message):
  await app.send_message(LOG_CHAT, "**#SUCCESS**\n\n**Your PyroGod Deployed Successfully**\n\n**NOW ENJOY!!!**")





print("PyroGod Started \nPowered By @Perry_XD\n(C) 2021 Paramedra Singh")




if __name__ == "__main__":
  app.run()
  goat.run()
