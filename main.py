import telebot
from lib import get_token, greeting_message, Storage


bot = telebot.TeleBot(get_token())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, greeting_message)


@bot.message_handler(commands=['add'])
def add_entry(message):
    address = message.text[5:]
    if (len(address) == 0):
        bot.send_message(message.chat.id, 'Provided address is empty')
    else:
        storage = Storage.get_instance()
        storage.add_address(message.from_user.id, address)
        bot.send_message(message.chat.id, '{} was added to your favourites!'.format(address))


@bot.message_handler(commands=['list'])
def list_entries(message):
    storage = Storage.get_instance()
    listings = storage.get_address_listings(message.from_user.id)
    listings = map(lambda l: l.decode('utf-8'), listings)
    bot.send_message(message.chat.id, 'Listings:\n - {}'.format('\n - '.join(listings)))


@bot.message_handler(commands=['reset'])
def reset_entries(message):
    storage = Storage.get_instance()
    storage.reset_address_listings(message.from_user.id)
    bot.send_message(message.chat.id, 'Your listings have been cleared.')


if __name__ == "__main__":
    bot.polling()
