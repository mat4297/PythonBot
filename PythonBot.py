#pip install aiogram https: // github.com/aiogram/aiogram
#pip install pytelegrambotapi --upgrade https://github.com/eternnoir/pyTelegramBotAPI
#pip install python-telegram-bot --upgrade https://github.com/python-telegram-bot/python-telegram-bot
#uso la prima libreria
#https://aiogram.readthedocs.io/en/latest/quick_start.html

import logging

from aiogram import Bot, Dispatcher, executor, types

#
API_TOKEN = '681592485:AAH_VkUoMQFzzXrc7HfZVf90lm58ERN4nVo'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")

#If you want to handle all messages in the chat simply add handler without filters:
#@dp.message_handler()
#async def echo(message: types.Message):
#    await bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
