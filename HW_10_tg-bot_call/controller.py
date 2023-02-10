import telebot
import ma
import view



bot = telebot.TeleBot("5963003016:AAECdzyoEoCq3p5kUQIIc_3hakMckjUCooM")
res = 0.0
def coll(message):
    global res
    a = view.input_first_tg(message)
    sim = view.input_simvol(message)
    b = view.input_second_tg(message)
    print(f'a = {a}, b = {b}, sim = {sim}')


    if sim == '-':
        res = ma.sub_num(a, b)

    elif sim == '+':
        res = ma.sum_num(a, b)

    elif sim == '/':
        res = ma.div_num(a, b)

    elif sim == '*':
        res = ma.mult_num(a, b)

    elif sim == '%' and type(a) != complex and type(b) != complex:
        res = ma.div_rem_num(a, b)

    elif sim == '%' and (type(a) == complex or type(b) == complex):
        bot.send_message(message.chat.id, 'не выполнимое действие с комплексными числами!')

    elif sim == '//' and type(a) != complex and type(b) != complex:
        res = ma.div_int_num(a, b)

    elif sim == '//' and (type(a) == complex or type(b) == complex):
        bot.send_message(message.chat.id, 'не выполнимое действие с комплексными числами!')
    return res
