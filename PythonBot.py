#https://pypi.org/project/python-telegram-bot/
#https://pypi.org/project/urllib3/
#https://pypi.org/project/beautifulsoup4/

# https://github.com/python-telegram-bot/python-telegram-bot/tree/259a1faedc92878e6ed3da537f3facdfafefebee e https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.commandhandler.html
# https://pypi.org/project/python-telegram-bot/
from telegram.ext import CommandHandler
from telegram.ext import Updater
updater = Updater(
    token='681592485:AAHzuV5bqWpShFgjcyy6u6ALZ86YCIHg8Bk', use_context=True)
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(
        chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


