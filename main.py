import telebot
import random
from my_token import token

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
butn1 = telebot.types.KeyboardButton('играть')
butn2 = telebot.types.KeyboardButton('нет')
keyboard.add(butn1, butn2)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_sticker(message.chat.id,
        'CAACAgIAAxkBAAI2x2S1PGnfcawfdYmAkM8yif3t7RnpAAJDAANEDc8XIqysVRZ-nWEvBA')
    msg = bot.send_message(message.chat.id, f'Привет {message.chat.first_name}начнем игру?', reply_markup=keyboard)


    bot.register_next_step_handler(msg, check_answer)

def check_answer(message):
    if message.text == 'играть':
        bot.send_message(message.chat.id,'ОК, тогда вот правила: нужно угодать число от 1 до 3 за 3 попытки' )
        random_number = random.randint(1,10)
        start_game(message, 3, random_number)
    else:
        bot.send_message(message.chat.id,'ладно')

def start_game(message, attemps,random_number):
    msg = bot.send_message(message.chat.id, 'Введи число')
    bot.register_next_step_handler(msg, check_number, attemps - 1, random_number)

def check_number(message, attempts, random_number):
    if message.text == str(random_number):
        bot.send_message(message.chat.id, 'Вы победили!')
        bot.send_photo(message.chat.id,'https://cdn5.vectorstock.com/i/1000x1000/67/24/winner-label-or-sticker-vector-28196724.jpg')
    elif attempts == 0:
        bot.send_message(message.chat.id, f'число было - {random_number}')
    else:
        bot.send_message(message.chat.id, f'Попробуйте еще раз, у вас осталось в количестве {attempts} попыток')
        start_game(message, attempts, random_number)
    

bot.polling()