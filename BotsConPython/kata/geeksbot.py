from telegram.ext import Updater, CommandHandler
def main():
    updater=Updater(token=open("../bot_token").read(), use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("repite",repite))
    updater.dispatcher.add_handler(CommandHandler("suma",suma))
    updater.dispatcher.add_handler(CommandHandler("stop",stop))
    updater.start_polling()
    updater.idle()

def start(update, context):
    update.message.reply_text("Hola soy un bot")

def repite(update, context):
    update.message.reply_text(update.message.text)

def suma(update, context):
    resultado = int(context.args[0]) + int(context.args[1])
    resultado = str(resultado)
    update.message.reply_text("El resultado es: " + resultado)

def stop(update, context):
    update.message.reply_text("parando el bot ")

main()