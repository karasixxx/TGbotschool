import telebot

bot = telebot.TeleBot('6901625503:AAFkL8SuPy541zLCiFvCRuFJImL0Ww6JQU8')

@bot.message_handler()
def main(msg):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    but1 = telebot.types.InlineKeyboardButton('first', callback_data='first')
    but2 = telebot.types.InlineKeyboardButton('second', callback_data='second')
    markup.add(but1, but2)

    bot.send_message(msg.chat.id, 'choose', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'first':
            bot.send_message(call.message.chat.id, 'первое сообщение')
        if call.data == 'second':
            bot.send_message(call.message.chat.id, 'второе сообщение')


bot.infinity_polling()
