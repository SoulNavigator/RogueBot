import discord
from discord.ext.commands import Bot
import commands

class RogueBot(Bot):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')



    
# All bot's commands here
def __commands(bot : RogueBot):
    bot.add_command(commands.makelobby)
    bot.add_command(commands.makemember)

    bot.add_listener(commands.on_guild_join)
    bot.add_listener(commands.on_guild_remove)
    bot.add_listener(commands.on_message)
    bot.add_listener(commands.on_reaction_add)


def runbot(token, prefix):
    bot = RogueBot(command_prefix=prefix)
    __commands(bot)

    bot.run(token)