from bot import runbot
import config
from datamanager import init

if __name__ == "__main__":
    init()
    runbot(config.BOT_TOKEN, config.COMMAND_PREFIX)