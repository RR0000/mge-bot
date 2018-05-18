#Imports some important stuff.
import discord
from discord.ext import commands

#Declares some important variables.
bot = commands.Bot(command_prefix='mge!')
dev_id = ''
token = ''

#Provides log-in info and sets the bot's playing status.
@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.name + '#' + bot.user.discriminator + '.')
    print('ID is ' + bot.user.id + '.')
    await bot.change_presence(game=discord.Game(name="Use mge!help"))

#Allows for the help command.
bot.remove_command("help")

#Command returns help.
@bot.command()
async def help():
    await bot.say("__**Monster Girl Encyclopedia Discord Bot Help**__ \n \n Need to know who made me, who owns my source material, and how to invite me to your server? Use ``mge!info``. \n \n To get the encyclopedia page of a monster girl, simply type that monster girl's name as a command. For the command to work, type it using only lowercase letters and without spaces or symbols. If the monster girl's name has a space or symbol, omit it when using the command. \n For example, typing ``mge!akaname`` will return the Akaname's encyclopedia page.")

#Command returns information on the bot.
@bot.command()
async def info():
    await bot.say("__**Monster Girl Encyclopedia Discord Bot**__ \n Hey there! I'm a bot created by <@" + dev_id + "> that allows you to get the encylopedia page of a monster girl with just one command. MGE belongs to Kenkou Cross. \n *Invite me to your server:* https://discordapp.com/oauth2/authorize?client_id=446141690454081536&permissions=378944&scope=bot \n *Version 0.0*")

#Commands return encyclopedia pages.
@bot.command()
async def akaname():
    embed=discord.Embed(title="Akaname", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/7/76/Akaname_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def alice():
    embed=discord.Embed(title="Alice", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/f/fa/Alice_eng3.png")
    await bot.say(embed=embed)

@bot.command()
async def alp():
    embed=discord.Embed(title="Alp", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/4/4d/Alp_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def alraune():
    embed=discord.Embed(title="Alraune", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/a/a9/Alraune_eng3.png")
    await bot.say(embed=embed)

@bot.command()
async def amazoness():
    embed=discord.Embed(title="Amazoness", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/a/ad/Amazoness_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def angel():
    embed=discord.Embed(title="Angel", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/a/a2/Angel_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def antarachne():
    embed=discord.Embed(title="Ant Arachne", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/7/78/AntArachne_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def anubis():
    embed=discord.Embed(title="Anubis", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/8/86/Anubis_eng3.png")
    await bot.say(embed=embed)

@bot.command()
async def apophis():
    embed=discord.Embed(title="Apophis", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/0/0f/Apophis_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def apsara():
    embed=discord.Embed(title="Apsara", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/6/62/Apsara_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def arachne():
    embed=discord.Embed(title="Arachne", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/8/89/Arachne_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def archimp():
    embed=discord.Embed(title="Arch Imp", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/2/28/Arch_Imp_eng1.jpg")
    await bot.say(embed=embed)

@bot.command()
async def atlachnacha():
    embed=discord.Embed(title="Atlach-Nacha", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/1/15/Atlach-nacha_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def automaton():
    embed=discord.Embed(title="Automaton", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/5/59/Automaton_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def baphomet():
    embed=discord.Embed(title="Baphomet", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/e/e1/Baphomet_eng3.png")
    await bot.say(embed=embed)

@bot.command()
async def barometz():
    embed=discord.Embed(title="Barometz", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/b/be/Barometz_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def basilisk():
    embed=discord.Embed(title="Basilisk", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/5/56/Basilisk_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def beelzebub():
    embed=discord.Embed(title="Beelzebub", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/f/f7/Beelzebub_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def bicorn():
    embed=discord.Embed(title="Bicorn", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/1/19/Bicorn_eng1.jpg")
    await bot.say(embed=embed)

@bot.command()
async def blackharpy():
    embed=discord.Embed(title="Black Harpy", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/3/3e/Black_Harpy_eng3.png")
    await bot.say(embed=embed)

@bot.command()
async def blueoni():
    embed=discord.Embed(title="Blue Oni", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/9/9c/Blue_Oni_eng1.jpg")
    await bot.say(embed=embed)

@bot.command()
async def bubbleslime():
    embed=discord.Embed(title="Bubble Slime", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/a/ac/Bubble_Slime_eng3.png")
    await bot.say(embed=embed)

@bot.command()
async def caitsith():
    embed=discord.Embed(title="Cait Sith", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/7/74/Cait_Sith_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def cancer():
    embed=discord.Embed(title="Cancer", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/2/2d/Cancer_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def centaur():
    embed=discord.Embed(title="Centaur", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/9/93/Centaur_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def charybdis():
    embed=discord.Embed(title="Charybdis", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/a/a2/Charybdis_eng2.PNG")
    await bot.say(embed=embed)

@bot.command()
async def cheshirecat():
    embed=discord.Embed(title="Cheshire Cat", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/2/25/Cheshire_Cat_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def chimaera():
    embed=discord.Embed(title="Chimaera", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/2/29/Chimaera_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def chochinobake():
    embed=discord.Embed(title="Chochin-Obake", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/1/17/Chochin-Obake_eng1.jpg")
    await bot.say(embed=embed)

@bot.command()
async def cockatrice():
    embed=discord.Embed(title="Cockatrice", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/d/d3/Cockatrice_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def crowtengu():
    embed=discord.Embed(title="Crow Tengu", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/f/fe/Crow_Tengu_eng2.png")
    await bot.say(embed=embed)

@bot.command()
async def cusith():
    embed=discord.Embed(title="Cu Sith", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/b/be/Cu_Sith_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def cupid():
    embed=discord.Embed(title="Cupid", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/9/91/Cupid_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def cursedsword():
    embed=discord.Embed(title="Cursed Sword", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/f/fe/Cursed_Sword_eng1.png")
    await bot.say(embed=embed)

@bot.command()
async def cyclops():
    embed=discord.Embed(title="Cyclops", color=0x896392)
    embed.set_image(url="http://mgewiki.com/images/0/0d/Cyclops_eng2.png")
    await bot.say(embed=embed)

#Starts the bot.
bot.run(token)
