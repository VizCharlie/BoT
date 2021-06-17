import discord
import random
from discord.ext import commands


class Reply(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=['bots'])
    async def bot(self, ctx):
        embed = discord.Embed(title=f'{self.client.user.name}\'s ѕтαтυѕ', color=0xffffff)
        embed.add_field(name='иαмє', value=self.client.user.name, inline=True)
        embed.add_field(name='ιᴅ', value=self.client.user.id, inline=True)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.set_footer(text=f'🤖 ᴄσииᴄтєᴅ тσ ᴅιѕᴄσяᴅ ( ʟαтєиᴄу: {self.client.latency*1000:.2f} мѕ )')
        await ctx.send(embed=embed)

    @commands.command(aliases=['hi', 'greetings'])
    async def hello(self, ctx):
        response = [
            f'Hello! {ctx.author.mention}',
            f'Hey! {ctx.author.mention}. How you doin?'
        ]
        await ctx.send(random.choice(response))

    @commands.command(aliases=['user', 'info'])
    async def whois(self, ctx, *, member: discord.Member):
        embed = discord.Embed(title=f'{member.name}\'s info')
        embed.add_field(name='Name', value=member.name, inline=True)
        embed.add_field(name='ID', value=member.id, inline=True)
        embed.add_field(name='Status', value=member.status, inline=True)
        embed.add_field(name='Roles', value=member.top_role)
        embed.add_field(name='Joined', value=member.joined_at)
        embed.add_field(name='Created', value=member.created_at)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested By {ctx.author.name}')

        await ctx.send(embed=embed)