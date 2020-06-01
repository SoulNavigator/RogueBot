from discord.ext import commands
from discord.utils import get
from datamanager import add_guild, add_lobby, remove_guild

rules = "Rule 1: Don't be a dick \n" + "Rule 2: Have fun"

yes_emoji = '\U0001F44D'
no_emoji =  '\U0001F44E'

@commands.command()
async def makelobby(ctx):
    try:
        add_lobby(ctx.guild.id, ctx.channel.id)
        
        await ctx.send("This channel is lobby now!")
        await ctx.send("Here the rules:")
        await ctx.send(f"```{rules}```")
        await ctx.send("If you accept, type '-!join' for members or '-!guest' for guests")
    except Exception as error:
        await ctx.send(str(error))
    
async def on_guild_join(guild):
    add_guild(guild.id, guild.name)

async def on_guild_remove(guild):
    remove_guild(guild.id)
    
async def on_message(msg):
    channel = msg.channel
    content = msg.content

    if rules in content:
        print(msg.guild.name)
        await msg.add_reaction(yes_emoji)
        await msg.add_reaction(no_emoji)