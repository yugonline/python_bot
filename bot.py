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
	update.message.reply_text("Hi!")
	user = update.message.from_user
	if update.message.photo:
		update.message.reply_text("Thinking hard...")
		photo_id = update.message.photo[-1].file_id
		photo_file = bot.getFile(photo_id)
		photo_file.download()
def linkgrab(bot,update):
	Image_Response = updater.dispatcher.add_handler(MessageHandler(Filters.photo,get_input))
	update.message.reply_text(
		'{} please upload an image now'.format(update.message.from_user.first_name))

def main():
	secret_key_file = open("secret_key.txt").readlines()
	updater = Updater(secret_key_file[0].strip())

	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('hello', hello))
	updater.dispatcher.add_handler(CommandHandler('yo',yo))
	updater.dispatcher.add_handler(CommandHandler('linkgrab',linkgrab))


	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()