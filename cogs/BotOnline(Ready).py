import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('#Fluid_Bot is now online | Server Backed up | All Cogs are ready | Discord = XYZ#0003 | Enjoy the Bot')

def setup(client):
    client.add_cog(Example(client))