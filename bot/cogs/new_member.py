import discord
import random
from discord.ext import commands


class NewMember(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            response = [
                f'Welcome {member.mention} to {guild.name}!',
                f'Hi! {member.mention}. Welcome to {guild.name}!',
                f'A wild {member.mention} appeared in {guild.name}',
                f'Whose that pokemon??? Its.....{member.mention}!!!'
            ]
            await guild.system_channel.send(random.choice(response))

            # Welcomes User
            embed = discord.Embed(title='{}\'s info'.format(member.name))
            embed.add_field(name='Name', value=member.name, inline=True)
            embed.add_field(name='ID', value=member.id, inline=True)
            embed.add_field(name='Status', value=member.status, inline=True)
            embed.add_field(name='Roles', value=member.top_role)
            embed.add_field(name='Joined', value=member.joined_at)
            embed.add_field(name='Created', value=member.created_at)
            embed.set_thumbnail(url=member.avatar_url)
            await guild.system_channel.send(embed=embed)


def setup(client):
    client.add_cog(NewMember(client))
