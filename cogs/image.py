import discord
from discord.ext import commands
import random
import os
import asyncio
import praw

# De Catogorie
#Dat tussen () is voor de rewrite versie


class Image(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please type all required arguments.')

        if isinstance(error, commands.CommandNotFound):
            await ctx.send('This command does not exist.')

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to do that!")

# event in een cog moet altijd dit @commands.Cog.listener() hebben.
# self moet altijd als eerst in een class event ding staan.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Meme Image is working.')
    reddit = praw.Reddit(client_id='',
                         client_secret='',
                         user_agent='Script by /u/Turbootzz',
                         username='',
                         password='')

    @commands.command()
    async def testmeme(self, reddit, *, ctx):
        await ctx.send('Loading meme...')
        memes_submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 15)
        for i in range(0, post_to_pick):
            submission = next(x for x in memes_submissions if not x.stickied)

        await ctx.send(submission.url)
        reddit.read_only = True


async def setup(client):
    await client.add_cog(Image(client))
