import telebot
import controller

bot = telebot.TeleBot("5963003016:AAECdzyoEoCq3p5kUQIIc_3hakMckjUCooM")

flag = 1
otvet = 0
a = 0
b = 0
sim = ''

@bot.message_handler(commands=["start"])
def start(message):
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
        controller.coll(message.chat.id)
    else:
        start('/start')



bot.infinity_polling()
