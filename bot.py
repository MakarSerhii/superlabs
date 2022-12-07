from telegram import *
from telegram.ext import *
from parsing import selenium_parser


def code(update: Update, context: CallbackContext):
    trading_pair = update.message.text
    img = selenium_parser(trading_pair)


def start(update, context):
    update.message.reply_text('Hello!')
    update.message.reply_text('Please enter your trading pair:')


updater = Updater("5958169582:AAHNe8yH_oHtMKRYZ0Wtj7mx6Ypq5hJTsSM", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, code))
updater.start_polling()
updater.idle()
