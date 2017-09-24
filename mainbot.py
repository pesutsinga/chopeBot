from pprint import pprint
import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackQueryHandler
from time import gmtime, strftime
import chopeDB
import datetime
import logging

FIRST_ONLINE = ''
USER_STATUS = {}
TOKEN = '377140861:AAEiMIj-VOwB68HcftvMILjr5wc6LJJml6g'
VERBOSE = False


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


def vprint(obj):
    if VERBOSE:
        print(obj)


def cmd_start(bot, update, args):
    VERBOSE = args == 'v'
    chatID = update.message.chat_id
    firstName = update.message.from_user.first_name
    username = update.message.from_user.username

    vprint("username check")
    if username == "None":
        vprint("FAIL")
        assert_no_username(bot, update)
        return
    vprint("PASS")

    vprint("login check")
    if not can_login():
        vprint("FAIL")
        push_user()
    vprint("PASS")

    bot.send_message(chat_id=chatID, text="Hi " + firstName)
    if not verify_credential(username, chatID)


# Depressed on the def thingy
def callback_general(bot, update):
    print(update)


def handler_init(dispatcher):
    cmdStart = CommandHandler('start', cmd_start, pass_args=True)
    dispatcher.add_handler(cmdStart)
    callbackGeneral = CallbackQueryHandler(callback_general)
    dispatcher.add_handler(callbackGeneral)
    # MEMO: Belom bisa figure out the how to
    # callback_handler = MessageHandler(callback)
    # dispatcher.add_handler(callback_handler, clbk)


def main():
    FIRST_ONLINE = strftime("%d %b %Y %H:%M:%S", gmtime())
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher
    handler_init(dispatcher)
    print("deploying bot...")
    updater.start_polling()
    print("deployed")

if __name__ == "__main__":
    main()
