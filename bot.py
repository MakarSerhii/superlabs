from telegram import *
from telegram.ext import *
from parsing import selenium_parser, deleting_img


def code(update: Update, context: CallbackContext):
    """
    1.Taking the trading pair from user and give it to parser.
    2.Sending the photo to user in telegram.
    3.Deleting the image.
    """
    trading_pair = update.message.text
    selenium_parser(trading_pair)
    update.message.reply_photo(open("telegram_photo.jpg", "rb"))
    deleting_img()

def start(update, context):
    """
    Entry point
    """
    update.message.reply_text('Hello!')
    update.message.reply_text('Please enter your trading pair:')


updater = Updater("5958169582:AAHNe8yH_oHtMKRYZ0Wtj7mx6Ypq5hJTsSM", use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, code))
updater.start_polling()
updater.idle()
