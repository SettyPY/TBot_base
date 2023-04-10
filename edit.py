import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from openpyxl import load_workbook
from termcolor import colored
import time

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']


TOKEN = '6173641683:AAF10JrrBpfxZeAjWnwPhn0VzM0MBYVdYqk'
ALLOWED_IDS = [577948990] # список разрешенных ID пользователей

# функция для проверки, является ли пользователь администратором
def is_admin(update):
    return update.effective_user.id in ALLOWED_IDS

# функция-обработчик команды /start
def start(update, context):
    # проверяем, является ли пользователь администратором
    if not is_admin(update):
        context.bot.send_message(chat_id=update.effective_chat.id, text="У вас нет прав на использование этого бота.")
        return
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Этот бот записывает данные в XLSX таблицу. Отправь мне несколько строк с данными, и я запишу их в таблицу.")

# функция-обработчик сообщений
def handle_message(update, context):
    # проверяем, является ли пользователь администратором
    if not is_admin(update):
        context.bot.send_message(chat_id=update.effective_chat.id, text="У вас нет прав на использование этого бота.")
        return
    user_input = update.message.text
    parts = user_input.split('\n')
    for part in parts:
        if not part.strip():
            continue
        cols = part.split()
        if len(cols) != 2:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Неверный формат ввода. Отправь мне два слова через пробел в каждой строке, и я запишу их в таблицу.")
            return
        col1 = cols[0]
        col2 = cols[1]
        worksheet.append([col1, col2])
    
    # Сохраняем данные в файл только после записи каждого сообщения
    workbook.save('example.xlsx')
    context.bot.send_message(chat_id=update.effective_chat.id, text="Данные успешно записаны в таблицу!")

# Открываем существующий файл для записи
workbook = load_workbook(filename='example.xlsx')
worksheet = workbook.active

# Создаем экземпляр класса Updater и добавляем обработчики команд и сообщений
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)

text = '!Bot started!\n\n\nProject channel: \n=============\n@Panda_Space\n=============\n\nCreated by:\n=============\n@Panda_ADM\n=============\n'
colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']

for i in range(69):
    for color in colors:
        print('\033[2J\033[1;1H' + color + text, end='\r')
        time.sleep(0.9)
        
# Запускаем бота
updater.start_polling()
updater.idle()
