import requests
import json
from telegram.ext import Updater, CommandHandler, MessageHandler
updater=Updater(token ='6079923149:AAFgDUMk_p-mTsDk26grmVU8K1L1SrWTWgU', use_context=True)
dispatcher = updater.dispatcher
def hello(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text='Hello, World')
hello_handler=CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
updater.start_polling()