import logging
import sys
import time
import pyromod.listen
from pyrogram import Client, errors
from config import API_HASH, API_ID, PY_SESSION, BOT_TOKEN
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

LOGGER = logging.getLogger("pyrogram").setLevel(logging.WARNING)


HELP = {}
CMD_HELP = {}

StartTime = time.time()

API_ID = API_ID
API_HASH = API_HASH
PY_SESSION = PY_SESSION
BOT_TOKEN = BOT_TOKEN


app = Client(PY_SESSION, api_id=API_ID, api_hash=API_HASH)
goat = Client("godboy", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    
