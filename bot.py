from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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
def get_input(bot,update):
	user = update.message.from_user
	if update.message.photo:
		update.message.reply_text("Thinking hard...")
		photo_id = update.message.photo[-1].file_id
		photo_file = bot.getFile(photo_id)
		photo_file.download()

updater = Updater('340664104:AAG3RpwP4maWNbO2FtTCu2xqvGGFLU_F2Xs')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('yo',yo))
updater.dispatcher.add_handler(MessageHandler(get_input))

updater.start_polling()
updater.idle()