import telebot
from telebot import types

bot = telebot.TeleBot('7076862024:AAFP0rijMMQJFeh9waQ_rDVFL03tKZGA67k')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помошник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('Low')
        btn2 = types.KeyboardButton('High')
        btn3 = types.KeyboardButton('Custom')
        btn4 = types.KeyboardButton('History')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вас вопрос', reply_markup=markup) #ответ бота

    elif message.text == 'Low':
        bot.send_message(message.from_user.id, 'Выдает минимальное значение', parse_mode='Markdown')

    elif message.text == 'High':
        bot.send_message(message.from_user.id, 'Выдает максимальное значение', parse_mode='Markdown')

    elif message.text == 'Custom':
        bot.send_message(message.from_user.id, 'Выдает кастомный ответ', parse_mode='Markdown')

    elif message.text == 'History':
        bot.send_message(message.from_user.id, 'Показывает историю запросов', parse_mode='Markdown')


bot.polling(none_stop=True, interval=0) #обязательная для работы бота часть