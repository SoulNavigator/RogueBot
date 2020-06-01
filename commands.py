from discord.ext import commands
from discord.utils import get
from datamanager import add_guild, add_lobby, remove_guild, set_member, get_member, set_rules, get_rules

yes_emoji = '\U0001F44D'
no_emoji =  '\U0001F44E'

@commands.command()
async def makelobby(ctx, *, rules):
    try:
        add_lobby(ctx.guild.id, ctx.channel.id)
        set_rules(ctx.guild.id, rules)
        await ctx.send("This channel is lobby now!")
        await ctx.send("Here the rules:")
        await ctx.send(f"```{rules}```")
        await ctx.send("If you accept, type '-!join' for members or '-!guest' for guests")
    except Exception as error:
        await ctx.send(str(error))
    

@commands.command()
async def makemember(ctx, role):
    member_role = get(ctx.guild.roles, name=role)
    if member_role:
        set_member(ctx.guild.id, member_role.id)
        await ctx.send(f"{member_role} is now a member role!")



""" EVENTS """   
async def on_guild_join(guild):
    add_guild(guild.id, guild.name)

async def on_guild_remove(guild):
    remove_guild(guild.id)
    
async def on_message(msg):
    channel = msg.channel
    content = msg.content
    guild = msg.guild
    rules = get_rules(guild.id)
    if rules in content and msg.author.bot:
        print(msg.guild.name)
        await msg.add_reaction(yes_emoji)
        await msg.add_reaction(no_emoji)

async def on_reaction_add(reaction, author):
    if not author.bot:
        content = reaction.message.content
        guild = reaction.message.guild
        member_role = get(guild.roles, id=get_member(guild.id))
        rules = get_rules(guild.id)

        if rules in content:
            if reaction.emoji==yes_emoji:
                print("It's a yes emoji")
                await reaction.remove(author)
                await author.add_roles(member_role)
            if reaction.emoji==no_emoji:
                print("It's a no emoji")
                await reaction.remove(author)