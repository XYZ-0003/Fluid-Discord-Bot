import discord
import random
from discord.ext import commands

class ChatCommands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["Yes.",
                    "No.",]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    

def setup(client):
    client.add_cog(ChatCommands(client))
    
