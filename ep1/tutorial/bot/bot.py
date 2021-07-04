import discord
import os
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pytz import utc
from dotenv import load_dotenv

OWNER_IDS = [860721513958342676]
PREFIX = "."

load_dotenv()

class Bot(commands.Bot):
    def __init__(self):
        self.ready = False
        self.scheduler = AsyncIOScheduler()
        self.scheduler.configure(timezone=utc)
        self.prefix = PREFIX

        super().__init__(
            command_prefix=self.prefix,
            owner_ids=OWNER_IDS,
            case_sensitive=True,
            intents=discord.Intents.all()
        )

    def run(self):
        print("Running bot")

        super().run(os.environ.get("TOKEN"), reconnect=True)
    

    async def on_connect(self):
        print("Bot connected")

    async def on_disconnect(self):
        print("Bot disconnected")

    async def on_ready(self):
        if not self.ready:
            print("Bot is ready!")
        
        else:
            print("Bot reconnected")
