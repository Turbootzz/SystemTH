import discord
from discord.ext import commands
import random
import os
import asyncio
from aiohttp import request
# De Catogorie
#Dat tussen () is voor de rewrite versie
class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    def donator():
        def predicate(ctx):
            return ctx.message.author.id in (397012276206370826, 98079042086912000, 485106562407333889, 295278844040970243, 446763706525679627, 306716112538828802, 282473051768225792)
        return commands.check(predicate)

# event in een cog moet altijd dit @commands.Cog.listener() hebben.
# self moet altijd als eerst in een class event ding staan.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun Cog is working.')

    """
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please type all required arguments.')

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to do that!")
    """

# voorbeeld hoe je een command maakt in cog:
    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def poop(self, ctx):
        await ctx.send('STINKYYY')

    @commands.command(name='imagetest')
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def imagetest_embed(self, ctx):
        file = discord.File("./img/test.png", filename="test.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://test.png")
        await ctx.send(file=file, embed=embed)

    @commands.command(name='chinny')
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def chinny_embed(self, ctx):
        file = discord.File("./img/chin.jpg", filename="chin.jpg")
        embed = discord.Embed()
        embed.set_image(url="attachment://chin.jpg")
        await ctx.send(file=file, embed=embed)

    # @commands.command(name='sorry')
    # @commands.guild_only()
    # @commands.cooldown(1, 4, commands.BucketType.guild)
    # async def sorry_embed(self, ctx):
    #     file = discord.File("./img/sorry.png", filename="sorry.png")
    #     embed = discord.Embed()
    #     embed.set_image(url="attachment://sorry.png")
    #     await ctx.send(file=file, embed=embed)


    @commands.command(name='sorry')
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def sorry_embed(self, ctx):
        sorry_image=[
            ('http://turboot.com/images/sorry.png', 'VERY VERY MY SORRY'),
            ('http://turboot.com/images/sorry2.png', 'MY OPOPOGIES'),
            # ('http://turboot.com/images/lintpaard.png', 'HAHAHAH BAMBOOZLED')
        ]
        embed = discord.Embed(
            color=discord.Colour.dark_blue()

        )
        url, text = random.choice(sorry_image)

        embed.set_image(url=url)
        embed.set_footer(text=f'{text}')
        await ctx.send(embed=embed)


# werkt nog niet hieronder
#    @commands.command()
 #   async def bigbrain(self, ctx):
  #      await message.channel.send('take this', file=discord.File(random.choice('bigbrain1.png', 'bigbrain2.png', 'bigbrain3.png', 'bigbrain4.png', 'bigbrain5.png')))




#    @commands.command(aliases=['hugebrain'])
#    async def bigbrain(self, ctx):
#        brainlvl = [discord.File('./img/bigbrain1.png'),
#                    discord.File('./img/bigbrain2.png'),
#                    discord.File('./img/bigbrain3.png'),
#                    discord.File('./img/bigbrain4.png'),
#                    discord.File('./img/bigbrain5.png')]
#        await ctx.send(file=discord.File{random.choice(brainlvl))
#        print(f'[TH CommandLog]: {ctx.author} uses .bigbrain')


#    brainlvl = os.path.join(os.path.dirname(__file__), "./brainlvl/")
# Cats = "images/" - to just use the relative path

#    @commands.command()
#    async def brainlvl(self, ctx, **kwargs):
#        await ctx.send(file=File((choice(brainlvl)))

#    @commands.command()
#    async def randomtest(self, ctx):
#        kies = ["poep", "plas", "kots", "sap"]
#        await ctx.send(random.choice(kies))



    """ WAIFU OLD
    @commands.command(aliases=["waifu","waifurandom"])
    @donator()
    async def waifu_embed(self, ctx):
        waifu_image=[
            'http://turboot.com/waifu/waifu1.png',
            'http://turboot.com/waifu/waifu2.jpg',
            'http://turboot.com/waifu/raphtalia.jpg',
            'http://turboot.com/waifu/rem.jpg'
        ]
        embed = discord.Embed(
            color=discord.Colour(0xFF94F9)
        )
        embed.set_image(url=random.choice(waifu_image))
        embed.set_footer(text=f'Requested by: {ctx.author.name}')
        await ctx.send(embed=embed)

    @commands.command(aliases=["wbetter","wbetterr"])
    async def waifu_embed1(self, ctx):
        waifu_image=('https://waifu.pics/api/sfw/waifu')
        embed = discord.Embed(
            color=discord.Colour(0xFF94F9)
        )
        embed.set_image(url=waifu_image)
        embed.set_footer(text=f'Requested by: {ctx.author.name}')
        await ctx.send(embed=embed)
    """

    @commands.command()
    @donator()
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def waifu(self, ctx):
        waifuimage = "https://waifu.pics/api/sfw/waifu"

        async with request ("GET", waifuimage, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                image_link = data["url"]
                embed = discord.Embed(title="WAIFU",
                              
                              colour=ctx.author.colour)
                embed.set_image(url=image_link)
                embed.set_footer(text=f'Requested by: {ctx.author.name}')
                await ctx.send(embed=embed)

            else:
                await ctx.send(f"API returned a {response.status} status.")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def bully(self, ctx, *, member: discord.Member):
        bullyimage = "https://waifu.pics/api/sfw/bully"

        async with request ("GET", bullyimage, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                image_link = data["url"]
                embed = discord.Embed(
                              colour=ctx.author.colour)
                embed.set_image(url=image_link)
                embed.add_field(name="BULLY", value=f"{ctx.author.mention} bullies {member.mention}")
                await ctx.send(embed=embed)


            else:
                await ctx.send(f"API returned a {response.status} status.")


    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def dance(self, ctx):
        danceimage = "https://waifu.pics/api/sfw/dance"

        async with request ("GET", danceimage, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                image_link = data["url"]
                embed = discord.Embed(
                              colour=ctx.author.colour)
                embed.set_image(url=image_link)
                embed.add_field(name="DANCE", value=f"{ctx.author.mention} is dancing!")
                await ctx.send(embed=embed)


            else:
                await ctx.send(f"API returned a {response.status} status.")

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def cringe(self, ctx, *, member: discord.Member):
        cringeimage = "https://waifu.pics/api/sfw/cringe"

        async with request ("GET", cringeimage, headers={}) as response:
            if response.status == 200:
                try:
                    data = await response.json()
                    image_link = data["url"]
                    embed = discord.Embed(
                              colour=ctx.author.colour)
                    embed.set_image(url=image_link)
                    embed.add_field(name="CRINGE", value=f"{ctx.author.mention} is cringing due to {member.mention}")
                    await ctx.send(embed=embed)

                except:

                    data = await response.json()
                    image_link = data["url"]
                    embed = discord.Embed(
                              colour=ctx.author.colour)
                    embed.set_image(url=image_link)
                    embed.add_field(name="CRINGE", value=f"{ctx.author.mention} is cringing..", )
                    await ctx.send(embed=embed)


            else:
                await ctx.send(f"API returned a {response.status} status.")

    @commands.command(aliases=["winkwink", ";)"])
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def wink(self, ctx):
        winkimage = "https://waifu.pics/api/sfw/wink"

        async with request ("GET", winkimage, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                image_link = data["url"]
                embed = discord.Embed(
                              colour=ctx.author.colour)
                embed.set_image(url=image_link)
                embed.add_field(name=";)", value=f"{ctx.author.mention} winks")
                await ctx.send(embed=embed)


            else:
                await ctx.send(f"API returned a {response.status} status.")


    """
    @commands.command()
    async def trigger(self, ctx, *, member:discord.Member=None):
        await ctx.channel.trigger_typing()
        if member is None:
            member = ctx.author
        download_file(get_avatar(member, animate=False), "data/trigger.png")
        avatar = Image.open("data/trigger.png")
        triggered = imagetools.rescale(Image.open("assets/imgs/pillow/triggered.jpg"), avatar.size)
        position = 0, avatar.getbbox()[3] - triggered.getbbox()[3]
        avatar.paste(triggered, position)
        avatar.save("data/trigger.png")
        await ctx.send(file=discord.File("data/trigger.png"))
    """

    @commands.command(aliases=["bigbrain","brainlvl"])
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def bigbrain_embed(self, ctx):
        bigbrain_image=[
            ('http://turboot.com/brainlvl/bigbrain1.png', 'BIGBRAIN SMOLL 1%'),
            ('http://turboot.com/brainlvl/bigbrain2.png', 'BIGBRAIN MEDIUM 26%'),
            ('http://turboot.com/brainlvl/bigbrain3.png', 'BIGBRAIN BIG 44%'),
            ('http://turboot.com/brainlvl/bigbrain4.png', 'BIGBRAIN LARGE 62%'),
            ('http://turboot.com/brainlvl/bigbrain5.png', 'BIGBRAIN HUGEEE 70%'),
            ('http://turboot.com/brainlvl/bigbrain6.png', 'BIGBRAIN SUPERHUGE 81%'),
            ('http://turboot.com/brainlvl/bigbrain7.png', 'BIGBRAIN ENORMOUS 100%')
        ]
        embed = discord.Embed(
            color=discord.Colour.dark_blue()

        )
        url, text = random.choice(bigbrain_image)

        embed.set_image(url=url)
        embed.set_footer(text=f'Brainlvl: {text}')
        await ctx.send(embed=embed)


    @commands.command(aliases=["applejuice","appelsap"])
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def applejuice_embed(self, ctx):
        applejuice_image=[
            ('http://turboot.com/applejuice/1.jpg', 'YUMMY YUMMY SO NICE'),
            ('http://turboot.com/applejuice/2.jpg', 'aaaahh I LIKE'),
            ('http://turboot.com/applejuice/3.jpg', 'WOOOOW'),
            ('http://turboot.com/applejuice/4.jpg', 'APPLE JUICE'),
            ('http://turboot.com/applejuice/5.jpg', ':P'),
            ('http://turboot.com/applejuice/6.jpg', 'dfskfdmvfmf'),
            ('http://turboot.com/applejuice/7.jpg', 'AAAHHHHH'),
            ('http://turboot.com/applejuice/8.jpg', 'i like'),
            ('http://turboot.com/applejuice/9.jpg', 'sooo tasty.'),
            ('http://turboot.com/applejuice/10.jpg', 'SLURP'),
            ('http://turboot.com/applejuice/11.jpg', 'YUM'),
            ('http://turboot.com/applejuice/12.jpg', 'HAHA'),
            ('http://turboot.com/applejuice/13.jpg', 'OOPS-'),
            ('http://turboot.com/applejuice/14.jpg', 'OMG NO WAY'),
            ('http://turboot.com/applejuice/15.jpg', 'sooo goooooood'),
            ('http://turboot.com/applejuice/16.jpg', 'PLEASE'),
            ('http://turboot.com/applejuice/17.jpg', 'YAMM'),
            ('http://turboot.com/applejuice/18.jpg', 'EY that mine.'),
            ('http://turboot.com/applejuice/19.jpg', 'WOOOW'),
            ('http://turboot.com/applejuice/20.jpg', 'HMHMHMM')
        ]
        embed = discord.Embed(
            color=discord.Colour.dark_blue()

        )
        url, text = random.choice(applejuice_image)

        embed.set_image(url=url)
        embed.set_footer(text=f'{text}')
        await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def avatar(self, ctx, *, member: discord.Member=None): # set the member object to None
        if not member: # if member is no mentioned
            member = ctx.message.author # set member as the author
        userAvatar = member.avatar_url
        await ctx.send(userAvatar)


# aliases kan je meerdere commands hetzelfde laten doen.
# De _ zorgt ervoor dat je een nummer als eerst kan zetten.
# * daarmee kan je spaties gebruiken na het command
    @commands.command(aliases=['8ball', 'eightball', 'predict'])
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def _8ball(self, ctx, *, question):
        responses = ['As I see it, yes.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don’t count on it.',
                     'It is certain.',
                     'It is decidedly so.',
                     'Most likely.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Outlook good.',
                     'Reply hazy, try again.',
                     'Signs point to yes.',
                     'Very doubtful.',
                     'Without a doubt.',
                     'Yes.',
                     'Yes – definitely.',
                     'You may rely on it.']
        await ctx.send(f'{ctx.author}s Question: {question}\nAnswer: {random.choice(responses)}')
        print(f'[TH CommandLog]: {ctx.author} uses .predict')

    @commands.command(name='sounds', aliases=['soundlist', 'slist'])
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def sounds_embed(self, ctx):

        embed = discord.Embed(title='SystemTH Sounds List',
                              description='Use .playsound (sound)',
                              colour=discord.Color.purple())
        embed.set_author(name='SystemTH',
                         url='https://discordapp.com/',  # moet nog een bot link toevoegen!
                         icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653593477065736193/44daf07badb99eed25cac89e390bc2198a8ad3e4_full.jpg')
        # embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')
        embed.add_field(name='Sounds to play ', value=' yum\nscawy\njeen\ndisgusting\nhayyah\nyooo', inline=True)
        embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone', inline=True)

        await ctx.send(content=f'**Here you go {ctx.author.mention} :)**', embed=embed)

    @commands.command(name='donators', aliases=['donated', 'donatelist', "donations"])
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def donators_embed(self, ctx):

        embed = discord.Embed(title='SystemTH Donators List',
                              description='Top supporters of the bot :)',
                              colour=discord.Color.green())
        embed.set_author(name='SystemTH',
                         url='https://discordapp.com/',  # moet nog een bot link toevoegen!
                         icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653593477065736193/44daf07badb99eed25cac89e390bc2198a8ad3e4_full.jpg')
        # embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')
        embed.add_field(name='Donators ', value=' 1. Gab\n2. [FIRST]Rowley\n3. AnCore\n4. Kwaktillo\n5. Benneeplus\n6. Andyyyyy\n7. JauJau\n8. Daan\n9. -\n10. -', inline=True)
        embed.add_field(name=' Amount', value='€41,00\n€18,00\n€1,00\n€0,69\n€0,69\n€0,69\n€0,02\n€0,01\n€0,00\n€0,00', inline=True)

        await ctx.send(content=f'**Here you go {ctx.author.mention} :)**', embed=embed)



    @commands.command(aliases=['sound', 'scream', 'say'])
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def playsound(self, ctx, *args):
        if len(args) == 0:
            await ctx.send("Choose a sound.\nOr type .sounds for the sound list.")

        else:
        #server = ctx.message.server
        #voice_client = client.voice_client_in(server)

            voice_player = await ctx.message.author.voice.channel.connect()

            if args[0] == "disgusting":
                print(f"Playing disgusting by: {ctx.author}.")
                retStr = str("""```css\nPlaying sound: disgusting```""")
                await ctx.send(retStr)
                source = discord.FFmpegPCMAudio("sounds/disgusting.mp3")
                await asyncio.sleep(0.2)
                voice_player.play(source)
                await asyncio.sleep(1.4)
                await voice_player.disconnect()

            if args[0] == "oceans":
                print(f"Playing Oceans by: {ctx.author}.")
                retStr = str("""```css\nPlaying sound: Oceans (not listed)```""")
                await ctx.send(retStr)
                source = discord.FFmpegPCMAudio("sounds/oceans.mp3")
                await asyncio.sleep(0.2)
                voice_player.play(source)
                await asyncio.sleep(275.0)
                await voice_player.disconnect()

            if args[0] == "yooo":
                print(f"Playing yooo by: {ctx.author}.")
                retStr = str("""```css\nPlaying sound: yooo```""")
                await ctx.send(retStr)
                source = discord.FFmpegPCMAudio("sounds/yooo.mp3")
                await asyncio.sleep(0.2)
                voice_player.play(source)
                await asyncio.sleep(2.3)
                await voice_player.disconnect()

async def setup(client):
    await client.add_cog(Fun(client))
