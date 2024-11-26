# import telebot
from telebot import TeleBot

bot = TeleBot('7957916743:AAGKnPw3VKoMCziA_Qdokqt19dyhbov2VV4')


# обработка новой команды
@bot.message_handler(commands=['start'])
def botic(message):
    bot.send_message(message.chat.id, 'Привет, рада тебя видеть!')  # отправь сообщение чат id,сообщение


@bot.message_handler(commands=['candy'])
def botic_1(message):
    bot.send_message(message.chat.id,
                     'https://dzen.ru/a/Xx6maLxWg1QMdK6W?ysclid=m3xaedpiwb797847465')  # отправь сообщение чат id,сообщение


@bot.message_handler(commands=['how_many'])
def botic_2(message):
    bot.send_message(message.chat.id, 'Наши вкусные конфеты стоят *1000* рублей',
                     parse_mode='Markdown')  # отправь сообщение чат id,сообщение


@bot.message_handler(commands=['where_to_buy'])
def botic_3(message):
    bot.send_message(message.chat.id,
                     'на нашем сайте: https://lux-candy.ru/eng?ysclid=m3xebfem3f500289358')  # отправь сообщение чат id,сообщение


@bot.message_handler(commands=['goodbye'])
def botic_4(message):
    bot.send_message(message.chat.id, '_До свидания,\n заходи еще_',
                     parse_mode='Markdown')  # отправь сообщение чат id,сообщение


bot.infinity_polling()