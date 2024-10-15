import streamlit as st
import random

# Fonction pour expliquer les règles de grammaire
def lecons_grammaire():
    st.header("Leçons de grammaire allemande")
    
    st.subheader("La déclinaison des adjectifs en allemand")
    
    # Introduction
    st.write("""
    En allemand, la déclinaison des adjectifs change en fonction du cas (nominatif, accusatif, datif, génitif), du genre (masculin, féminin, neutre), 
    du nombre (singulier ou pluriel) et du type d'article qui précède l'adjectif. 
    """)
    
    # Explication avec article défini
    st.markdown("### Adjectif précédé d’un **article défini**")
    st.write("""
    Lorsqu'un adjectif est précédé d’un article défini (*der, die, das*), l’adjectif prend une terminaison différente selon le cas et le genre :
    """)
    
    # Tableau pour l'article défini
    st.table({
        "Cas": ["Nominatif", "Accusatif", "Datif", "Génitif"],
        "Masculin": ["der große Mann", "den großen Mann", "dem großen Mann", "des großen Mannes"],
        "Féminin": ["die große Frau", "die große Frau", "der großen Frau", "der großen Frau"],
        "Neutre": ["das große Kind", "das große Kind", "dem großen Kind", "des großen Kindes"],
        "Pluriel": ["die großen Männer", "die großen Männer", "den großen Männern", "der großen Männer"]
    })
    
    st.write("""
    Comme tu peux le voir, lorsque l'adjectif est précédé d'un article défini, les terminaisons des adjectifs sont assez uniformes :
    - **-e** au nominatif singulier féminin et neutre, et au pluriel.
    - **-en** dans presque tous les autres cas (masculin accusatif, datif, génitif).
    """)
    
    # Explication avec article indéfini
    st.markdown("### Adjectif précédé d’un **article indéfini**")
    st.write("""
    Lorsqu’un adjectif est précédé d’un article indéfini (*ein, eine, ein*), l’adjectif prend une terminaison différente :
    """)
    
    # Tableau pour l'article indéfini
    st.table({
        "Cas": ["Nominatif", "Accusatif", "Datif", "Génitif"],
        "Masculin": ["ein großer Mann", "einen großen Mann", "einem großen Mann", "eines großen Mannes"],
        "Féminin": ["eine große Frau", "eine große Frau", "einer großen Frau", "einer großen Frau"],
        "Neutre": ["ein großes Kind", "ein großes Kind", "einem großen Kind", "eines großen Kindes"],
        "Pluriel": ["(keine) großen Männer", "(keine) großen Männer", "(keinen) großen Männern", "(keiner) großen Männer"]
    })
    
    st.write("""
    Note ici que l’adjectif prend la terminaison **-er** au nominatif masculin, mais **-es** au neutre, et les autres cas sont similaires aux déclinaisons après un article défini.
    """)
    
    # Explication sans article
    st.markdown("### Adjectif sans article")
    st.write("""
    Lorsqu’il n’y a pas d’article devant l’adjectif, l’adjectif porte toutes les informations grammaticales sur le cas, le genre, et le nombre. 
    Voici un tableau montrant la déclinaison de l’adjectif sans article :
    """)
    
    # Tableau pour aucun article
    st.table({
        "Cas": ["Nominatif", "Accusatif", "Datif", "Génitif"],
        "Masculin": ["großer Mann", "großen Mann", "großem Mann", "großen Mannes"],
        "Féminin": ["große Frau", "große Frau", "großer Frau", "großer Frau"],
        "Neutre": ["großes Kind", "großes Kind", "großem Kind", "großen Kindes"],
        "Pluriel": ["große Männer", "große Männer", "großen Männern", "großer Männer"]
    })
    
    st.write("""
    Ici, l’adjectif porte des terminaisons distinctes : **-er** au nominatif masculin, **-es** au nominatif neutre, et **-e** au pluriel.
    """)

    # Exemples supplémentaires
    st.subheader("Exemples supplémentaires")
    
    st.write("""
    1. **Article défini** : _Ich sehe den **großen** Hund._ (accusatif, masculin)
    2. **Article indéfini** : _Ein **kleines** Auto steht dort._ (nominatif, neutre)
    3. **Sans article** : _Große Autos sind teuer._ (nominatif, pluriel)
    """)
    
    # Conseil pour les étudiants
    st.info("""
    **Conseil :** Lorsque tu apprends la déclinaison des adjectifs, essaie de mémoriser les terminaisons des adjectifs avec les articles définis en premier, 
    car elles sont les plus fréquentes. Ensuite, tu pourras apprendre les variations avec les articles indéfinis et sans article.
    """)


# Fonction pour des exercices de grammaire interactifs
def exercices_grammaire():
    st.header("Exercices de grammaire")

    st.write("Complétez les phrases suivantes avec la forme correcte du verbe, de l'article ou de l'adjectif :")

    # Section pour les cas : nominatif, accusatif, datif
    st.subheader("Exercice sur les cas")
    st.write("1. Ich sehe ___ Hund. (der)")
    answer_1 = st.text_input("Votre réponse pour la question 1", "")
    if answer_1.lower() == "den":
        st.write("Correct!")
    elif answer_1:
        st.write("Incorrect, la bonne réponse est 'den'.")

    st.write("2. ___ Katze ist schwarz. (die)")
    answer_2 = st.text_input("Votre réponse pour la question 2", "")
    if answer_2.lower() == "die":
        st.write("Correct!")
    elif answer_2:
        st.write("Incorrect, la bonne réponse est 'die'.")

    st.write("3. Er gibt ___ Frau ein Buch. (die)")
    answer_3 = st.text_input("Votre réponse pour la question 3", "")
    if answer_3.lower() == "der":
        st.write("Correct!")
    elif answer_3:
        st.write("Incorrect, la bonne réponse est 'der'.")

    # Section sur la conjugaison des verbes
    st.subheader("Exercice sur la conjugaison des verbes")
    st.write("4. Er ___ ein Buch. (lesen)")
    answer_4 = st.text_input("Votre réponse pour la question 4", "")
    if answer_4.lower() == "liest":
        st.write("Correct!")
    elif answer_4:
        st.write("Incorrect, la bonne réponse est 'liest'.")

    st.write("5. Wir ___ Deutsch. (lernen)")
    answer_5 = st.text_input("Votre réponse pour la question 5", "")
    if answer_5.lower() == "lernen":
        st.write("Correct!")
    elif answer_5:
        st.write("Incorrect, la bonne réponse est 'lernen'.")

    # Section sur les articles définis et indéfinis
    st.subheader("Exercice sur les articles définis et indéfinis")
    st.write("6. Ich habe ___ Apfel. (un)")
    answer_6 = st.text_input("Votre réponse pour la question 6", "")
    if answer_6.lower() == "einen":
        st.write("Correct!")
    elif answer_6:
        st.write("Incorrect, la bonne réponse est 'einen'.")

    st.write("7. ___ Mann spricht Deutsch. (l'homme)")
    answer_7 = st.text_input("Votre réponse pour la question 7", "")
    if answer_7.lower() == "der":
        st.write("Correct!")
    elif answer_7:
        st.write("Incorrect, la bonne réponse est 'der'.")

    # Section sur la déclinaison des adjectifs
    st.subheader("Exercice sur la déclinaison des adjectifs")
    st.write("8. Das ist ein ___ Haus. (groß)")
    answer_8 = st.text_input("Votre réponse pour la question 8", "")
    if answer_8.lower() == "großes":
        st.write("Correct!")
    elif answer_8:
        st.write("Incorrect, la bonne réponse est 'großes'.")

    st.write("9. Ich habe einen ___ Hund. (klein)")
    answer_9 = st.text_input("Votre réponse pour la question 9", "")
    if answer_9.lower() == "kleinen":
        st.write("Correct!")
    elif answer_9:
        st.write("Incorrect, la bonne réponse est 'kleinen'.")

# Fonction pour afficher un tableau de conjugaison
def tableau_conjugaison():
    st.header("Tableaux de conjugaison des verbes")
    
    verbe = st.selectbox("Choisissez un verbe à conjuguer", ["sein (être)", "haben (avoir)", "machen (faire)"])
    
    if verbe == "sein (être)":
        st.write("""
        Conjugaison du verbe **sein** (être) au présent :
        - Ich bin
        - Du bist
        - Er/Sie/Es ist
        - Wir sind
        - Ihr seid
        - Sie sind
        """)
        
    elif verbe == "haben (avoir)":
        st.write("""
        Conjugaison du verbe **haben** (avoir) au présent :
        - Ich habe
        - Du hast
        - Er/Sie/Es hat
        - Wir haben
        - Ihr habt
        - Sie haben
        """)
        
    elif verbe == "machen (faire)":
        st.write("""
        Conjugaison du verbe **machen** (faire) au présent :
        - Ich mache
        - Du machst
        - Er/Sie/Es macht
        - Wir machen
        - Ihr macht
        - Sie machen
        """)

# Liste de mots, articles, et verbes pour générer les exercices
nouns = ["Hund", "Katze", "Mann", "Frau", "Auto"]
articles = {
    "der": {"nominatif": "der", "accusatif": "den", "datif": "dem", "génitif": "des"},
    "die": {"nominatif": "die", "accusatif": "die", "datif": "der", "génitif": "der"},
    "das": {"nominatif": "das", "accusatif": "das", "datif": "dem", "génitif": "des"}
}
verbs = ["sehen", "geben", "haben", "sein", "lernen"]
adjectives = ["klein", "groß", "schnell", "langsam"]

# Fonction qui génère un exercice de grammaire aléatoire
def generer_exercice():
    # Choisir un type d'exercice
    exercice_type = random.choice(["cas", "conjugaison", "adjectif"])
    
    if exercice_type == "cas":
        return generer_exercice_sur_les_cas()
    elif exercice_type == "conjugaison":
        return generer_exercice_sur_la_conjugaison()
    elif exercice_type == "adjectif":
        return generer_exercice_sur_les_adjectifs()

# Générer un exercice sur les cas
def generer_exercice_sur_les_cas():
    nom = random.choice(nouns)
    article = random.choice(list(articles.keys()))
    cas = random.choice(["nominatif", "accusatif", "datif", "génitif"])
    
    question = f"Complétez la phrase suivante avec l'article correct : ___ {nom} (cas : {cas})."
    reponse = articles[article][cas]
    
    return question, reponse

# Générer un exercice sur la conjugaison des verbes
def generer_exercice_sur_la_conjugaison():
    sujet = random.choice(["ich", "du", "er/sie/es", "wir", "ihr", "sie/Sie"])
    verbe = random.choice(verbs)
    
    conjugaison = {
        "ich": {"sehen": "sehe", "geben": "gebe", "haben": "habe", "sein": "bin", "lernen": "lerne"},
        "du": {"sehen": "siehst", "geben": "gibst", "haben": "hast", "sein": "bist", "lernen": "lernst"},
        "er/sie/es": {"sehen": "sieht", "geben": "gibt", "haben": "hat", "sein": "ist", "lernen": "lernt"},
        "wir": {"sehen": "sehen", "geben": "geben", "haben": "haben", "sein": "sind", "lernen": "lernen"},
        "ihr": {"sehen": "seht", "geben": "gebt", "haben": "habt", "sein": "seid", "lernen": "lernt"},
        "sie/Sie": {"sehen": "sehen", "geben": "geben", "haben": "haben", "sein": "sind", "lernen": "lernen"}
    }
    
    question = f"Conjuguez le verbe '{verbe}' avec le sujet '{sujet}' :"
    reponse = conjugaison[sujet][verbe]
    
    return question, reponse

# Générer un exercice sur la déclinaison des adjectifs
def generer_exercice_sur_les_adjectifs():
    nom = random.choice(nouns)
    adj = random.choice(adjectives)
    article = random.choice(list(articles.keys()))
    cas = random.choice(["nominatif", "accusatif", "datif", "génitif"])
    
    declinaison = {
        "nominatif": {"der": "e", "die": "e", "das": "e"},
        "accusatif": {"der": "en", "die": "e", "das": "e"},
        "datif": {"der": "en", "die": "en", "das": "en"},
        "génitif": {"der": "en", "die": "en", "das": "en"}
    }
    
    question = f"Complétez avec la déclinaison correcte de l'adjectif '{adj}' : {article} ___ {nom} (cas : {cas})."
    reponse = adj + declinaison[cas][article]
    
    return question, reponse

# Fonction principale pour générer des exercices à l'infini
def generer_exercices_infinis():
    while True:
        question, reponse = generer_exercice()
        yield question, reponse        


def exos_infinis():
    st.title("Générateur d'exercices de grammaire allemande - ne marche pas !! 🥸")
    
    
    
    if st.button("Obtenir un nouvel exercice"):
        generateur = generer_exercices_infinis()
        question, reponse = next(generateur)
        st.write(question)
        user_answer = st.text_input("Votre réponse")
        
        if user_answer:
            if user_answer.lower() == reponse:
                st.success("Bonne réponse !")
            else:
                st.error(f"Faux ! La bonne réponse était : {reponse}")
# Fonction principale pour structurer l'application
def main():
    st.title("Eya learning 3000 - Apprenez la Grammaire Allemande 🌭")
    
    menu = ["Accueil", "Leçons de grammaire", "Exercices", "Tableau de conjugaison", "Exos_infini"]
    choix = st.sidebar.selectbox("Menu", menu)
    
    if choix == "Accueil":
        st.subheader("Bienvenue dans votre application d'apprentissage de la grammaire allemande docteure 👩‍⚕️")
        st.write("Explorez les leçons, faites des exercices et pratiquez les conjugaisons.")
        
    elif choix == "Leçons de grammaire":
        lecons_grammaire()
        
    elif choix == "Exercices":
        exercices_grammaire()
        
    elif choix == "Tableau de conjugaison":
        tableau_conjugaison()

    elif choix == "Exos_infini":
        exos_infinis()
if __name__ == "__main__":
    main()
