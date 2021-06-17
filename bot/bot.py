import discord
import os
from discord.ext import commands
from pathlib import Path


class IBot(commands.Bot):

    def __init__(self):
        self._cogs = [p.stem for p in Path('.').glob('./bot/cogs/*.py')]
        super().__init__(
            command_prefix='!',
            case_insensitive=True,
            intent=discord.Intents.all
        )

    def setup(self):
        print('Running Setup...')

        for cog in self._cogs:
            self.load_extension(f'bot.cogs.{cog}')
            print(f'Completed Loading {cog}.')

        print('Setup Completed')

    def run(self):
        self.setup()

        print(f'Running Bot...')
        super().run(os.getenv('TOKEN'), reconnect=True)

    async def shutdown(self):
        print('Closing Connection to Discord')
        await super().logout

    async def on_connect(self):
        print(f'Connected to Discord (latency: {self.latency * 1000} ms).')

    async def on_ready(self):
        self.client = (await self.application_info()).id
        await self.change_presence(status=discord.Status.online, activity=discord.Game('вσт'))
        print(f'{self.user.name} Ready')
