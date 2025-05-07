import telebot
from Config import keys, TOKEN
from Extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу, введите команду боту  в следующем фомате:\n<имя валюты, цену на которую надо узнать> \
<имя валюты, цену в которой надо узнать> <количество переводимой валюты>\nУвдеть список всех доступных валют: /values'
    (bot.reply_to(message, text))

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
       text = '\n'.join((text,key,))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def get_price (message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Неверное количество параметров.')

        base, quote, amount = values
        amount = float(amount)
        total_base = CryptoConverter.get_price(base, quote, amount)


    except APIException as e:
        bot.reply_to(message,f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} = {total_base} {quote} '
        bot.send_message(message.chat.id, text)


bot.polling()