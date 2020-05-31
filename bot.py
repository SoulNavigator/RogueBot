import discord
from discord.ext.commands import Bot
import commands

class RogueBot(Bot):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')



    
# All bot's commands here
def __commands(bot : RogueBot):
    bot.add_command(commands.helpme)
    bot.add_command(commands.makelobby)

    bot.add_listener(commands.on_guild_join)
    bot.add_listener(commands.on_guild_remove)


def runbot(token, prefix):
    bot = RogueBot(command_prefix=prefix)
    """
    @bot.event
    async def on_guild_join(guild):
        print("hello")
    """
    __commands(bot)

    bot.run(token)