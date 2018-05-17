#Imports some important stuff.
import discord
from discord.ext import commands

#Declares some important variables.
bot = commands.Bot(command_prefix='mge!')
devid = '303667865863716865'
token = 'NDQ2MTQxNjkwNDU0MDgxNTM2.Dd0tqg.uA8ThL8LUbZmP6DzRNBWgb8MBx8'

#Notifies the console of a successful log-in, and sets the bot's playing status.
@bot.event
async def on_ready():
    print('Logged in as ' + bot.user.id + '.')
    await bot.change_presence(game=discord.Game(name="Use mge!help"))

#Allows for the help command.
bot.remove_command("help")

#Command returns help.
@bot.command()
async def help():
    await bot.say("__**Monster Girl Encyclopedia Discord Bot Help**__ \n \n Need to know who made me, who owns my source material, and how to invite me to your server? Use ``mge!info``. \n \n To get the encyclopedia page of a monster girl, simply type that monster girl's name as a command. For the command to work, type it using only lowercase letters and without spaces. If the monster girl's name has a space, omit it when using the command. \n For example, typing ``mge!akaname`` will return the Akaname's encyclopedia page.")

#Command returns information on the bot.
@bot.command()
async def info():
    await bot.say("__**Monster Girl Encyclopedia Discord Bot**__ \n Hey there! I'm a bot created by <@" + devid + "> that allows you to get the encylopedia page of a monster girl with just one command. MGE belongs to Kenkou Cross. \n *Invite me to your server:* https://discordapp.com/oauth2/authorize?client_id=446141690454081536&permissions=378944&scope=bot \n *Version 0.0*")

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
    
#Starts the bot.
bot.run(token)
