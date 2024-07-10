import discord
from discord.ext import commands
from discord import Color, Embed
import asyncio


# De Catogorie
class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

# event in een cog moet altijd dit @commands.Cog.listener() hebben.
# self moet altijd als eerst in een class event ding staan.
    @commands.Cog.listener()
    async def on_ready(self):
        print('Basic Cog is working.')


    """
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please type all required arguments.')

        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to do that!")
    """

    """
    AUTO HELP
    
    @bot.command(name="help", description="Returns all commands available")
    async def help(self, ctx):
        helptext = "```"
        for command in self.bot.commands:
            helptext+=f"{command}\n"
        helptext+="```"
        await ctx.send(helptext)

    """


# Stuurt naar user de help embed. (Old help page without multiple pages)
    # @commands.command(name='help', aliases=['help1'])
    # @commands.guild_only()
    # @commands.cooldown(1, 4, commands.BucketType.guild)
    # async def help_embed(self, ctx):

    #     embed = discord.Embed(title='SystemTH Help Page',
    #                           description='Showcasing how to use the bot.\nUse the . prefix!\nType .help2\nType .premium for cmds.',
    #                           colour=0x00AEE3)
    #     embed.set_author(name='SystemTH',
    #                      url='https://top.gg/bot/653220332454412288',
    #                      icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653593477065736193/44daf07badb99eed25cac89e390bc2198a8ad3e4_full.jpg')
    #     # embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')
    #     embed.add_field(name='Basic Commands ', value=' help\nping\nvote\ndonate\nwebsite', inline=True)
    #     embed.add_field(name=' Explanation', value='Shows this page.\nShows the latency of the bot.\nSupport the bot by voting.\nGet new epic features. (C S)\nVisit the Turboot Website', inline=True)
    #     embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone', inline=True)
    #     embed.add_field(name='Fun Commands ', value=' predict (what to predict)\npoop\nsounds\nplaysound (sound)', inline=True)
    #     embed.add_field(name=' Explanation', value='It predicts your sentence.\nJust says something back.\nList of sounds.\nPlays a real nice sound ;)', inline=True)
    #     embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone', inline=True)
    #     embed.add_field(name='Music Commands ', value=' join\nplay (name/link)\npause\nresume\nskip\nqueue\nnow_playing [or .np]\nvolume (%)\nstop\n\nType .help2 for the second page!', inline=True)
    #     embed.add_field(name=' Explanation', value='Bot joins VC.\nPlays a song.\nPauses the song.\nResumes the song.\nSkips a song.\nShows upcoming songs.\nShows current song.\nChange the volume in %.\nStops the song and queue.', inline=True)
    #     embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone', inline=True)
    #     embed.add_field(name='Bot Website', value='[Click Here!](https://top.gg/bot/653220332454412288)', inline=True)
    #     embed.add_field(name='Command Invoker', value=ctx.author.mention, inline=True)
    #     embed.set_footer(text='Bot made by Turboot#3918', icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653606619577581568/2.jpg')

    #     await ctx.send(content=f'**Here is some help for you {ctx.author.mention}.**', embed=embed)
    #     print(f'[TH CommandLog]: {ctx.author} uses .help')

# Stuurt naar user de help embed.
    @commands.command(name='help')
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def help_embed2(self, ctx, *args):

        if len(args) == 0:
            embed = discord.Embed(title='SystemTH Help Page',
                              description='Showcasing how to use the bot.\nUse the . prefix!\nType .help 2\nType .premium for cmds.',
                              colour=0x00AEE3)
            embed.set_author(name='SystemTH',
                         url='https://top.gg/bot/653220332454412288',
                         icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653593477065736193/44daf07badb99eed25cac89e390bc2198a8ad3e4_full.jpg')
            # embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')
            embed.add_field(name='Basic Commands ', value=' help (page)\nping\nvote\ndonate\nwebsite', inline=True)
            embed.add_field(name=' Explanation', value='Shows help page.\nShows the latency of the bot.\nSupport the bot by voting.\nGet new epic features. (C S)\nVisit the Turboot Website', inline=True)
            embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone', inline=True)
            embed.add_field(name='Fun Commands ', value=' predict (what to predict)\npoop\nsounds\nplaysound (sound)', inline=True)
            embed.add_field(name=' Explanation', value='It predicts your sentence.\nJust says something back.\nList of sounds.\nPlays a real nice sound ;)', inline=True)
            embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone', inline=True)
            embed.add_field(name='Music Commands ', value=' join\nplay (name/link)\npause\nresume\nskip\nqueue\nnow_playing [or .np]\nvolume (%)\nstop\n\nType .help2 for the second page!', inline=True)
            embed.add_field(name=' Explanation', value='Bot joins VC.\nPlays a song.\nPauses the song.\nResumes the song.\nSkips a song.\nShows upcoming songs.\nShows current song.\nChange the volume in %.\nStops the song and queue.', inline=True)
            embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone', inline=True)
            embed.add_field(name='Bot Website', value='[Click Here!](https://top.gg/bot/653220332454412288)', inline=True)
            embed.add_field(name='Command Invoker', value=ctx.author.mention, inline=True)
            embed.set_footer(text='Bot made by Turboot#3918', icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653606619577581568/2.jpg')

            await ctx.send(content=f'**Here is some help for you {ctx.author.mention}.**', embed=embed)
            print(f'[TH CommandLog]: {ctx.author} uses .help')


        else:
            if args[0] == "1":
                embed = discord.Embed(title='SystemTH Help Page',
                              description='Showcasing how to use the bot.\nUse the . prefix!\nType .help 2\nType .premium for cmds.',
                              colour=0x00AEE3)
                embed.set_author(name='SystemTH',
                         url='https://top.gg/bot/653220332454412288',
                         icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653593477065736193/44daf07badb99eed25cac89e390bc2198a8ad3e4_full.jpg')
                # embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')
                embed.add_field(name='Basic Commands ', value=' help (page)\nping\nvote\ndonate\nwebsite', inline=True)
                embed.add_field(name=' Explanation', value='Shows help page.\nShows the latency of the bot.\nSupport the bot by voting.\nGet new epic features. (C S)\nVisit the Turboot Website', inline=True)
                embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone', inline=True)
                embed.add_field(name='Fun Commands ', value=' predict (what to predict)\npoop\nsounds\nplaysound (sound)', inline=True)
                embed.add_field(name=' Explanation', value='It predicts your sentence.\nJust says something back.\nList of sounds.\nPlays a real nice sound ;)', inline=True)
                embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone', inline=True)
                embed.add_field(name='Music Commands ', value=' join\nplay (name/link)\npause\nresume\nskip\nqueue\nnow_playing [or .np]\nvolume (%)\nstop\n\nType .help2 for the second page!', inline=True)
                embed.add_field(name=' Explanation', value='Bot joins VC.\nPlays a song.\nPauses the song.\nResumes the song.\nSkips a song.\nShows upcoming songs.\nShows current song.\nChange the volume in %.\nStops the song and queue.', inline=True)
                embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone', inline=True)
                embed.add_field(name='Bot Website', value='[Click Here!](https://top.gg/bot/653220332454412288)', inline=True)
                embed.add_field(name='Command Invoker', value=ctx.author.mention, inline=True)
                embed.set_footer(text='Bot made by Turboot#3918', icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653606619577581568/2.jpg')

                await ctx.send(content=f'**Here is some help for you {ctx.author.mention}.**', embed=embed)
                print(f'[TH CommandLog]: {ctx.author} uses .help')

            if args[0] == "2":
                embed = discord.Embed(title='SystemTH Help Page 2',
                              description='Showcasing how to use the bot.\nUse the . prefix!\nType .premium for cmds.',
                              colour=0x00AEE3)
                embed.set_author(name='SystemTH',
                              url='https://top.gg/bot/653220332454412288',
                              icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653593477065736193/44daf07badb99eed25cac89e390bc2198a8ad3e4_full.jpg')
                # embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')
                embed.add_field(name='Image Commands ', value=' meme\nanime\nfoodporn\nshitfood\nnaruto\npokemon\nmakemesuffer\nnsfw\nhentai\nbigbrain\navatar', inline=True)
                embed.add_field(name=' Explanation', value='Shows Memes.\nShows Anime.\nShows Foodporn.\nShows shitty foodporn.\nShows Naruto stuff\nShows Pokémon stuff.\nMakes you Suffer.\nShows NSFW gifs.\nShows Hentai gifs.\nRate your bigbrain\nShows persons avatar', inline=True)
                embed.add_field(name=' Permission', value='Everyone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone\nEveryone(nsfw)\nEveryone(nsfw)\nEveryone\nEveryone', inline=True)
                embed.add_field(name='Premium Commands ', value=' amongus\nfiftyfifty\nwaifu', inline=True)
                embed.add_field(name=' Explanation', value='Shows Among Us memes.\nGet a 50/50 image.\nGet a waifu', inline=True)
                embed.add_field(name=' Permission', value='Premium\nPremium(nsfw)\nPremium', inline=True)
                embed.add_field(name='Staff Commands ', value=' clear (amount)\nenable\ndisable\nreload', inline=True)
                embed.add_field(name=' Explanation', value='Clears messages.\nEnables a Catogory of the bot.\nDisables a Catogory of the bot.\nReloads a Catogory of the bot. (for updates)', inline=True)
                embed.add_field(name=' Permission', value='Moderator\nDev\nDev\nAdmin/Dev', inline=True)
                embed.add_field(name='Bot Website', value='[Click Here!](https://top.gg/bot/653220332454412288)', inline=True)
                embed.add_field(name='Command Invoker', value=ctx.author.mention, inline=True)
                embed.set_footer(text='Bot made by Turboot#3918', icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653606619577581568/2.jpg')

                await ctx.send(content=f'**Here is some help for you {ctx.author.mention}.**', embed=embed)
                print(f'[TH CommandLog]: {ctx.author} uses .help 2')

            

    @commands.command(name='premium')
    @commands.guild_only()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def premium_embed(self, ctx, *args):

        embed = discord.Embed(title='SystemTH Help Page Premium',
                              description='Showcasing the premium cmds',
                              colour=0x00AEE3)
        embed.set_author(name='SystemTH',
                              url='https://top.gg/bot/653220332454412288',
                              icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653593477065736193/44daf07badb99eed25cac89e390bc2198a8ad3e4_full.jpg')
        # embed.set_image(url='https://cdn.discordapp.com/attachments/84319995256905728/252292324967710721/embed.png')
        embed.add_field(name='Image Commands ', value=' amongus\nfiftyfifty\nwaifu', inline=True)
        embed.add_field(name=' Explanation', value='Shows Among Us memes.\nGet a 50/50 image.\nGet a waifu.', inline=True)
        embed.add_field(name=' Permission', value='Premium\nPremium(nsfw)\nPremium', inline=True)
        embed.add_field(name='Bot Website', value='[Click Here!](https://top.gg/bot/653220332454412288)', inline=True)
        embed.add_field(name='Command Invoker', value=ctx.author.mention, inline=True)
        embed.set_footer(text='Bot made by Turboot#3918', icon_url='https://cdn.discordapp.com/attachments/653233619506036758/653606619577581568/2.jpg')

        await ctx.send(content=f'**Here is some help for you {ctx.author.mention}.**', embed=embed)
        print(f'[TH CommandLog]: {ctx.author} uses .help2')

    """
    @commands.command()
    async def amongusrank(self, ctx, role: discord.Role):
        await ctx.add_roles(role)
        await ctx.send(f"{ctx.author} joinen the Among Us rank")
    """

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.guild)
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=653220332454412288&permissions=8&scope=bot")


async def setup(client):
    await client.add_cog(Basic(client))
