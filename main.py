import telebot

bot = telebot.TeleBot('6856288990:AAG55MiJNSJtiTdjqJwn1iAghnU6Th5hFkk')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'я тебя да')


@bot.message_handler(commands=['love'])
def main(message):
    bot.send_message(message.chat.id, 'как дела? \nчто делаешь?')


@bot.message_handler(commands=['rimus'])
def main(message):
    bot.send_message(message.chat.id, '*я устал*', parse_mode='Markdown')


@bot.message_handler(commands=['link'])
def main(message):
    bot.send_message(message.chat.id, '[ЭТО ССЫЛКА](https://pastebin.com/)', parse_mode='Markdown')


bot.infinity_polling()