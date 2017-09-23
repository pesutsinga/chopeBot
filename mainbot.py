from pprint import pprint
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from time import gmtime, strftime
import chopeDB
import datetime
import logging

FIRST_ONLINE = ''
USER_STATUS = {}
TOKEN = '377140861:AAEiMIj-VOwB68HcftvMILjr5wc6LJJml6g'


def assert_error(bot, update):
    chatID = update.message.chat_id
    text = "Last bot restart: " + FIRST_ONLINE + "Please redo /start"
    bot.send_message(chat_id=chatID, text=text)


def assert_no_username(bot, update):
    chatID = update.message.chat_id
    text = "mirna pls.\nset username in your settings"
    bot.send_message(chat_id=chatID, text=text)


def ask_username():
    pass


def abc():
    print("AKLS")


def start(bot, update, args):
    chatID = update.message.chat_id
    firstName = update.message.from_user.first_name
    username = update.message.from_user.username
    if username != "None":
        bot.send_message(chat_id=chatID, text="Hi " + firstName)
        from emoji import emojize
        button_list = [
            [InlineKeyboardButton("col1", callback_data="abc"),
             InlineKeyboardButton("col2", callback_data="def")],
            [InlineKeyboardButton("row 2", callback_data="ghi")]
        ]
        reply_markup = InlineKeyboardMarkup(button_list)
        bot.send_message(
            chat_id=chatID,
            text="A two-column menu",
            reply_markup=reply_markup)
    else:
        assert_no_username(bot, update)


# Depressed on the def thingy
# def clbk(bot, update):
#     print(update)


def init_handler(dispatcher):
    cmd_start = CommandHandler('start', start, pass_args=True)
    dispatcher.add_handler(cmd_start)
    # MEMO: Belom bisa figure out the how to
    # callback_handler = MessageHandler(callback)
    # dispatcher.add_handler(callback_handler, clbk)


def main():
    FIRST_ONLINE = strftime("%d %b %Y %H:%M:%S", gmtime())
    loggingFormat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=loggingFormat, level=logging.INFO)

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    init_handler(dispatcher)
    print("BOT Finishing Init")
    updater.start_polling()
    print("Bot Properly Started")

if __name__ == "__main__":
    main()
