import os
import openpyxl
from telegram.ext import Updater, CommandHandler
from termcolor import colored
import time
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
TOKEN = '6173641683:AAF10JrrBpfxZeAjWnwPhn0VzM0MBYVdYqk'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🐼 Panda Space 🐼\n Я бот который будет искать данные по всем базам которые у меня есть, отпавь мне номер телефена без +7 и с командой /search + номер")

def search(update, context):
    args = context.args
    if len(args) == 0:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Введите поисковый запрос в команде, \n\n например: \n /search 987654321")
        return

    workbook = openpyxl.load_workbook('example.xlsx')
    sheet = workbook.active

    for row in sheet.iter_rows(values_only=True):
        if any(arg in str(cell).lower() for arg in args for cell in row):
            column_b = row[1]
            context.bot.send_message(chat_id=update.effective_chat.id, text="Данные в базе:\n\n" + str(column_b) + '\n\n=============\n@Panda_Space\n=============')
            return

    context.bot.send_message(chat_id=update.effective_chat.id, text="Ничего не найдено.")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("search", search))
    updater.start_polling()
    text = '!Bot started!\n\n\nProject channel: \n=============\n@Panda_Space\n=============\n\nCreated by:\n=============\n@Panda_ADM\n=============\n'
    colors = ['\033[91m', '\033[93m', '\033[92m', '\033[96m', '\033[94m', '\033[95m']

    for i in range(69):
        for color in colors:
            print('\033[2J\033[1;1H' + color + text, end='\r')
            time.sleep(0.9)
    updater.idle()

if __name__ == '__main__':
    main()