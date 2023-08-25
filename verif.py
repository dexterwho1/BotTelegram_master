import sqlite3
import telebot
from telebot import types
from datetime import datetime
from abonnement_type_1 import abonnement_1_main
from abonnement_type_2 import abonnement_2_main
from abonnement_type_3 import abonnement_3_main


DATABASE = 'C:/Users/Pro/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db'
TOKEN = '6490536043:AAGIZndJZLbuILBa8kJCHafxsqNU9IeTe8c'
bot = telebot.TeleBot(TOKEN)

def check_user_in_db(message):
    with sqlite3.connect(DATABASE) as conn_local:
        cursor_local = conn_local.cursor()

        user_id = message.chat.id
        cursor_local.execute('SELECT * FROM user WHERE id_user = ?', (user_id,))
        user = cursor_local.fetchone()

        if user:
            user_expiry_date = datetime.strptime(user[2],
                                                 "%Y-%m-%d").date()  # Supposons que la date est stockée au 3ème index (index 2)

            # Vérifiez si la date d'expiration est postérieure à la date d'aujourd'hui
            if user_expiry_date > datetime.today().date():
                new=user[4]
                if int(new)==0:
                    print(new,"lllll")
                    subscription_type = user[5]  # Supposons que le type d'abonnement est à l'index 5
                    if subscription_type == 1:
                        abonnement_1_main(user_id,message)
                    elif subscription_type == 2:
                        abonnement_2_main(user_id)
                    elif subscription_type == 3:
                        abonnement_3_main(user_id)
                    else:
                        bot.send_message(user_id, "Type d'abonnement inconnu. Veuillez contacter l'assistance.")
                else:
                    bot.send_message(message.chat.id,
                                     "Vous êtes déjà enregistré! Si vous avez le moindre problème, contactez l'assistance")

        else:
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            itembtn = types.KeyboardButton('Partager le numéro de téléphone', request_contact=True)
            markup.add(itembtn)
            bot.send_message(message.chat.id, """Merci beaucoup d'avoir réalisé un abonnement chez Petcho-Pêche, avant toute chose veuillez nous transmettre votre numéro de téléphone en cliquant sur le H à côté de la barre de recherche message
""", reply_markup=markup)

            bot.send_video(chat_id=message.chat.id, video=open("explication.gif", 'rb'))


from datetime import datetime


def update_user_id_by_phone(user_id, phone_number):
    with sqlite3.connect(DATABASE) as conn_local:
        cursor_local = conn_local.cursor()

        # Obtenez l'utilisateur avec le numéro de téléphone correspondant
        cursor_local.execute('SELECT * FROM user WHERE tel = ?', (phone_number,))
        user = cursor_local.fetchone()

        if user:
            # Convertissez la date de la base de données en un objet datetime
            user_expiry_date = datetime.strptime(user[2],
                                                 "%Y-%m-%d").date()  # Supposons que la date est stockée au 3ème index (index 2)

            # Vérifiez si la date d'expiration est postérieure à la date d'aujourd'hui
            if user_expiry_date > datetime.today().date():
                cursor_local.execute('UPDATE user SET id_user = ? WHERE tel = ?', (user_id, phone_number))
                conn_local.commit()


            else:
                bot.send_message(user_id,
                                 "Votre abonnement semble avoir expiré. Veuillez renouveler votre abonnement ou contacter l'assistance si vous pensez que c'est une erreur.")
        else:
            bot.send_message(user_id,
                             "Numéro de téléphone non enregistré dans notre base de donnée. Je vous invite à commander un abonnement sur notre site internet petchopeche, cependant si vous avez un abonnement actif, veuillez contacter l'assistance.")



