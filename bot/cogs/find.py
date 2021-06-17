from discord.ext import commands
from googlesearch import search


class Find(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['search', 'google'])
    async def find(self, ctx, *, message):
        for j in search(message, tld="co.in", num=1, stop=1, pause=2):
            await ctx.send(j)


def setup(client):
    client.add_cog(Find(client))
