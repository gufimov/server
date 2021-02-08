import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

API_ID = int(os.getenv("2048409"))
API_HASH = os.getenv("649e419e5fa739da02b649780d492c1b")

with TelegramClient(StringSession(), API_ID, API_HASH) as client:
    print(client.session.save())
