from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from pyrogod import goat
from config import *


@Client.on_message(filters.command("repo", PREFIX) & filters.private)
async def repo(_, m: Message):
  btn = InlineKeyboardMarkup([[InlineKeyboardButton("MY⭐REPO", url="https://github.com/Perry-xD/PyroGod")]])
  await m.reply_photo(photo="https://telegra.ph/file/12cea9b27a126e338d5ee.jpg", reply_markup=btn)

