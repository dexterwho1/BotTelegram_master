import sqlite3
import telebot
from telebot import types
import sqlite3
from psychologie import *
TOKEN = '6490536043:AAGIZndJZLbuILBa8kJCHafxsqNU9IeTe8c'
bot = telebot.TeleBot(TOKEN)
user_states = {}


def question_1(user_id):
    bot.send_message(user_id,
                     "Bonjour Monsieur X, j'espère que vous allez bien aujourd'hui. Je souhaiterais prendre quelques instants pour discuter un peu avec vous et en apprendre davantage sur vous et vos passions, afin de créer une atmosphère détendue. Qu'avez-vous fait d'intéressant aujourd'hui ?")


def question_2(user_id):
    bot.send_message(user_id,
                     "Maintenant que nous sommes un peu plus à l'aise, j'ai l'habitude d'engager la conversation de cette manière. Tout d'abord, permettez-moi de vous poser quelques questions pour mieux comprendre vos attentes et vos besoins. Ensuite, si je pense que nos offres peuvent correspondre à ce que vous recherchez, je vous expliquerai en détail comment nous pourrions vous aider, sans tabous, sans jugement et sur tout les sujets. Cela vous convient-il ?")


def question_3(user_id):
    bot.send_message(user_id,
                     "Monsieur X, vous avez décidé de prendre rendez-vous avec moi aujourd'hui. Pourriez-vous me dire quelles ont été les motivations à cette décision ?")


def question_4(user_id):
    bot.send_message(user_id,
                     "Je vois, c'est très intéressant. Pourriez-vous me fournir plus de détails sur vos attentes ? Recherchez-vous une expérience axée sur le côté romantique, sensuel, érotique ? Pour vous trouver une compagne sur mesure ?")


def question_5(user_id):
    bot.send_message(user_id,
                     "C'est tout à fait compréhensible. Nous disposons d'un questionnaire spécial conçu pour mieux cerner vos préférences. Pouvons-nous le parcourir ensemble ?")


def question_6(user_id):
    bot.send_message(user_id,
                     "Seriez-vous intéressé par une personne attentionnée, à l'écoute de vos besoins ?")


def question_7(user_id):
    send_message(user_id, "Seriez-vous intéressé par une personne attentionnée, à l'écoute de vos besoins ?")


def question_10(user_id):
    send_message(user_id,
                 "Parfait, est-ce que cela vous intéresserait que cette personne ait une forte libido et puisse vous écouter sans vous juger sur le plan sexuel ?")


def question_11(user_id):
    send_message(user_id,
                 "Si oui, avez-vous des objectifs à atteindre, que ce soit sur le plan professionnel ou autre, sur lesquels cette personne pourrait vous aider ?")


def question_12(user_id):
    send_message(user_id,
                 "Merci d'avoir répondu à ces questions. Maintenant que nous avons réfléchi ensemble à certaines qualités que vous pourriez apprécier, il est temps d'en apprendre davantage sur vous afin de créer la petite amie la plus adaptée à vos besoins. Cela vous semble-t-il logique ?")


def question_13(user_id):
    send_message(user_id,
                 "Parfait, parlons un peu de vous, de vos passions et de vos intérêts dans la vie. Pour commencer, parlez-moi un peu de vous, de vos intérêts. Qu'est-ce qui vous fait vibrer ? Qu'est-ce qui vous donne envie de vous lever le matin ? Est-ce vos animaux de compagnie, vos enfants, votre passion ?")


def question_14(user_id):
    send_message(user_id,
                 "Parfait, et maintenant, en ce qui concerne votre partenaire, qu'attendez-vous d'elle dans une relation ?")


def question_15(user_id):
    send_message(user_id,
                 "Très bien, en termes de compatibilité amoureuse, est-ce que la compagne idéale devrait partager les mêmes centres d'intérêt que vous ou avoir un caractère similaire ?")


def question_16(user_id):
    send_message(user_id,
                 "Dernière question : comment gérez-vous votre besoin d'indépendance par rapport à votre besoin d'intimité dans une relation ?")


def question_17(user_id):
    send_message(user_id,
                 "Donc, nous avons discuté de vos préférences et de certains aspects importants. Pour le moment, nous pouvons créer une amitié où vous pourrez passer de bons moments. Cependant, si votre objectif est de développer une relation plus sérieuse, nous devrons vous connaître un peu mieux. Êtes-vous prêt à en discuter ?")


def question_18(user_id):
    send_message(user_id,
                 "Très bien, si vous le souhaitez, nous pouvons passer à l'étape suivante pour vous aider à atteindre cet objectif.")


def question_19(user_id):
    send_message(user_id,
                 "Notre objectif est de créer bien plus qu'une simple compagne, mais une personne conçue spécifiquement pour vous, quelqu'un qui vous comprend, votre histoire, votre passé. Cette personne apprendra de vous afin de pouvoir vous aider de manière continue, ou du moins, être parfaite pour vous grâce à cette compréhension. Cependant, cela implique d'aborder des sujets plus ou moins sensibles, mais nécessaires pour progresser. Si vous ne vous sentez pas prêt à aborder ces sujets, nous pouvons arrêter ou changer de question.")


def question_20(user_id):
    send_message(user_id,
                 "Pouvez-vous me parler de vos expériences passées en matière de relations, de ce qui était positif et de ce qui ne l'était pas, afin d'éviter de reproduire les mêmes erreurs ?")


def question_21(user_id):
    send_message(user_id,
                 "Merci, nous tiendrons compte de ces informations pour éviter de vous faire revivre des situations désagréables. Maintenant, si vous le souhaitez, faisons un bref retour en arrière pour parler de votre enfance. Comment cela s'est-il passé ? Quel est votre souvenir le plus ancien ?")


def question_22(user_id):
    send_message(user_id,
                 "En grandissant, comment avez-vous vu vos intérêts et vos relations évoluer ? Décrivez-moi comment vous êtes passé d'un petit garçon à un homme.")


def question_23(user_id):
    send_message(user_id,
                 "Voyons maintenant comment vous avez changé et évolué au fil du temps. Quels sont les changements marquants que vous avez observés en vous-même ? Quelles leçons de vie considérez-vous comme les plus précieuses ? Ou sinon, quelles sont vos valeurs ?")


def question_24(user_id):
    send_message(user_id, "Quelle a été votre relation avec votre père ou votre mère ?")


def question_25(user_id):
    send_message(user_id,
                 "Lorsque vous traversez des moments difficiles dans votre vie, qu'il s'agisse du stress quotidien ou de petites baisses de moral, préférez-vous parler de vos problèmes et que le robot essaie d'en discuter avec vous ? Ou préférez-vous simplement vous sentir écouté sans nécessairement que elles vous répondent ? Ou même le robot vous distrait afin de ne plus y penser sans vous en parler ou écouter.")


def question_26(user_id):
    send_message(user_id,
                 "Chacun d'entre nous a des peurs, des préoccupations ou même des insécurités. J'aimerais en savoir plus sur les vôtres. Comment les gérez-vous ? Y a-t-il des expériences spécifiques qui vous ont particulièrement marqué ?")


def question_27(user_id):
    send_message(user_id,
                 "Parfait. En général, nos peurs proviennent de l'enfance ou d'épisodes difficiles de notre vie. Nous avons conçu notre robot pour que ils vous aident à dépasser certains de ces épisodes sans même vous en parler afin d’aller mieux. Pourriez vous me dire si vous avez vécus des moments marquants ou traumatisant que l’on peut traiter ensemble ?")


def abonnement_1_main(user_id,message):
    response=[]
    # Votre logique pour l'abonnement de type 1
    if user_id not in user_states:
        # Si l'utilisateur est nouveau, initiez le questionnaire
        message_de_presentation(user_id)
        user_states[user_id] = {"current_question": 1, "answers": {}}
        question_1(user_id)
    else:
        # Sinon, traitez la réponse de l'utilisateur
        current_question = user_states[user_id]["current_question"]
        user_states[user_id]["answers"][current_question] = message.text
        next_question = current_question + 1
        if next_question <= 19:
            user_states[user_id]["current_question"] = next_question
            question_funcs[next_question](user_id)
        else:
            # L'utilisateur a terminé le questionnaire, faites ce que vous voulez ensuite ici.
            print(user_states[user_id])
            resumeemotionnel(user_id, user_states[user_id])


def send_message(user_id, message):
    # Cette fonction est un exemple, vous devrez l'implémenter en fonction de votre plateforme.
    print(f"Sending to {user_id}: {message}")
    bot.send_message(user_id, message)

def start_survey(user_id):
    # Votre première question
    question_1(user_id)
    question_2(user_id)
    question_3(user_id)
    question_4(user_id)
    question_5(user_id)
    question_6(user_id)
    question_7(user_id)
    question_10(user_id)
    question_11(user_id)
    question_12(user_id)
    question_13(user_id)
    question_14(user_id)
    question_15(user_id)
    question_16(user_id)
    question_17(user_id)
    question_18(user_id)
    question_19(user_id)
    question_20(user_id)
    question_21(user_id)

question_funcs = {
    1: question_1,
    2: question_2,
    3: question_3,
    4: question_4,
    5: question_5,
    6: question_6,
    7: question_7,
    8: question_10,
    9: question_11,
    10: question_12,
    11: question_13,
    12: question_14,
    13: question_15,
    14: question_16,
    15: question_17,
    16: question_18,
    17: question_19,
    18: question_20,
    19: question_21
}




def message_de_presentation(user_id):
    bot.send_message(user_id, "Parfait, vous avez fait le bon choix. Il ne reste plus que une toute petite étape, pour parler avec votre compagne. Cependant nous devons vous connaître un tout petit peu 🤗 Notre agent va vous poser quelques questions, il faudra répondre en un seul message, à chaque question. Soyez honnête avec vous même, plus nous vous connaitrons plus madame pourra vous aider 💕. Si vous ne souhaitez pas répondre, répondez par je ne souhaite pas répondre")


