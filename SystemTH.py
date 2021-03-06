import discord
import random
import os
import json
from discord.ext import commands, tasks
from discord.ext.commands import (has_permissions, MissingPermissions, CommandOnCooldown)
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
import asyncio
import sys
import traceback
from itertools import cycle
from discord.utils import get
from gtts import gTTS
from discord.ext.commands import bot
import praw
import time
import playsound
import speech_recognition as sr


if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": ""}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
"""
def get_prefix(client, message):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]
"""



client = commands.Bot(command_prefix = ".")
client.remove_command('help')
status = cycle(['.help for SystemCMDs', 'Made by: Turboot', 'The System Bot', 'Bot is now 24/7!!'])


""" vergeet daarboven niet get_prefix!

#wnr dat de bot een server joint
@client.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(guild.id)] = "."

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)


@client.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes.pop[str(guild.id)] = "."

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)

"""
# Als er een error is.
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please type all required arguments.')

    if isinstance(error, commands.CommandNotFound):
        await ctx.send('This command does not exist.')

    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You dont have permissions to do that!')

    if isinstance(error, commands.NSFWChannelRequired):
        await ctx.send("NSFW channel required!")

    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"Command on cooldown! Try again in {error.retry_after} seconds.")
    
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(f"You can't do that! **Premium** or **Dev** required!")


def dev(ctx):
    return ctx.author.id == 282473051768225792

def donator(ctx):
    return ctx.author.id in (397012276206370826, 98079042086912000, 485106562407333889, 295278844040970243, 446763706525679627, 306716112538828802, 282473051768225792)


# 397012276206370826,98079042086912000,485106562407333889,295278844040970243



# ctx represents the context
# {extension} zoekt voor de cog

# Om de files te laden als de bot start.
# ./ is de currente folder waar de bot in staat.
# [:-3] haalt de laatste 3 letters weg.

# Dit load / unload of reload de Catogorie (de cogs)
@client.command()
@commands.check(dev)
async def enable(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been enabled.')


@client.command()
@commands.check(dev)
async def disable(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been disabled.')


@client.command()
@commands.has_permissions(manage_roles=True)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded.')

initial_extensions = ['cogs.basic',
                      'cogs.fun',
                      'cogs.music']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()
# Wat er gebeurd als de bot start
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online)
    change_status.start()
    print(f"Logged in as {client.user}")
    print('Bot is ready :)')
    print('--------')
    print('Servers connected to:\n')
    for server in client.guilds:
        print(server.name)
    print('--------')


# Veranderd de status om elke hoeveelheid seconden
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))




@client.event
async def on_member_join(member):
    print(f'{member} has joined a server!')


@client.event
async def on_member_remove(member):
    print(f'{member} has left a server!')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def test(ctx):
    await ctx.send('GOOD JOB, ITS WORKING!')

"""
@client.command(aliases=["prefix"])
@commands.has_permissions(manage_roles=True)
@commands.cooldown(1, 30, commands.BucketType.guild)
async def changeprefix(ctx, prefix):
    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)

    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
        json.dump(prefixes, f, indent=4)
"""


@client.command()
@commands.check(dev)
async def servers(ctx):
    for server in client.guilds:
        await ctx.send(server.name)


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def vote(ctx):
    await ctx.send('Please vote for our bot here: https://top.gg/bot/653220332454412288/vote\nThank u very much :)')
    print(f'[TH CommandLog]: {ctx.author} uses .vote')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def donate(ctx):
    await ctx.send('Get some special features by donating me!\nIt also keeps me motivated to keep improving the bot for you guys!\nAfter you donated send a message to Turboot#3918 !\nPaypal donate link: https://paypal.me/pools/c/8l3uLY8J47\nIDEAL donate link: https://betaalverzoek.rabobank.nl/betaalverzoek/?id=b2-JK-6PTZKBIes3SQxnow')
    print(f'[TH CommandLog]: {ctx.author} uses .donate')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def website(ctx):
    await ctx.send('Turboot Website: http://turboot.com/')
    print(f'[TH CommandLog]: {ctx.author} uses .website')


# Het checkt of de gene die dit uitvoerd hetzelfde id heeft als hieronder.. zo niet dan pech.
def is_it_me(ctx):
    return ctx.author.id == 629271015767277568


@client.command()
@commands.check(is_it_me)
async def onlyme(ctx):
    await ctx.send(f'Hi {ctx.author}')

@client.command()
@commands.check(donator)
@commands.cooldown(1, 4, commands.BucketType.guild)
async def donatetest(ctx):
    await ctx.send(f"You are a donator {ctx.author}!")

@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def myname(ctx):
    await ctx.send(f"Your name: {ctx.author}!")


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def ping(ctx):
    await ctx.send(f'Bot ping: {round(client.latency * 1000)}ms')

''' In onderhoud
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

@client.command()
async def voice(ctx):
    voice_player = await ctx.message.author.voice.channel.connect()
    source = discord.speak("Hello Daddy")
    await asyncio.sleep(0.2)
    voice_player.play(source)
    await asyncio.sleep(6.4)  # wacht 6.4 seconden
    await voice_player.disconnect()
'''

reddit = praw.Reddit(client_id='ToCmBCE4W5E6sA',
                     client_secret='WnrQDV-hHuWYyC9ZrXY-pHbosjk',
                     user_agent='Script by /u/Turbootzz',
                     username='Turbootzz',
                     password='redM0rg3nSt0nd')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def meme(ctx):
    await ctx.send('Loading meme...')
    memes_submissions = reddit.subreddit('memes').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .meme')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def anime(ctx):
    await ctx.send('Loading anime...')
    memes_submissions = reddit.subreddit('anime').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .anime')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def foodporn(ctx):
    await ctx.send('Loading foodporn...')
    memes_submissions = reddit.subreddit('foodporn').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .foodporn')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def shitfood(ctx):
    await ctx.send('Loading shitty foodporn...')
    memes_submissions = reddit.subreddit('shittyfoodporn').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .shitfood')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def naruto(ctx):
    await ctx.send('Loading Naruto...')
    memes_submissions = reddit.subreddit('naruto').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .naruto')


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def pokemon(ctx):
    await ctx.send('Loading Pok??mon...')
    memes_submissions = reddit.subreddit('pokemon').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .pokemon')


@client.command(name='makemesuffer', aliases=['mms'])
@discord.ext.commands.is_nsfw()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def makemesuffer(ctx):
    await ctx.send('Loading MakeMeSuffer...')
    memes_submissions = reddit.subreddit('MakeMeSuffer').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .MakeMeSuffer')


@client.command()
@discord.ext.commands.is_nsfw()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def nsfw(ctx):
    await ctx.send('Loading NSFW...')
    memes_submissions = reddit.subreddit('NSFW_GIF').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .nsfw')


@client.command()
@discord.ext.commands.is_nsfw()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def hentai(ctx):
    await ctx.send('Loading Hentai...')
    memes_submissions = reddit.subreddit('HENTAI_GIF').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .hentai')


@client.command(aliases=['pedophile', 'children'])
@commands.check(dev)
@commands.cooldown(1, 4, commands.BucketType.guild)
async def pedo(ctx):
    await ctx.send('Searching the internet for children ;)...')
    memes_submissions = reddit.subreddit('ChildrenFallingOver').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True

    await asyncio.sleep(1)
    await ctx.send('Searching some more...')
    memes_submissions = reddit.subreddit('ChildrenFallingOver').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True

    await asyncio.sleep(1)
    await ctx.send('Searching MOREEEE...')
    memes_submissions = reddit.subreddit('ChildrenFallingOver').hot()
    post_to_pick = random.randint(1, 45)
    for i in range(0, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True


@client.command()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def vegan(ctx):
    await ctx.send('Loading Vegan...')
    memes_submissions = reddit.subreddit('vegan').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .vegan')

# -------------------------- PREMIUM --------------------- #

@client.command()
@commands.check(donator)
@commands.cooldown(1, 4, commands.BucketType.guild)
async def amongus(ctx):
    await ctx.send('Loading Among Us...')
    memes_submissions = reddit.subreddit('AmongUs').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .amongus')


@client.command(aliases=['5050', '50/50', 'FiftyFifty'])
@commands.check(donator)
@discord.ext.commands.is_nsfw()
@commands.cooldown(1, 4, commands.BucketType.guild)
async def fiftyfifty(ctx):
    await ctx.send('Loading FiftyFifty...')
    memes_submissions = reddit.subreddit('FiftyFifty').hot()
    post_to_pick = random.randint(1, 50)
    for i in range(2, post_to_pick):
        submission = next(x for x in memes_submissions if not x.stickied)

    await ctx.send(submission.url)
    reddit.read_only = True
    print(f'[TH CommandLog]: {ctx.author} uses .FiftyFifty')

    @nsfw.error
    async def nsfw_error(ctx, error):
        if ctx.channel.is_nsfw(error):
            await ctx.send("This is not a NSFW channel/server!")



# ------------------------------------------------------- #


@client.command()
@commands.has_permissions(manage_messages=True)
@commands.cooldown(1, 4, commands.BucketType.guild)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

# error voor de clear command
# Dit commando word uitgevoerd als de clear command een error heeft.
"""
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please specify an amount of messages to delete.')
        """


# \n = een enter
# je moet random importen voor random.choice

client.run(token)
