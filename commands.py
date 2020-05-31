from discord.ext import commands
from discord.utils import get
from datamanager import add_guild
@commands.command()
async def sayhello(cnx):
    await cnx.send(f"Hello there {cnx.channel}!")

@commands.command()
async def register(cnx):
    try:
        add_guild(cnx.guild.id, cnx.guild.name)
        await cnx.send("This guild is registered!")
    except Exception as error:
        await cnx.send(str(error))
    
    
    
    