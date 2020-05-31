import discord
from discord.ext.commands import Bot
import commands

class RogueBot(Bot):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
    
# All bot's commands here
def __commands(bot : RogueBot):
    bot.add_command(commands.sayhello)
    bot.add_command(commands.register)

def runbot(token, prefix):
    bot = RogueBot(command_prefix=prefix)
    __commands(bot)

    bot.run(token)