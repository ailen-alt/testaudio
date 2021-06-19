from .. import loader, utils
from requests import get
from io import BytesIO
from random import randint, choice
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap
import os
from telethon.sync import TelegramClient
from telethon import TelegramClient, events, sync
from telethon import functions,types
from time import sleep

bot = "NewSession"
api_id = 6600577
api_hash = 8c7460dc8d98c68d9a93c5e3da5a002c
client = TelegramClient(bot,api_id,api_hash)
client.start()
@client.on(event.NewMessage)
async def my_event_handler(event):
    if event.raw_text == "test":
        await event.edit("Прослушивание сообщения")
        sleep(1.0)
        await event.edit("Прослушивание сообщения.")
        sleep(1.0)
        await event.edit("Прослушивание сообщения..")
        sleep(1.0)
        await event.edit("Прослушивание сообщения...")
        sleep(1.0)
        await event.edit("Прослушивание сообщения")
        sleep(1.0)
        await event.edit("Прослушивание сообщения.")
        sleep(1.0)
        await event.edit("Прослушивание сообщения..")
        sleep(1.0)
        await event.edit("Прослушивание сообщения...")
        sleep(1.0)
        await event.edit("Пользователь установил ограничения на получение аудио сообщений." + "\n" + "\n" + "<b>Сообщение не доставлено.</b>")

client.run_until_disconnected()
