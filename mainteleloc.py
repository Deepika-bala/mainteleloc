from telegram import *
import constants as keys
from telegram.ext import *

import responses as r

print("bot started..")


def start_command(update, context):
    update.message.reply_text("WELCOME")


def help_command(update, context):
    update.message.reply_text("need help? wait for response ")
def sendlocation_command(bot,context, chatId=None, latitude=None, longitude=None, title=None, address=None):
    bot.send_message(
            context.sendVenue({chatId: '@mdustartup_bot', latitude: 9.940739, longitude: 78.131510, title: 'CLOUDFLOOR',
                               address: '3B,NMR Subburaman Road, Chinna Chokikulam, Tamil Nadu 625002'}))

def handle_message(update,context ):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"update{update} caused error {context.error}")


def main():
    updater = Updater(keys.API_key, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
