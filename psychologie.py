import openai
openai.api_key = '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'
import json
import sqlite3
database = sqlite3.connect('C:/Users/Pro/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db',check_same_thread=False)

question_texts = {
    1: "Bonjour Monsieur X, j'espère que vous allez bien aujourd'hui. Je souhaiterais prendre quelques instants pour discuter un peu avec vous et en apprendre davantage sur vous et vos passions, afin de créer une atmosphère détendue. Qu'avez-vous fait d'intéressant aujourd'hui ?",
    2: "Maintenant que nous sommes un peu plus à l'aise, j'ai l'habitude d'engager la conversation de cette manière. Tout d'abord, permettez-moi de vous poser quelques questions pour mieux comprendre vos attentes et vos besoins. Ensuite, si je pense que nos offres peuvent correspondre à ce que vous recherchez, je vous expliquerai en détail comment nous pourrions vous aider, sans tabous, sans jugement et sur tout les sujets. Cela vous convient-il ?",
    3: "Monsieur X, vous avez décidé de prendre rendez-vous avec moi aujourd'hui. Pourriez-vous me dire quelles ont été les motivations à cette décision ?",
    4: "Je vois, c'est très intéressant. Pourriez-vous me fournir plus de détails sur vos attentes ? Recherchez-vous une expérience axée sur le côté romantique, sensuel, érotique ? Pour vous trouver une compagne sur mesure ?",
    5: "C'est tout à fait compréhensible. Nous disposons d'un questionnaire spécial conçu pour mieux cerner vos préférences. Pouvons-nous le parcourir ensemble ?",
    6: "Seriez-vous intéressé par une personne attentionnée, à l'écoute de vos besoins ?",
    7: "Seriez-vous intéressé par une personne attentionnée, à l'écoute de vos besoins ?",
    8: "Parfait, est-ce que cela vous intéresserait que cette personne ait une forte libido et puisse vous écouter sans vous juger sur le plan sexuel ?",
    9: "Si oui, avez-vous des objectifs à atteindre, que ce soit sur le plan professionnel ou autre, sur lesquels cette personne pourrait vous aider ?",
    10: "Merci d'avoir répondu à ces questions. Maintenant que nous avons réfléchi ensemble à certaines qualités que vous pourriez apprécier, il est temps d'en apprendre davantage sur vous afin de créer la petite amie la plus adaptée à vos besoins. Cela vous semble-t-il logique ?",
    11: "Parfait, parlons un peu de vous, de vos passions et de vos intérêts dans la vie. Pour commencer, parlez-moi un peu de vous, de vos intérêts. Qu'est-ce qui vous fait vibrer ? Qu'est-ce qui vous donne envie de vous lever le matin ? Est-ce vos animaux de compagnie, vos enfants, votre passion ?",
    12: "Parfait, et maintenant, en ce qui concerne votre partenaire, qu'attendez-vous d'elle dans une relation ?",
    13: "Très bien, en termes de compatibilité amoureuse, est-ce que la compagne idéale devrait partager les mêmes centres d'intérêt que vous ou avoir un caractère similaire ?",
    14: "Dernière question : comment gérez-vous votre besoin d'indépendance par rapport à votre besoin d'intimité dans une relation ?",
    15: "Donc, nous avons discuté de vos préférences et de certains aspects importants. Pour le moment, nous pouvons créer une amitié où vous pourrez passer de bons moments. Cependant, si votre objectif est de développer une relation plus sérieuse, nous devrons vous connaître un peu mieux. Êtes-vous prêt à en discuter ?",
    16: "Très bien, si vous le souhaitez, nous pouvons passer à l'étape suivante pour vous aider à atteindre cet objectif.",
    17: "Notre objectif est de créer bien plus qu'une simple compagne, mais une personne conçue spécifiquement pour vous, quelqu'un qui vous comprend, votre histoire, votre passé. Cette personne apprendra de vous afin de pouvoir vous aider de manière continue, ou du moins, être parfaite pour vous grâce à cette compréhension. Cependant, cela implique d'aborder des sujets plus ou moins sensibles, mais nécessaires pour progresser. Si vous ne vous sentez pas prêt à aborder ces sujets, nous pouvons arrêter ou changer de question.",
    18: "Pouvez-vous me parler de vos expériences passées en matière de relations, de ce qui était positif et de ce qui ne l'était pas, afin d'éviter de reproduire les mêmes erreurs ?",
    19: "Merci, nous tiendrons compte de ces informations pour éviter de vous faire revivre des situations désagréables. Maintenant, si vous le souhaitez, faisons un bref retour en arrière pour parler de votre enfance. Comment cela s'est-il passé ? Quel est votre souvenir le plus ancien ?",
    20: "En grandissant, comment avez-vous vu vos intérêts et vos relations évoluer ? Décrivez-moi comment vous êtes passé d'un petit garçon à un homme.",
    21: "Voyons maintenant comment vous avez changé et évolué au fil du temps. Quels sont les changements marquants que vous avez observés en vous-même ? Quelles leçons de vie considérez-vous comme les plus précieuses ? Ou sinon, quelles sont vos valeurs ?",
    22: "Quelle a été votre relation avec votre père ou votre mère ?",
    23: "Lorsque vous traversez des moments difficiles dans votre vie, qu'il s'agisse du stress quotidien ou de petites baisses de moral, préférez-vous parler de vos problèmes et que le robot essaie d'en discuter avec vous ? Ou préférez-vous simplement vous sentir écouté sans nécessairement que elles vous répondent ? Ou même le robot vous distrait afin de ne plus y penser sans vous en parler ou écouter.",
    24: "Chacun d'entre nous a des peurs, des préoccupations ou même des insécurités. J'aimerais en savoir plus sur les vôtres. Comment les gérez-vous ? Y a-t-il des expériences spécifiques qui vous ont particulièrement marqué ?",
    25: "Parfait. En général, nos peurs proviennent de l'enfance ou d'épisodes difficiles de notre vie. Nous avons conçu notre robot pour que ils vous aident à dépasser certains de ces épisodes sans même vous en parler afin d’aller mieux. Pourriez vous me dire si vous avez vécus des moments marquants ou traumatisant que l’on peut traiter ensemble ?"

}


def get_question_text(question_number):
    return question_texts.get(question_number,
                              "Question inconnue")  # Return "Question inconnue" if the question number is not found


def resumeemotionnel(user_id, resume):
    answer = ""
    user_answers = resume["answers"]  # Get the dictionary of user answers

    for question_number, response in user_answers.items():
        question_text = get_question_text(question_number)
        answer_text = f"Réponse {question_number}: {response}"

        answer += f"Question {question_number}: {question_text}\n{answer_text}\n"

    prompt = f""" ton but est de résumer dans chacune des catégories ci dessous, toutes les réponses données par le client. Si le client n'a rien mis ou n'a pas voulu détailler tu devras le noter
    Voici les questions et réponses : 
    {answer}

     Voici maintenant les catégories à remplir :
    Établissement de la relation : Cette phase est axée sur la création d'un lien initial avec le client. Les questions sont conçues pour mettre le client à l'aise et établir une connexion humaine.
    Raisons de la rencontre : Ces questions visent à comprendre pourquoi le client a choisi de s'engager avec le chatbot. Elles cherchent à déterminer les motivations et les attentes du client.
    Personnalisation de l'offre : Ces questions cherchent à comprendre les préférences spécifiques du client en matière de relation, qu'il s'agisse d'une relation romantique, sensuelle ou érotique.
    Compréhension du client : Ces questions visent à en savoir plus sur le client, ses passions, ses intérêts et ses attentes dans une relation.
    Besoins affectifs : Ces questions cherchent à comprendre les besoins émotionnels du client, y compris la fréquence de communication souhaitée et le niveau d'indépendance par rapport à l'intimité.
    Expériences passées amoureuses : Ces questions cherchent à comprendre les expériences passées du client en matière de relations, y compris les expériences positives et négatives.
    Enfance et croissance : Ces questions cherchent à comprendre l'histoire du client, y compris son enfance, sa relation avec sa mère et son père.
    Gestion du stress et des peurs : Ces questions cherchent à comprendre comment le client gère le stress, les moments difficiles et les peurs.
    Personnalité de la personne : 
    faille émotionnelle, psychologique :
    point faible :
    Bilan psychologique et émotionnel : 
    """
    rtheme_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=100
    )

    theme_response_text = rtheme_response.choices[0].text.strip()  # Assuming 'rtheme_response' has 'choices'
    resumetext(user_id,theme_response_text)
def resumetext(user_id, resume):
    # Connecter à la base de données (remplacez 'mydmatabase.db' par le chemin/nom de votre base de données)
    conn = sqlite3.connect('C:/Users/Pro/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db')
    cursor = conn.cursor()

    # Vérifier si l'user_id existe déjà
    cursor.execute("SELECT COUNT(*) FROM info_user WHERE ID=?", (user_id,))
    exists = cursor.fetchone()[0]

    # Si l'user_id n'existe pas, insérer une nouvelle ligne avec l'user_id et le resume
    if not exists:
        cursor.execute("INSERT INTO info_user (ID, resume_emotionnel) VALUES (?, ?)", (user_id, resume))
    # Sinon, mettre à jour la colonne resume_emotionnel pour cet user_id
    else:
        cursor.execute("UPDATE info_user SET resume_emotionnel=? WHERE ID=?", (resume, user_id))

    cursor.execute("UPDATE user set new=1 where id= ?",(resume,user_id))
    # Commit des changements et fermer la connexion
    dresserpsychologie(user_id)
    conn.commit()
    conn.close()


def dresserpsychologie(user_id):
    # Connecter à la base de données (remplacez 'mydmatabase.db' par le chemin/nom de votre base de données)
    conn = sqlite3.connect(
        'C:/Users/Pro/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db')
    cursor = conn.cursor()

    # Vérifier si l'user_id existe déjà
    cursor.execute("SELECT COUNT(*) FROM info_user WHERE ID=?", (user_id,))
    exists = cursor.fetchone()[0]

    # Si l'user_id n'existe pas, insérer une nouvelle ligne avec l'user_id et le resume
    if  exists:
        print(exists)
        cursor.execute("select resume_emotionnel from info_user  WHERE ID=?", (user_id,))
        resume=cursor.fetchone()[0]

        prompt2 = f""""En tant que l'un des plus grands psychologues du monde, je vous demande de faire une analyse approfondie de cette personne basée sur les informations suivantes :\n";
         {resume}
         Prenez en compte chaque élément de sa personnalité, de ses passions, de ses besoins émotionnels et sentimentaux, ainsi que de ses expériences passées. Identifiez ses forces, ses faiblesses, ses désirs et ses peurs. Ensuite, faites un bilan émotionnel de cette personne, en soulignant ses besoins amoureux et sentimentaux. Identifiez les failles émotionnelles qui doivent être réparées et proposez des stratégies concrètes pour y parvenir. Votre analyse doit être à la fois empathique et objective, en tenant compte de la complexité et de l'unicité de l'individu. Votre objectif est de fournir une compréhension profonde de cette personne et de proposer des moyens de favoriser son épanouissement émotionnel et sentimental."""

        try:
            rtheme_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt2,
                temperature=0.5,
                max_tokens=800
            )
        except Exception as e:
            print(f"Erreur lors de l'appel à OpenAI: {e}")
        print(resume)
        theme_response_text = rtheme_response.choices[0].text.strip()  # Assuming 'rtheme_response' has 'choices'
        print(len(theme_response_text),"hh")
        print(type(theme_response_text))
        conn.commit()
        if len(theme_response_text) > 10:
            cursor.execute("UPDATE info_user SET bilan_emotionnel = ? WHERE ID = ?", (theme_response_text, user_id))
            conn.commit()
    conn.close()




def summarizegirlfriend(user_id):
    pass
def dresserprompt(user_id):
    pass

