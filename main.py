from transliterate import to_cyrillic, to_latin
import telebot

bot = telebot.TeleBot(
    "5921180814:AAG00ZMbtMoMxCEjOH-cOOtgW_Vf6uis2a4", parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! Xush kelibsiz")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(
        message, "Assalomu alaykum! Sizda bot ishlashi bo'yicha muammo bo'lyaptimi?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    def javob(msg): return to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    # if msg.isascii():
    #     javob = to_cyrillic(msg)
    # else:
    #     javob = to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()
