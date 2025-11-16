import telebot
from settings import TG_API_TOKEN

bot = telebot.TeleBot(TG_API_TOKEN)

# Обработчик команды
@bot.message_handler(commands=['start'])  # /start
def start_command(message):
    bot.send_message(message.chat.id, 'Привет! Я твой бот.')

# Обработчик типа сообщения
@bot.message_handler(content_types=['sticker'])  # ['audio', 'photo', 'video', 'document', 'text', 'location', 'contact', 'sticker']
def handle_sticker(message):
    bot.reply_to(message, 'О, классный стикер!')

bot.infinity_polling()  # или bot.polling()