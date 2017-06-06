from telegram.ext import Updater, CommandHandler

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def yo(bot,update):
	update.message.reply_text(
		'Yo! {}'.format(update.message.from_user.first_name))

def photo(bot, update):
    file_id = update.message.photo[-1]
    newFile = bot.getFile(file_id)
    newFile.download('test.jpg')
    bot.sendMessage(chat_id=update.message.chat_id, text="download succesfull")

updater = Updater('340664104:AAG3RpwP4maWNbO2FtTCu2xqvGGFLU_F2Xs')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('yo',yo))
updater.dispatcher.add_handler(CommandHandler('photo',photo))

updater.start_polling()
updater.idle()