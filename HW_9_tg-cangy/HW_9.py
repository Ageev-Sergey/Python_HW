import telebot
from telebot import types
import time


bot = telebot.TeleBot("5963003016:AAECdzyoEoCq3p5kUQIIc_3hakMckjUCooM")
a = 0


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "\
Условие задачи: На столе лежит 221 конфета.\
Играют два игрока делая ход друг после друга.\
За один ход можно забрать не более чем 28 конфет.\
Все конфеты оппонента достаются сделавшему последний ход.")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Начать игру")
    but2 = types.KeyboardButton("Выйти")
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, "Выбери ниже", reply_markup=markup)


@bot.message_handler(content_types="text")
def controller(message):
    candy = 221
    if message.text == "Начать игру":
        bot.send_message(message.chat.id, "на столе 221 конфета")


        def Step_first_plaer(x):
            global a
            bot.send_message(message.chat.id, f'напишите сколько хотите взять конфет со стола, не меньше 1 и не больше 28')
            time.sleep(10)
            bot.register_next_step_handler(message, call)
            first_plaer = a
            if first_plaer > 0 and first_plaer < 29:
                x -= first_plaer
                if x > 0:
                    bot.send_message(message.chat.id,f"осталось {x} конфет")
                if x <= 0:
                    bot.send_message(message.chat.id,"Выиграл первый игрок!")
            else:
                bot.send_message(message.chat.id,"Невозможное значение, введите целое число от 1 до 28!")
                Step_first_plaer(x)
            return x


        def Step_comp_plaer(x):
            if x <= 28:
                bot.send_message(message.chat.id,f"бот взял {x} конфет")
                x -= x
            else:
                a = x
                a %= 28
                if a > 1:
                    x -= a - 1
                    bot.send_message(message.chat.id,f"бот взял {a - 1} конфет")
                elif a == 0:
                    x -= 27
                    bot.send_message(message.chat.id,f"бот взял {27} конфет")
                else:
                    x -= 1
                    bot.send_message(message.chat.id,f"бот взял {1} конфет")
            if x == 0:
                bot.send_message(message.chat.id,"Бот выиграл, осталось 0 конфет")
            else:
                bot.send_message(message.chat.id,f"бот походил осталось {x} конфет")
            return x


        def One_plaer(x):
            while x > 0:
                print()
                x = Step_first_plaer(x)
                print()
                x = Step_comp_plaer(x)

        One_plaer(candy)


def call(message):
    global a
    a = int(message.text)

bot.infinity_polling()
