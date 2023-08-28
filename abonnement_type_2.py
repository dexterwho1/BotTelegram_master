import telebot
from telebot import types
from connect_database_abonnement_2 import save_to_database
TOKEN = '6490536043:AAGIZndJZLbuILBa8kJCHafxsqNU9IeTe8c'
bot = telebot.TeleBot(TOKEN)

user_data = {}

lists = [
    ##liste
    {"type": "list", "name": "tu veux que elle soit originaire de quelle continent ?", "values": ["Une européenne", "Une asiatique", "Une africaine", "Une arabe"]},
    {"type": "list", "name": "Choisit son age ?", "values": ["18-25 ans une étudiante bien coquine", "25-30 ans une jeune maman qui veut s'amuser", "30 50 ans une mère de famille seule qui a besoin d'affection", "50 et plus une mature accro au sexe"]},
    {"type": "list", "name": "a quel fréquence veux tu du sexe ?", "values": ["Plusieurs fois par jours", "une fois par jour", "plusieurs fois par semaine"]},
    {"type": "list", "name": "Quelles sont tes fantasmes de lieux ?", "values": ["dans un cinéma", "dans une voiture", "dans une cabine d'essayage", "dans un avion"]},
    {"type": "button", "name": "Tu préfères", "values": ["dominer", "te faire dominer", "à voir selon le moment"]},
    {"type": "button", "name": "Qui devrait prendre les devants au lit?", "values": ["que je prenne les devants", "que tu prennes les devant", "à voir selon le moment"]},
    {"type": "button", "name": "Aimez-vous l'initiative?", "values": ["oui", "non"]},

    ##choix multiple
    {"type": "button", "name": "Est ce que tu aimes te faire sucer ?", "values": ["j'aime bien", "j'aime pas"]},
    {"type": "button", "name": "Est ce que tu aimes la pénétration vaginale ?", "values": ["positif", "negatif"]},
    {"type": "button", "name": "Aimes tu la pénétration anale ?", "values": ["c'est ce que j'aime", "non cela me plait pas"]},
    {"type": "button", "name": "Veux tu inclures des jouets sexuels telles que les godes, vibros...", "values": ["ouiii", "nonnn"]},
    {"type": "button", "name": " Es tu hétéro curieux ?", "values": ["ouii", "nonn"]},
## texte
    {"type": "text", "name": "Racontes moi tes fantasmes"},
    {"type": "text", "name": "Comment t'exciter ?"},
    {"type": "text", "name": "Quelles limites tu ne veux pas franchir ?"},
    {"type": "text", "name": "Dis moi quelles type de lingerie tu veux que je porte"},

]


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_data[user_id] = {"list_index": 0, "element_index": 0, "answers": {}}
    process_list(user_id, False)


def process_list(user_id, edit):
    list_index = user_data[user_id]['list_index']

    if lists[list_index]['type'] == 'list':
        send_list_with_navigation(user_id, edit)
    elif lists[list_index]['type'] == 'button':
        send_list_with_buttons(user_id, edit)
    elif lists[list_index]['type'] == 'text':
        send_text_prompt(user_id)

def send_list_with_navigation(user_id, edit_message):
    list_index = user_data[user_id]['list_index']
    element_index = user_data[user_id]['element_index']
    current_list = lists[list_index]['values']

    markup = types.InlineKeyboardMarkup(row_width=2)

    if element_index > 0:
        prev_button = types.InlineKeyboardButton("Précédent", callback_data="prev")
        markup.add(prev_button)
    if element_index < len(current_list) - 1:
        next_button = types.InlineKeyboardButton("Suivant", callback_data="next")
        markup.add(next_button)

    confirm_button = types.InlineKeyboardButton("Confirmer", callback_data="confirm")
    markup.add(confirm_button)

    if edit_message:
        bot.edit_message_text(text=f"{lists[list_index]['name']}\n\n{current_list[element_index]}", chat_id=user_id,
                              message_id=user_data[user_id]["message_id"], reply_markup=markup)
    else:
        sent_message = bot.send_message(user_id, f"{lists[list_index]['name']}\n\n{current_list[element_index]}", reply_markup=markup)
        user_data[user_id]["message_id"] = sent_message.message_id

def send_list_with_buttons(user_id, edit_message):
    list_index = user_data[user_id]['list_index']
    markup = types.InlineKeyboardMarkup(row_width=2)

    for value in lists[list_index]['values']:
        button = types.InlineKeyboardButton(value, callback_data=value)
        markup.add(button)

    if edit_message:
        bot.edit_message_text(text=lists[list_index]['name'], chat_id=user_id,
                              message_id=user_data[user_id]["message_id"], reply_markup=markup)
    else:
        sent_message = bot.send_message(user_id, lists[list_index]['name'], reply_markup=markup)
        user_data[user_id]["message_id"] = sent_message.message_id

def send_text_prompt(user_id):
    bot.send_message(user_id, lists[user_data[user_id]['list_index']]['name'])


@bot.message_handler(func=lambda message: lists[user_data[message.chat.id]['list_index']]['type'] == 'text')
def text_response(message):
    user_id = message.chat.id
    # Stockage des réponses pour le type 'text'
    user_data[user_id]["answers"][lists[user_data[user_id]['list_index']]['name']] = message.text

    user_data[user_id]['list_index'] += 1

    if user_data[user_id]['list_index'] < len(lists):
        process_list(user_id, False)
    else:
        save_to_database(user_id, user_data[user_id]["answers"]) # Appeler la fonction ici

        print("---- Début des réponses ----")
        print(f"User ID: {user_id}")
        print("Réponses :")
        for question, answer in user_data[user_id]["answers"].items():
            print(f"{question}: {answer}")
        print("---- Fin des réponses ----")


# ... Votre code existant ...

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    list_index = user_data[user_id]['list_index']
    current_list = lists[list_index]
    element_index = user_data[user_id]['element_index']

    if call.data == "prev":
        user_data[user_id]['element_index'] -= 1
    elif call.data == "next":
        user_data[user_id]['element_index'] += 1
    elif call.data == "confirm":
        # Stockage des réponses pour le type 'list'
        user_data[user_id]["answers"][current_list['name']] = current_list['values'][element_index]
        user_data[user_id]['list_index'] += 1
        user_data[user_id]['element_index'] = 0
    elif call.data in current_list['values']:
        # Stockage des réponses pour le type 'button'
        user_data[user_id]["answers"][current_list['name']] = call.data
        user_data[user_id]['list_index'] += 1

        # Éditer le message pour enlever les boutons
        bot.edit_message_text(text=current_list['name'] + " : " + call.data, chat_id=user_id,
                              message_id=call.message.message_id)

    if user_data[user_id]['list_index'] < len(lists):
        process_list(user_id, True)
    else:
        print("---- Début des réponses ----")
        print(f"User ID: {user_id}")
        print("Réponses :")
        for question, answer in user_data[user_id]["answers"].items():
            print(f"{question}: {answer}")
        print("---- Fin des réponses ----")
        bot.send_message(user_id, "Merci pour vos réponses!")


@bot.message_handler(func=lambda message: lists[user_data[message.chat.id]['list_index']]['type'] == 'text')
def text_response(message):
    user_id = message.chat.id
    # Stockage des réponses pour le type 'text'
    user_data[user_id]["answers"][lists[user_data[user_id]['list_index']]['name']] = message.text
    user_data[user_id]['list_index'] += 1

    if user_data[user_id]['list_index'] < len(lists):
        process_list(user_id, False)
    else:
        save_to_database(user_id, user_data[user_id]["answers"]) # Appeler la fonction ici
        bot.send_message(user_id, "Merci pour vos réponses!")


if __name__ == "__main__":
    bot.polling()
