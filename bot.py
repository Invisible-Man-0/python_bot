import telebot
from telebot import types

bot = telebot.TeleBot('TELEGRAM_BOT_TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('Привет! А ты кто?')
    btn2 = types.KeyboardButton('Да так, гулял, как раз собирался домой...')
    markup.row(btn1, btn2)
    
    with open('./the_beginning.mp4', 'rb') as file:
        bot.send_video(message.chat.id, file, reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def on_click(message):
    if message.text == 'Привет! А ты кто?':
        with open('./1-1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Меня Илья зовут')
        btn2 = types.KeyboardButton('А я тоже Генка! (соврать)')
        btn3 = types.KeyboardButton('Замечательно. Я, пожалуй, пойду домой...')
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, second_choice)

    elif message.text == 'Да так, гулял, как раз собирался домой...':
        with open('./1-2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Хм, ну покажи...')
        btn2 = types.KeyboardButton('Пошёл на***')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, second_choice)

    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def second_choice(message):
    if message.text == 'Меня Илья зовут':
        with open('./1-1-1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Ладно, я, пожалуй, пойду...')
        btn2 = types.KeyboardButton('Так чего ты там проводник?')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, third_choice_1_1)

    elif message.text == 'А я тоже Генка! (соврать)':
        with open('./1-1-2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Я правду говорю, я твой брат')
        btn2 = types.KeyboardButton('Генка-Гренка!')
        btn3 = types.KeyboardButton('Ладно, на самом деле, меня Илья зовут...')
        markup.row(btn1, btn2, btn3)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, third_choice_1_2)

    elif message.text == 'Замечательно. Я, пожалуй, пойду домой...':
        with open('./1-2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Хм, ну покажи...')
        btn2 = types.KeyboardButton('Пошёл на***')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, second_choice)
        
    elif message.text == 'Хм, ну покажи...':
        with open('./1-2-1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Это не зоопарк. Ты меня обманул')
        btn2 = types.KeyboardButton('А где зоопарк?')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, zoo_choice)
        
    elif message.text == 'Пошёл на***':
        with open('./1-2-2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Я сейчас полицию вызову!')
        btn2 = types.KeyboardButton('(уйти)')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, police_choice)
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def zoo_choice(message):
    if message.text in ['Это не зоопарк. Ты меня обманул', 'А где зоопарк?']:
        with open('./zoo_1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Куда ты меня завёл...')
        btn2 = types.KeyboardButton('Ты достал! Где зоопарк?!')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, bad_ending_choice)
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def bad_ending_choice(message):
    if message.text in ['Куда ты меня завёл...', 'Ты достал! Где зоопарк?!']:
        with open('./bad_ending.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper_bad_ending.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Плохая концовка - на вас совершено нападение в московском дворике. Если хотите переиграть, нажмите или пропишите /start")
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def police_choice(message):
    if message.text == 'Я сейчас полицию вызову!':
        with open('./police.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Что ты предлагаешь?')
        btn2 = types.KeyboardButton('Я звоню в полицию')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, police_follow_up)
    elif message.text == '(уйти)':
        with open('./strangulation.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper_strangulation.png', 'rb') as image:
            bot.send_photo(message.chat.id, image)
        bot.send_message(message.chat.id, 'Плохая концовка - Генка задушил вас. Если хотите переиграть, нажмите или пропишите /start')
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def police_follow_up(message):
    if message.text == 'Что ты предлагаешь?':
        with open('./police_1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Ладно, давай...')
        btn2 = types.KeyboardButton('Пошёл на*** дважды')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, police_final_choice)
    elif message.text == 'Я звоню в полицию':
        with open('./police_2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Плохая концовка - Генка отправил вас в нокаут. Если хотите переиграть, нажмите или пропишите /start")
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def police_final_choice(message):
    if message.text == 'Ладно, давай...':
        with open('./1-2-1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Это не зоопарк. Ты меня обманул')
        btn2 = types.KeyboardButton('А где зоопарк?')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, zoo_choice)
    elif message.text == 'Пошёл на*** дважды':
        with open('./police_2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Плохая концовка - Генка отправил вас в нокаут. Если хотите переиграть, нажмите или пропишите /start")
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def third_choice_1_1(message):
    if message.text == 'Ладно, я, пожалуй, пойду...':
        with open('./1-2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Хм, ну покажи...')
        btn2 = types.KeyboardButton('Пошёл на***')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, second_choice)
    elif message.text == 'Так чего ты там проводник?':
        with open('./lower_internet.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Впервые слышу')
        btn2 = types.KeyboardButton('Наслышан, да...')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, fourth_choice)

def fourth_choice(message):
    if message.text == 'Впервые слышу':
        with open('./lower_internet_1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Хм, ну покажи...')
        btn2 = types.KeyboardButton('Пошёл на***')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, second_choice)

    elif message.text == 'Наслышан, да...':
        with open('./lower_internet_2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Там издеваются над людьми и извращают их!')
        btn2 = types.KeyboardButton('Ну, там всякий шлак, туалетный юмор...')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, fifth_choice)

def fifth_choice(message):
    if message.text == 'Там издеваются над людьми и извращают их!':
        with open('./lower_internet_3.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Хм, ну покажи...')
        btn2 = types.KeyboardButton('Пошёл на***')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, second_choice)

    elif message.text == 'Ну, там всякий шлак, туалетный юмор...':
        with open('./lower_internet_3.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Хм, ну покажи...')
        btn2 = types.KeyboardButton('Пошёл на***')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, second_choice)

def third_choice_1_2(message):
    if message.text == 'Я правду говорю, я твой брат':
        with open('./fatal_error.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper_fatal_choice.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Плохая концовка - Генка выстрелил в вас, вы ранены. Если хотите переиграть, нажмите или пропишите /start")
    elif message.text == 'Генка-Гренка!':
        with open('./genka_1.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Генка-Гренка!')
        btn2 = types.KeyboardButton('Поведусь...')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, genka_choice_1)
    elif message.text == 'Ладно, на самом деле, меня Илья зовут...':
        with open('./he_will_come_to_you.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Ладно, я, пожалуй, пойду...')
        btn2 = types.KeyboardButton('Так чего ты там проводник?')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, third_choice_1_1)
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def genka_choice_1(message):
    if message.text == 'Генка-Гренка!':
        with open('./fatal_error.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper_fatal_choice.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Плохая концовка - Генка выстрелил в вас, вы ранены. Если хотите переиграть, нажмите или пропишите /start")
    elif message.text == 'Поведусь...':
        with open('./genka_2.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('Что...')
        btn2 = types.KeyboardButton('(молчание)')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, genka_choice_2)
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def genka_choice_2(message):
    if message.text == 'Что...':
        with open('./fatal_error.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper_fatal_choice.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Плохая концовка - Генка выстрелил в вас, вы ранены. Если хотите переиграть, нажмите или пропишите /start")
    elif message.text == '(молчание)':
        with open('./genka_3.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        btn1 = types.KeyboardButton('(напасть на Генку)')
        btn2 = types.KeyboardButton('Да, это я, брат')
        markup.row(btn1, btn2)
        bot.send_message(message.chat.id, 'Выберите один из вариантов:', reply_markup=markup)
        bot.register_next_step_handler(message, genka_choice_3)
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

def genka_choice_3(message):
    if message.text == '(напасть на Генку)':
        with open('./genka_4.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper_genka_choice.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Вы достигли единственной хорошей концовки, мы вас поздравляем! Если хотите переиграть, нажмите или пропишите /start")
    elif message.text == 'Да, это я, брат':
        with open('./fatal_error.mp4', 'rb') as file:
            bot.send_video(message.chat.id, file)
        with open('./newspaper_fatal_choice.png', 'rb') as file:
            bot.send_photo(message.chat.id, file, caption="Плохая концовка - Генка выстрелил в вас, вы ранены. Если хотите переиграть, нажмите или пропишите /start")
    else:
        bot.send_message(message.chat.id, 'Неизвестный выбор. Пожалуйста, выберите один из предложенных вариантов.')

bot.polling(none_stop=True)
