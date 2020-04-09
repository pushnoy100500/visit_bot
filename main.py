import telebot
import lib


bot = telebot.TeleBot(lib.get_token())

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    print(message)
    bot.reply_to(message, lib.greeting_message)


@bot.message_handler(commands=['add'])
def add_entry(message):
    address = message.text[5:]
    if (len(address) == 0):
        bot.send_message(message.chat.id, 'Provided address is empty')
    else:
        lib.save_address(message.from_user.id, address)
        bot.send_message(message.chat.id, '{} was added to your favourites!'.format(address))


bot.polling()
