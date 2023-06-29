import telebot
from random import randint

text_game1 = 'Правила игры:\nЯ загадываю число от 1 до 1000, а ты должен угадать это число.\nЕсли не угадаешь, то я подскажу больше или меньше моё число, чем твоё. Попыток 10.\nПоехали!\n '
x = 1
i = 1
flag = False

bot = telebot.TeleBot('')

def game_over(flag,x,message_chat_id):
    if flag:
        bot.send_message(message_chat_id, 'Победа. Пока!')
    else:
        bot.send_message(message_chat_id, 'Поражение. Моё число ' + str(x) + ' . Удачи в следующий раз!')

@bot.message_handler(commands=['new_game'])
def start_funk(message):
    bot.send_message(message.chat.id, text_game1)
    global i
    global x
    global flag
    i = 1
    x = randint(1,1000)
    flag = False
    bot.send_message(message.chat.id, 'Твоя ' + str(i) + '-ая попытка(введи число): ')
    bot.register_next_step_handler(message, cirkl)

def cirkl(message):
    global i
    global x
    global flag
    try:
        y = int(message.text)
        if i < 11:
            if y == x:
                bot.send_message(message.chat.id, 'НЕРЕАЛЬНО! Ты угадал! Я загадал число '+str(x)+'!')
                flag = True
                game_over(flag,x,message.chat.id)
            else:
                if x > y:
                    bot.send_message(message.chat.id, 'Нет. Моё число больше')
                if x < y:
                    bot.send_message(message.chat.id, 'Нет. Моё число меньше')
                i += 1
                if i < 11:
                    bot.send_message(message.chat.id, 'Твоя ' + str(i) + '-ая попытка(введи число): ')
                    bot.register_next_step_handler(message, cirkl)
                else:
                    game_over(flag,x,message.chat.id)
        else:
            game_over(flag,x,message.chat.id)
    except:
        bot.send_message(message.chat.id, 'Это не число!')
        bot.send_message(message.chat.id, 'Твоя ' + str(i) + '-ая попытка(введи число): ')
        bot.register_next_step_handler(message, cirkl)
@bot.message_handler()
def spum(message):
    bot.send_message(message.chat.id, 'Я не понимаю, зачем ты это пишешь. Если хочешь поиграть напиши команду  "/new_game".')

bot.polling(none_stop=True)
