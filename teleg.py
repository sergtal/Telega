import telebot

bot = telebot.TeleBot('5244110939:AAEA2U0RT8b3ybfaCS8vE_OMByfrbtxT4ik')

#comands

@bot.message_handler(commands=['start'])
def start(message): #содержимое пользователю
    mess = f'<b>Привет</b>, {message.from_user.first_name} {message.from_user.last_name}'
    bot.send_message(message.chat.id, mess, parse_mode='html')

#text

@bot.message_handler()
def get_user_text(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, {message.from_user.id}, parse_mode='html')
    else:  bot.send_message(message.chat.id, 'Я не понимаю', parse_mode='html')



bot.polling(none_stop=True)