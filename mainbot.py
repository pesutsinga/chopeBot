from pprint import pprint
from telegram.ext import Updater, CommandHandler
from time import gmtime, strftime
import chopeDB
import datetime
import logging

def assert_error(bot, update):
    chat_id = update.message.chat_id
    text = "Last bot restart: " + curTime + "Please redo /start"
    bot.send_message(chat_id=chat_id, text=text)

def assert_no_username(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="mirna pls.\nset username in settings")

def start(bot, update, args):
    chat_id = update.message.chat_id
    name = update.message.from_user.first_name
    if uname != "None":
        bot.send_message(chat_id=update.message.chat_id, text="Hi " name)
    else:
        assert_no_username(bot, update)

    if not chopeDB.correct_credential(update.message.chat_id):
        print

def initHandler():
    cmd_start = CommandHandler('start', start, pass_args=True)
    dispatcher.add_handler(cmd_start)
    
def main():
    startTime = strftime("%d %b %Y %H:%M:%S", gmtime())
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    
    updater = Updater(token='377140861:AAEiMIj-VOwB68HcftvMILjr5wc6LJJml6g')
    dispatcher = updater.dispatcher
    
    updater.start_polling()

if __name__ == "__main__":
    main()
