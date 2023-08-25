import telebot
from telebot import types

TOKEN = '6490536043:AAGIZndJZLbuILBa8kJCHafxsqNU9IeTe8c'
bot = telebot.TeleBot(TOKEN)
bot = telebot.TeleBot(TOKEN)

user_data = {}
lists = [
    ["Élément 1-1", "Élément 1-2", "Élément 1-3"],
    ["Élément 2-1", "Élément 2-2", "Élément 2-3"],
    ["Élément 3-1", "Élément 3-2", "Élément 3-3"]
]


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_data[user_id] = {"list_index": 0, "element_index": 0}
    send_list(user_id, edit_message=False)


def send_list(user_id, edit_message=True):
    list_index = user_data[user_id]["list_index"]
    element_index = user_data[user_id]["element_index"]
    current_list = lists[list_index]

    markup = types.InlineKeyboardMarkup(row_width=2)
    confirm_button = types.InlineKeyboardButton("Confirmer", callback_data="confirm")
    markup.add(confirm_button)

    if element_index > 0:
        prev_button = types.InlineKeyboardButton("Précédent", callback_data="prev")
        markup.row(prev_button)  # Utiliser row() au lieu de insert()
    if element_index < len(current_list) - 1:
        next_button = types.InlineKeyboardButton("Suivant", callback_data="next")
        markup.row(next_button)  # Utiliser row() au lieu de insert()

    if edit_message:
        bot.edit_message_text(chat_id=user_id, message_id=user_data[user_id]["message_id"],
                              text=current_list[element_index], reply_markup=markup)
    else:
        sent_message = bot.send_message(user_id, current_list[element_index], reply_markup=markup)
        user_data[user_id]["message_id"] = sent_message.message_id


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    list_index = user_data[user_id]["list_index"]
    element_index = user_data[user_id]["element_index"]
    current_list = lists[list_index]

    if call.data == "prev" and element_index > 0:
        user_data[user_id]["element_index"] -= 1
    elif call.data == "next":
        if element_index < len(current_list) - 1:
            user_data[user_id]["element_index"] += 1
        elif list_index < len(lists) - 1:
            user_data[user_id]["list_index"] += 1
            user_data[user_id]["element_index"] = 0
    elif call.data == "confirm":
        user_data[user_id]["list_index"] += 1
        user_data[user_id]["element_index"] = 0

    send_list(user_id)
    bot.answer_callback_query(call.id)


if __name__ == "__main__":
    bot.polling()