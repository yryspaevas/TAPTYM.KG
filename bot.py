import telebot
from decouple import config
from telebot import types

token = config('TOKEN')
bot = telebot.TeleBot(token)    

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇰🇬 Кыргыз Тили')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇰🇬 Тилди тандаңыз", reply_markup=markup)

@bot.message_handler(func=lambda x:True)
def reply_to_button(message):

    if message.text == '🇷🇺 Русский':
        markup = types.InlineKeyboardMarkup()
        btn4 = types.InlineKeyboardButton(text='Наш сайт', url='http://34.123.240.158/')
        markup.add(btn4)
        bot.send_message(message.from_user.id, "По кнопке ниже можно перейти на сайт TAPTYM.KG", reply_markup = markup)
        markup = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text="Еда", url='http://34.123.240.158/place/')
        btn6 = types.InlineKeyboardButton(text='Размещение', url='http://34.123.240.158/hotel/')
        btn7 = types.InlineKeyboardButton(text='Развлечение', url='http://34.123.240.158/fun/')
        markup.add(btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выберите категорию, которая вас интересует", reply_markup=markup)

    elif message.text == '🇰🇬 Кыргыз Тили':
        markup = types.InlineKeyboardMarkup()
        btn3 = types.InlineKeyboardButton(text='Биздин сайт', url='http://34.123.240.158/')
        markup.add(btn3)
        bot.send_message(message.from_user.id, "Сайтка өтүү үчүн төмөнкү баскычты басыңыз TAPTYM.KG", reply_markup = markup)
        markup = types.InlineKeyboardMarkup()
        btn5 = types.InlineKeyboardButton(text="Тамак", url='http://34.123.240.158/place/')
        btn6 = types.InlineKeyboardButton(text='Турак жай', url='http://34.123.240.158/hotel/')
        btn7 = types.InlineKeyboardButton(text='Көңүл ачуу', url='http://34.123.240.158/fun/')
        markup.add(btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Сизди кызыктырган категорияны тандаңыз", reply_markup=markup)
    else:
        bot.send_message(message.id,'Click on the button')
        bot.register_next_step_handler(message,reply_to_button)

    
 
bot.polling(none_stop=True, interval=0)
