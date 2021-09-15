import sys
import time
import asyncio

from datetime import datetime
from telethon import TelegramClient, functions
from telethon.errors.rpcerrorlist import FloodWaitError

import yaml

with open("settings.yml", "r", encoding="utf8") as settings:
    CONFIG = yaml.safe_load(settings)

API_ID = CONFIG["api_id"]
API_HASH = CONFIG["api_hash"]
APP_SHORT_NAME = CONFIG["app_short_name"]
PHONE_NUMBER = CONFIG["phone_number"]

def log(message):
    now = datetime.now()
    print("[" + now.strftime("%H:%M:%S.%f")[:-3] + "] " + message)

async def doit():
    await CLIENT.connect()
    sent = await CLIENT.send_code_request(PHONE_NUMBER)
    print(sent)

if __name__ == "__main__":
    CLIENT = TelegramClient(APP_SHORT_NAME, API_ID, API_HASH)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(doit())
    loop.close()
