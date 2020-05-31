from discord.ext import commands
from discord.utils import get
from datamanager import add_guild, add_lobby, remove_guild

@commands.command()
async def helpme(cnx):
    await cnx.send(
        "This bot has following commands:\n" +
        "help: Duh!\n" + 
        "makelobby: make this channel into a lobby for new users\n"
        )

@commands.command()
async def makelobby(cnx):
    try:
        add_lobby(cnx.guild.id, cnx.channel.id)
        rules = "Rule 1: Don't be a dick \n" + "Rule 2: Have fun"
        await cnx.send("This channel is lobby now!")
        await cnx.send("Here the rules:")
        await cnx.send(f"```{rules}```")
        await cnx.send("If you accept, type '-!join' for members or '-!guest' for guests")
    except Exception as error:
        await cnx.send(str(error))
    
async def on_guild_join(guild):
    add_guild(guild.id, guild.name)

async def on_guild_remove(guild):
    remove_guild(guild.id)
    
    
    