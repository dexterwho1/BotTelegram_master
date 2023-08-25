import sqlite3
import telebot
from telebot import types
from datetime import datetime
from verif import *
DATABASE = 'C:/Users/Pro/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db'
TOKEN = '6490536043:AAGIZndJZLbuILBa8kJCHafxsqNU9IeTe8c'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, 'Bienvenue!')
    check_user_in_db(message)


@bot.message_handler(func=lambda m: True)
def handle_message(message):
    check_user_in_db(message)


@bot.message_handler(content_types=['contact'])
def handle_contact(message):
    user_phone = message.contact.phone_number
    update_user_id_by_phone(message.chat.id, user_phone)



if __name__ == '__main__':
    bot.polling(none_stop=True)
