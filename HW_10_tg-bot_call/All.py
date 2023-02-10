import telebot
import ma
import xlsxwriter
import datetime as dt

bot = telebot.TeleBot("5963003016:AAECdzyoEoCq3p5kUQIIc_3hakMckjUCooM")

a = 0
b = 0
sim = ''
res = 0
log = ''

@bot.message_handler(commands=["start"])
def start(message):
    global log
    log = open('c:/gb/Python_second_block/HW_10_tg-bot_call/log.txt', 'a')
    mrk = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = telebot.types.KeyboardButton("натуральные числа")
    key2 = telebot.types.KeyboardButton("комплексные числа")
    mrk.add(key1)
    mrk.add(key2)
    bot.send_message(message.chat.id, "если хотите работать с натуральными числами, нажмите 'натуральные числа',\
 если работать с комплексными числами, нажмите 'комплексные числа'", reply_markup=mrk)
    bot.register_next_step_handler(message,calculator)


def calculator(message):
    global otvet
    if message.text == 'натуральные числа':
        nut(message)
    elif message.text == "комплексные числа":
        com(message)
    else:
        start('/start')

def nut(message):
    bot.send_message(message.chat.id, "Введите первое число: ")
    bot.register_next_step_handler(message, add_a)


def add_a(message):
    global a
    a = int(message.text)
    bot.send_message(message.chat.id, 'Введите символ операции: ')
    bot.register_next_step_handler(message, add_sim)


def add_sim (message):
    global sim
    sim = message.text
    bot.send_message(message.chat.id, 'Введите второе число: ')
    bot.register_next_step_handler(message, add_b)


def add_b (message):
    global b
    b = int(message.text)
    matt_nut(a, b, sim, message)


def matt_nut(a, b, sim, message):
    global otvet
    if sim == '-':
        otvet = ma.sub_num(a, b)

    elif sim == '+':
        otvet = ma.sum_num(a, b)

    elif sim == '/':
        otvet = ma.div_num(a, b)

    elif sim == '*':
        otvet = ma.mult_num(a, b)

    elif sim == '%':
        otvet = ma.div_rem_num(a, b)

    elif sim == '//':
        otvet = ma.div_int_num(a, b)
    bot.send_message(message.chat.id, f"ответ = {otvet}")

    log.writelines(f'\n{message.from_user.first_name} {message.from_user.last_name} id = {message.chat.id}\n')

    log.close()


def com(message):
    bot.send_message(message.chat.id, "Введите первое число: ")
    bot.register_next_step_handler(message, add_a_com)


def add_a_com(message):
    global a
    a = complex(message.text)
    bot.send_message(message.chat.id, 'Введите символ операции: ')
    bot.register_next_step_handler(message, add_sim_com)
    print(a)
    print(type(a))


def add_sim_com (message):
    global sim
    sim = message.text
    bot.send_message(message.chat.id, 'Введите второе число: ')
    bot.register_next_step_handler(message, add_b_com)


def add_b_com(message):
    global b
    b = complex(message.text)
    matt_com(a, b, sim, message)


def matt_com(a, b, sim, message):
    global otvet
    if sim == '-':
        otvet = ma.sub_num(a, b)

    elif sim == '+':
        otvet = ma.sum_num(a, b)

    elif sim == '/':
        otvet = ma.div_num(a, b)

    elif sim == '*':
        otvet = ma.mult_num(a, b)

    elif sim == '%' and type(a) != complex and type(b) != complex:
        otvet = ma.div_rem_num(a, b)

    elif sim == '%' and (type(a) == complex or type(b) == complex):
        bot.send_message(message.chat.id, 'не выполнимое действие с комплексными числами!')

    elif sim == '//' and type(a) != complex and type(b) != complex:
        otvet = ma.div_int_num(a, b)

    elif sim == '//' and (type(a) == complex or type(b) == complex):
        bot.send_message(message.chat.id, 'не выполнимое действие с комплексными числами!')
    bot.send_message(message.chat.id, f"ответ = {otvet}")

    log.writelines(f'{message.from_user.first_name} {message.from_user.last_name} id = {message.chat.id}\n')


    log.close()


bot.infinity_polling()