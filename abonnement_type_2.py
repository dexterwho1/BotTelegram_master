import telebot
from telebot import types

TOKEN = '6490536043:AAGIZndJZLbuILBa8kJCHafxsqNU9IeTe8c'
bot = telebot.TeleBot(TOKEN)

user_articles = [
    {"name": "Une européenne", "image_url": "https://www.alimentarium.org/sites/default/files/media/image/2016-10/AL001-02%20tomate_0.jpg"},
    {"name": "Une africaine"},
    {"name": "Une arabe", "image_url": "https://www.alimentarium.org/sites/default/files/media/image/2016-10/AL001-02%20tomate_0.jpg"},
]

user_2 = [
    {"name": "18-25 ans une étudiante bien coquine", "image_url": "https://www.alimentarium.org/sites/default/files/media/image/2016-10/AL001-02%20tomate_0.jpg"},
    {"name": "25-30 ANS une jeune maman qui veut s'amuser"},
    {"name": "30 50 ans une mère de famille seule qui a besoin d'affection", "image_url": "https://www.alimentarium.org/sites/default/files/media/image/2016-10/AL001-02%20tomate_0.jpg"},
    {"name": "50 et plus, une mature accro au sexe"}
]

question_3 = [
    {"name": "dominer"},
    {"name": "te faire dominer"}
]

lists_sequence = [user_articles, user_2, question_3]
current_list_index = 0

def send_article_list(user_id, articles, page=1, message_id=None, new_message=False):
    markup = types.InlineKeyboardMarkup()
    current_article = articles[page - 1]
    buttons = []

    if page > 1:
        btn_prev = types.InlineKeyboardButton("⬅️ Précédent", callback_data=f"articles_prev_{page - 1}")
        buttons.append(btn_prev)

    if page < len(articles):
        btn_next = types.InlineKeyboardButton("➡️ Suivant", callback_data=f"articles_next_{page + 1}")
        buttons.append(btn_next)

    if buttons:
        markup.row(*buttons)

    if current_list_index < len(lists_sequence) - 1:
        btn_confirm = types.InlineKeyboardButton("🙂 Confirmer le choix", callback_data="confirm_choice")
        markup.add(btn_confirm)

    if new_message:
        bot.send_photo(chat_id=user_id, photo=current_article.get("image_url", None), caption=current_article["name"], reply_markup=markup)
    else:
        bot.edit_message_caption(caption=current_article["name"], chat_id=user_id, message_id=message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    global current_list_index
    current_list = lists_sequence[current_list_index]

    if "articles_next_" in call.data:
        page = int(call.data.split("_")[2])
        send_article_list(call.message.chat.id, current_list, page, call.message.message_id)

    elif "articles_prev_" in call.data:
        page = int(call.data.split("_")[2])
        send_article_list(call.message.chat.id, current_list, page, call.message.message_id)

    elif call.data == "confirm_choice":
        current_list_index += 1
        # Supprimer le bouton du message précédent
        markup = types.InlineKeyboardMarkup()
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup)
        # Envoyer la nouvelle liste comme un nouveau message
        send_article_list(call.message.chat.id, lists_sequence[current_list_index], 1, new_message=True)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global current_list_index
    current_list_index = 0
    send_article_list(message.chat.id, lists_sequence[current_list_index], 1, new_message=True)

bot.polling()
