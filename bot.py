from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import vision

def start(bot, update):
    update.message.reply_text('Hello World!')

def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def yo(bot,update):
	update.message.reply_text(
		'Yo! {}'.format(update.message.from_user.first_name))

def photo(bot, update):
	print("Photo")
	file_id = update.message.photo[-1]
	newFile = bot.getFile(file_id)
	newFile.download('test.jpg')
	bot.sendMessage(chat_id=update.message.chat_id, text="download succesfull")


def get_input(bot,update):
	print("get_input")
	update.message.reply_text("Hi!")
	user = update.message.from_user
	if update.message.photo:
		update.message.reply_text("Thinking hard...")
		# path = "test.jpg"
		# update.message.reply_text(str(vision.detect_text(path)))
		photo_id = update.message.photo[-1].file_id
		photo_file = bot.getFile(photo_id)
		photo_file.download()

def linkgrab(bot,update):
	try : 
		txt = MessageHandler(Filters.photo,get_input)
		Image_Response = updater.dispatcher.add_handler(txt)
	except:
		print "error"

	print("Replying : ")
	update.message.reply_text(
		'{}! I am up for grabs.'.format(update.message.from_user.first_name))


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