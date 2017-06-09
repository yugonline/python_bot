from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from vision import detect_text_uri

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def yo(bot,update):
	update.message.reply_text(
		'Yo! {}'.format(update.message.from_user.first_name))

def get_input(bot,update):
	print("get_input")
	user = update.message.from_user
	if update.message.photo:
		print("is a photo")
		update.message.reply_text("Thinking hard...")

		# path = "test.jpg"
		# update.message.reply_text(str(vision.detect_text(path)))
		photo_id = update.message.photo[-1].file_id
		print(photo_id)
		photo_file = bot.getFile(photo_id)
		ID = photo_file.file_path
		url = detect_text_uri(ID)
		url_string = ' '.join(url)
		update.message.reply_text(url_string)

		

def linkgrab(bot,update):
	update.message.reply_text(
		'{}! I am up for grabs.'.format(update.message.from_user.first_name))
def help(bot,update):
	update.message.reply_text('{} Please send an image that contains URLs so I can extract the URLs and send them back to you!'.format(update.message.from_user.first_name))

def main():
	secret_key_file = open("secret_key.txt").readlines()
	updater = Updater(secret_key_file[0].strip())

	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(CommandHandler('hello', hello))
	updater.dispatcher.add_handler(CommandHandler('yo',yo))
	updater.dispatcher.add_handler(CommandHandler('linkgrab',linkgrab))
	updater.dispatcher.add_handler(CommandHandler('help',help))
	updater.dispatcher.add_handler(MessageHandler(Filters.photo,get_input))


	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()