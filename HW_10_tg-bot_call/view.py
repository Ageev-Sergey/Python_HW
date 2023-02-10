import telebot
import time
bot = telebot.TeleBot("5963003016:AAECdzyoEoCq3p5kUQIIc_3hakMckjUCooM")

znk = ''
a = 0
b = 0

def input_a (message):
    global a
    print(f'aa = {a}')
    print(f'message.text = {message.text}')
    a = int(message.text)
    print(f'aa = {a}')

def input_second(message):
    global b
    print(f'aa = {b}')
    print(f'message.text = {message.text}')
    b = int(message.text)
    print(f'aa = {b}')

def Operacion(message):
    global znk
    print('хаха')
    znk = message.text


def input_first_tg(message):
    global a
    bot.send_message(message.chat.id, 'введите первое число')
    bot.register_next_step_handler(message, input_a)
    time.sleep(10)
    print(f' a = {a}')
    return a

def input_simvol(message):
    global znk
    simvol = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("+")
    key2 = telebot.types.KeyboardButton("-")
    key3 = telebot.types.KeyboardButton("*")
    key4 = telebot.types.KeyboardButton("/")
    key5 = telebot.types.KeyboardButton("//")
    key6 = telebot.types.KeyboardButton("%")
    simvol.add(key1)
    simvol.add(key2)
    simvol.add(key3)
    simvol.add(key4)
    simvol.add(key5)
    simvol.add(key6)
    bot.send_message(message.chat.id, "выберите символ", reply_markup=simvol)
    bot.register_next_step_handler(message, Operacion())
    time.sleep(10)
    print(f'znk = {znk}')


def input_second_tg(message):
    global b
    bot.send_message(message.chat.id, 'введите второе число')
    bot.register_next_step_handler(message, input_second)
    time.sleep(10)
    print (f' b = {b}')
    return b