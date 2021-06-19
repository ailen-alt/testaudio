from .. import loader, utils
from requests import get
from io import BytesIO
from random import randint, choice
from PIL import Image, ImageFont, ImageDraw
from textwrap import wrap

class AudioMeme(loader.Module):
    #.audio
    strings = {
		"name": "audio-meme"
	}

	async def client_ready(self, client, db):
		self.client = client

    @loader.owner
	async def audiom(self, message):
        if event.raw_text == ".taudio":
            await await message.edit("test")
