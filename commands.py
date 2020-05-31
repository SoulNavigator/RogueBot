from discord.ext import commands
from discord.utils import get
from data import add_guild, set_channel
@commands.command()
async def sayhello(cnx):
    await cnx.send(f"Hello there {cnx.channel}!")

@commands.command()
async def register(cnx):
    add_guild(cnx.guild.id)
    await cnx.send("This guild is registered")

@commands.command()
async def makethislobby(cnx):
    set_channel(cnx.guild.id, cnx.channel.id)
    await cnx.send("This is a lobby channel now!")

@commands.command()
async def echorole(cnx, role):
    if get(cnx.guild.roles, name=role):
        resrole = get(cnx.guild.roles, name=role)
        await cnx.send(f'{resrole.id}: {role}')
    else:
        await cnx.send("Can't find such role :s")
    