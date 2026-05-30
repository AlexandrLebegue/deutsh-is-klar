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
# ============================================================
# EXERCICES B2 — GOETHE-ZERTIFIKAT B2
# ============================================================

def _lesen_teil1():
    st.subheader("Teil 1 — Forumsbeiträge zuordnen")
    st.info("Lisez les 4 contributions au forum sur le thème du minimalisme, puis associez chaque affirmation à l'auteur correspondant (A, B, C ou D). Plusieurs affirmations peuvent correspondre au même auteur.")

    autoren = {
        "A — Lea_K": (
            "Ich habe vor einem Jahr begonnen, meine Wohnung zu entrümpeln. Seitdem besitze ich nur noch "
            "150 Kleidungsstücke, und ich kann nicht sagen, wie erleichtert ich mich fühle. Natürlich "
            "vermisse ich manchmal ein bestimmtes Hemd, aber der Gewinn an innerer Ruhe überwiegt bei "
            "weitem. Mein größtes Problem war, Dinge loszulassen, die Erinnerungen tragen."
        ),
        "B — Marco_V": (
            "Für mich ist Minimalismus kein Lebensstil, sondern eine Notwendigkeit. Als Student habe ich "
            "schlichtweg keinen Platz für unnötige Dinge. Aber ich bemerke, dass ich konzentrierter arbeite, "
            "seit ich meinen Schreibtisch aufgeräumt habe. Digital funktioniert das genauso: Ich habe "
            "300 Apps gelöscht und nutze jetzt nur noch fünf."
        ),
        "C — Sara_B": (
            "Ich bin skeptisch. Der Minimalismus-Trend kommt vor allem aus Ländern, in denen Menschen schon "
            "im Überfluss leben. Für jemanden, der tatsächlich arm ist, ist Minimalismus keine Philosophie "
            "— es ist der Alltag. Ich finde, die Bewegung hat einen blinden Fleck, was soziale Ungleichheit "
            "betrifft."
        ),
        "D — Tobias_F": (
            "Ich habe den Minimalismus ausprobiert, aber nach drei Monaten wieder aufgegeben. Ich vermisse "
            "meine Buchsammlung und meine Vinylplatten zu sehr. Vielleicht ist Minimalismus einfach nichts "
            "für Menschen, die kreativ sind und Inspiration durch Objekte brauchen. Ich räume auf, aber ich "
            "werde nie minimalistisch leben."
        ),
    }
    for label, text in autoren.items():
        with st.expander(f"**{label}**"):
            st.write(text)

    aussagen = [
        ("Diese Person hat digitale Gewohnheiten verändert.", "B"),
        ("Diese Person sieht Minimalismus als gesellschaftlich problematisch an.", "C"),
        ("Diese Person hat Minimalismus dauerhaft abgelehnt.", "D"),
        ("Diese Person hatte Schwierigkeiten, emotionale Bindungen zu überwinden.", "A"),
        ("Diese Person praktiziert Minimalismus aus praktischen Gründen.", "B"),
        ("Diese Person glaubt, Kreativität brauche materielle Gegenstände.", "D"),
        ("Diese Person berichtet von einem Gefühl der Befreiung.", "A"),
        ("Diese Person kritisiert die sozialen Voraussetzungen der Bewegung.", "C"),
        ("Diese Person verbesserte ihre Arbeitsfähigkeit durch Ordnung.", "B"),
    ]

    st.markdown("**Zuordnungsaufgabe :** Welche Person sagt das?")
    answers = []
    for i, (aussage, _) in enumerate(aussagen):
        st.write(f"**{i+1}.** {aussage}")
        ans = st.selectbox("Auteur :", ["— choisir —", "A", "B", "C", "D"], key=f"lt1_sel_{i}")
        answers.append(ans)

    if st.button("Vérifier mes réponses", key="lt1_check"):
        score = 0
        for i, (_, correct) in enumerate(aussagen):
            if answers[i] == correct:
                st.success(f"**{i+1}** : Correct ✓")
                score += 1
            elif answers[i] != "— choisir —":
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}**")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}**")
        st.metric("Score", f"{score} / {len(aussagen)}")


def _lesen_teil2():
    st.subheader("Teil 2 — Lückentext : Die Zukunft der Arbeit")
    st.info("Complétez l'article avec les connecteurs/phrases correctes. Choisissez parmi les 8 options (A–H) ; 2 options ne sont pas utilisées.")

    st.markdown("""
> Die Arbeitswelt steht vor einem grundlegenden Wandel. Durch Digitalisierung und Automatisierung verschwinden
> viele traditionelle Berufe, **[1]** entstehen gleichzeitig völlig neue Tätigkeitsfelder. Experten sind sich
> uneinig darüber, ob dieser Wandel letztlich mehr Arbeitsplätze schafft oder vernichtet. **[2]**, dass die
> Qualifikationsanforderungen steigen werden. Wer in der Zukunft erfolgreich sein will, muss sich kontinuierlich
> weiterbilden. **[3]** gilt besonders für technische Berufe, in denen sich die relevanten Kenntnisse schnell
> veralten. Unternehmen investieren daher vermehrt in die Weiterbildung ihrer Mitarbeiter, **[4]** sie die
> Kosten einer vollständigen Neueinstellung vermeiden wollen. Gleichzeitig verlangen viele Arbeitnehmer mehr
> Flexibilität: **[5]** die klassische 40-Stunden-Woche in einem einzigen Unternehmen ist für eine wachsende
> Zahl von Menschen kein attraktives Modell mehr. Homeoffice, Teilzeit und projektbasiertes Arbeiten gewinnen
> an Bedeutung. **[6]** dieser Entwicklung steht die Frage, wie soziale Sicherheit in einer flexibleren
> Arbeitswelt gewährleistet werden kann.
""")

    optionen = {
        "A": "während",
        "B": "Einig sind sich die meisten Forscher jedoch darin",
        "C": "Das",
        "D": "da",
        "E": "Vor allem",
        "F": "Im Mittelpunkt",
        "G": "Obwohl",
        "H": "Außerdem",
    }
    st.markdown("**Options :**")
    for k, v in optionen.items():
        st.markdown(f"- **{k}** : *{v}*")

    correct = ["A", "B", "C", "D", "E", "F"]
    answers = []
    for i in range(1, 7):
        ans = st.selectbox(
            f"Gap [{i}] :",
            ["— wählen —"] + list(optionen.keys()),
            key=f"lt2_sel_{i}"
        )
        answers.append(ans)

    if st.button("Vérifier mes réponses", key="lt2_check"):
        score = 0
        for i, (ans, corr) in enumerate(zip(answers, correct)):
            if ans == corr:
                st.success(f"Gap [{i+1}] : **{ans}** — Correct ✓  (*{optionen[corr]}*)")
                score += 1
            elif ans != "— wählen —":
                st.error(f"Gap [{i+1}] : **{ans}** — Incorrect. Réponse correcte : **{corr}** (*{optionen[corr]}*)")
            else:
                st.warning(f"Gap [{i+1}] : Non répondu. Réponse correcte : **{corr}** (*{optionen[corr]}*)")
        st.metric("Score", f"{score} / 6")


def _lesen_teil3():
    st.subheader("Teil 3 — Leseverstehen : Lebendige Städte")
    st.info("Lisez l'article, puis répondez aux 6 questions en choisissant la bonne réponse (a, b ou c).")

    with st.expander("📄 Artikel lesen : Lebendige Städte — Wie Stadtplanung das Zusammenleben neu erfindet"):
        st.markdown("""
Städte wachsen schneller als je zuvor. Laut UN-Prognosen werden bis 2050 mehr als zwei Drittel der
Weltbevölkerung in städtischen Gebieten leben — ein historisch beispielloser Trend. Doch während die
Bevölkerung in Millionenstädten wächst, kämpfen viele kleinere Städte mit dem gegenteiligen Problem:
Abwanderung, Leerstand und fehlendes Kapital für Infrastrukturmaßnahmen.

Neue Ansätze in der Stadtplanung versuchen, diesem Auseinanderdriften entgegenzuwirken. Das Konzept der
„15-Minuten-Stadt", das vor allem durch die Pariser Bürgermeisterin Anne Hidalgo bekannt wurde, setzt
darauf, dass alle wichtigen Einrichtungen — Arbeit, Einkauf, Erholung, Bildung und Gesundheitsversorgung
— innerhalb von 15 Minuten zu Fuß oder per Fahrrad erreichbar sein sollen. Kritiker werfen dem Modell
vor, es ignoriere wirtschaftliche Realitäten und sei nur in bereits dicht besiedelten, wohlhabenden
Städten umsetzbar.

Einen anderen Weg gehen Städte, die auf „taktischen Urbanismus" setzen: temporäre, kostengünstige
Maßnahmen — parkende Autos werden durch Sitzgelegenheiten ersetzt, leere Ladenflächen als
Gemeinschaftsräume zwischengenutzt — die den öffentlichen Raum aufwerten, ohne jahrelange
Planungsverfahren abzuwarten. Detroit, einst Sinnbild des industriellen Niedergangs, gilt als Pionier
solcher Ansätze. Dort haben Bürger auf brachliegenden Flächen Gemeinschaftsgärten angelegt, die nicht
nur Lebensmittel produzieren, sondern auch nachbarschaftliche Bindungen stärken.

Inwieweit digitale Technologien die Stadtplanung verbessern können, ist ebenfalls umstritten. „Smart
Cities", die Sensordaten zur Verkehrssteuerung und Energieoptimierung nutzen, versprechen Effizienz
— doch Datenschutzfragen und die Gefahr einer technologiegetriebenen Überwachung sind nicht gelöst.
""")

    fragen = [
        {
            "frage": "Was prognostizieren UN-Daten für das Jahr 2050?",
            "optionen": [
                "a) Die Mehrheit der Menschen wird in städtischen Gebieten leben.",
                "b) Kleinere Städte werden stärker wachsen als Großstädte.",
                "c) Die Weltbevölkerung wird hauptsächlich auf dem Land leben.",
            ],
            "correct": "a",
        },
        {
            "frage": "Was kritisieren Gegner des ‚15-Minuten-Stadt'-Konzepts?",
            "optionen": [
                "a) Es sei technisch nicht realisierbar.",
                "b) Es sei nur unter bestimmten städtischen Voraussetzungen anwendbar.",
                "c) Es fördere die Nutzung von Autos.",
            ],
            "correct": "b",
        },
        {
            "frage": "Was kennzeichnet den ‚taktischen Urbanismus'?",
            "optionen": [
                "a) Langfristige, staatlich finanzierte Bauprojekte.",
                "b) Schnelle, günstige Maßnahmen zur Aufwertung des öffentlichen Raums.",
                "c) Die vollständige Umgestaltung von Industriegebieten.",
            ],
            "correct": "b",
        },
        {
            "frage": "Welche Rolle spielt Detroit im Artikel?",
            "optionen": [
                "a) Als Beispiel für gescheiterte Stadtplanung.",
                "b) Als Vorbild für bürgerschaftliche Stadterneuerung.",
                "c) Als Pionier der ‚Smart City'-Technologie.",
            ],
            "correct": "b",
        },
        {
            "frage": "Was wird an ‚Smart Cities' kritisiert?",
            "optionen": [
                "a) Sie seien zu teuer für mittelgroße Städte.",
                "b) Datenschutz und mögliche Überwachung seien problematisch.",
                "c) Sie setzten zu stark auf Fußgänger und Fahrradfahrer.",
            ],
            "correct": "b",
        },
        {
            "frage": "Was ist das Hauptthema des Artikels?",
            "optionen": [
                "a) Die Probleme von Megastädten in Entwicklungsländern.",
                "b) Verschiedene Ansätze zur Verbesserung städtischen Lebens.",
                "c) Die wirtschaftliche Entwicklung von Industriestädten.",
            ],
            "correct": "b",
        },
    ]

    answers = []
    for i, f in enumerate(fragen):
        st.write(f"**{i+1}.** {f['frage']}")
        ans = st.radio("", f["optionen"], key=f"lt3_radio_{i}", index=None, label_visibility="collapsed")
        answers.append(ans)

    if st.button("Vérifier mes réponses", key="lt3_check"):
        score = 0
        for i, (ans, f) in enumerate(zip(answers, fragen)):
            corr_text = next(o for o in f["optionen"] if o.startswith(f["correct"] + ")"))
            if ans is not None and ans.startswith(f["correct"] + ")"):
                st.success(f"**{i+1}** : Correct ✓")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : *{corr_text}*")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : *{corr_text}*")
        st.metric("Score", f"{score} / {len(fragen)}")


def _lesen_teil4():
    st.subheader("Teil 4 — Meinungen zuordnen : Homeoffice")
    st.info("Lisez les 8 opinions sur le télétravail, puis associez chacun des 6 titres au texte correspondant (1–8).")

    textes = {
        "1 — Marta (Übersetzerin)": (
            "Ich brauche absolute Stille zum Arbeiten. Im Büro wird man ständig unterbrochen — jemand fragt "
            "nach einem Stift, jemand klappert mit der Tastatur. Zuhause habe ich meine Produktivität "
            "mindestens verdoppelt."
        ),
        "2 — Jonas (IT-Manager)": (
            "Das Problem ist, dass man im Homeoffice nie wirklich abschaltet. Das Laptop liegt auf dem "
            "Küchentisch, die E-Mails kommen auch um 22 Uhr noch. Die Grenze zwischen Arbeit und Privatleben "
            "löst sich auf, und das macht mir Sorgen."
        ),
        "3 — Priya (Designstudentin)": (
            "Kreativität entsteht durch Begegnung. Wenn ich monatelang alleine vor meinem Bildschirm sitze, "
            "werde ich schlechter in meinem Beruf. Die besten Ideen hatte ich immer in zufälligen Gesprächen "
            "am Kaffeeautomaten."
        ),
        "4 — Klaus (Buchhalter)": (
            "Ich habe 45 Minuten Pendelzeit gespart — jeden Tag. Das klingt wenig, aber über ein Jahr sind "
            "das mehr als 270 Stunden, die ich jetzt für meine Familie nutzen kann. Homeoffice hat mein "
            "Leben verändert."
        ),
        "5 — Lena (Personalchefin)": (
            "Wir haben Schwierigkeiten, neue Mitarbeiter in unsere Unternehmenskultur einzubinden, wenn sie "
            "von Anfang an remote arbeiten. Sie lernen die ungeschriebenen Regeln nie kennen. Das ist ein "
            "strukturelles Problem."
        ),
        "6 — Armin (ehem. Ingenieur)": (
            "In meiner Zeit wäre so etwas undenkbar gewesen. Ich verstehe junge Leute nicht, die freiwillig "
            "alleine zuhause sitzen wollen. Arbeit ist auch Gemeinschaft, Verantwortung — nicht nur Output."
        ),
        "7 — Sophie (alleinerziehende Mutter)": (
            "Für Menschen wie mich ist Homeoffice keine Frage des Komforts, sondern der Möglichkeit, "
            "überhaupt arbeiten zu können. Ich kann meinen Sohn von der Schule abholen und trotzdem meinen "
            "Vollzeitjob machen. Das wäre früher nicht gegangen."
        ),
        "8 — Felix (Startup-Gründer)": (
            "Wir haben nie ein Büro gehabt und sind profitabel. Wir stellen die besten Talente ein, egal wo "
            "sie wohnen. Das Büro ist eine Erfindung des 20. Jahrhunderts — kein Naturgesetz."
        ),
    }
    for label, text in textes.items():
        with st.expander(f"**Text {label}**"):
            st.write(text)

    titres = [
        ("Homeoffice ermöglicht bessere Vereinbarkeit von Familie und Beruf", "7"),
        ("Zeitersparnis durch Wegfall des Pendelns als entscheidender Vorteil", "4"),
        ("Kollektiver Austausch als Motor kreativer Leistung", "3"),
        ("Fehlende Trennung von Berufs- und Privatsphäre als Risiko", "2"),
        ("Integration neuer Mitarbeiter in die Unternehmenskultur erschwert", "5"),
        ("Räumliche Unabhängigkeit als Grundprinzip moderner Unternehmen", "8"),
    ]

    st.markdown("**Zuordnungsaufgabe :** Welcher Titel passt zu welchem Text?")
    answers = []
    choices = ["— wählen —", "1", "2", "3", "4", "5", "6", "7", "8"]
    for i, (titre, _) in enumerate(titres):
        st.write(f"**Titre {i+1} :** *{titre}*")
        ans = st.selectbox("Texte :", choices, key=f"lt4_sel_{i}")
        answers.append(ans)

    if st.button("Vérifier mes réponses", key="lt4_check"):
        score = 0
        for i, (ans, (titre, correct)) in enumerate(zip(answers, titres)):
            if ans == correct:
                st.success(f"**Titre {i+1}** : Correct ✓ (Text {correct})")
                score += 1
            elif ans != "— wählen —":
                st.error(f"**Titre {i+1}** : Incorrect — réponse correcte : Text **{correct}**")
            else:
                st.warning(f"**Titre {i+1}** : Non répondu — réponse correcte : Text **{correct}**")
        st.metric("Score", f"{score} / {len(titres)}")


def _lesen_teil5():
    st.subheader("Teil 5 — Akademische Überschriften")
    st.info("Lisez les 3 paragraphes d'un règlement universitaire et associez à chacun l'en-tête correspondant parmi les 8 proposées (5 ne sont pas utilisées).")

    paragraphes = {
        "Abschnitt A": (
            "Studierende, die aufgrund von Krankheit oder eines anderen wichtigen Grundes an einer Prüfung "
            "nicht teilnehmen konnten, haben dies dem Prüfungsamt unverzüglich, spätestens jedoch innerhalb "
            "von drei Werktagen, schriftlich unter Vorlage entsprechender Nachweise mitzuteilen. Bei "
            "Krankheit ist ein ärztliches Attest vorzulegen, das am Tag der Prüfung ausgestellt sein muss. "
            "Wird der Nachweis nicht fristgemäß erbracht, gilt die Prüfung als nicht bestanden."
        ),
        "Abschnitt B": (
            "Die Gesamtnote des Studiums errechnet sich aus dem gewichteten Durchschnitt aller Modulnoten. "
            "Module des ersten Studienjahrs werden dabei mit dem Faktor 0,5 gewichtet, Module des zweiten "
            "und dritten Jahres mit dem Faktor 1,0. Abschlussarbeit und Kolloquium zusammen bilden 30 % "
            "der Gesamtnote. Bei einem Durchschnitt von 1,0 bis 1,3 wird das Prädikat ‚mit Auszeichnung' "
            "vergeben."
        ),
        "Abschnitt C": (
            "Studierende können auf Antrag von bestimmten Pflichtmodulen befreit werden, wenn sie durch "
            "Vorlage von Nachweisen belegen können, dass sie die entsprechenden Kompetenzen bereits "
            "anderweitig erworben haben — etwa durch eine einschlägige Berufsausbildung, nachgewiesene "
            "Berufserfahrung oder durch Studienleistungen an einer anderen Hochschule. Der Antrag ist vor "
            "Beginn des jeweiligen Semesters beim zuständigen Prüfungsausschuss zu stellen."
        ),
    }
    for label, text in paragraphes.items():
        with st.expander(f"**{label}**"):
            st.write(text)

    ueberschriften = {
        "1": "Anerkennung bereits erworbener Kenntnisse für Pflichtveranstaltungen",
        "2": "Verfahren bei Prüfungsverhinderung und Nachweispflichten",
        "3": "Berechnung der Abschlussnote und Auszeichnungsregelung",
        "4": "Zulassungsvoraussetzungen für Masterstudiengänge",
        "5": "Regelungen zur Verlängerung der Bearbeitungszeit für Abschlussarbeiten",
        "6": "Prüfungswiederholung bei Nichtbestehen",
        "7": "Fristen für die Anmeldung zu Prüfungen",
        "8": "Anerkennung ausländischer Studienabschlüsse",
    }
    st.markdown("**Überschriften (8 options, 5 nicht verwendet) :**")
    for k, v in ueberschriften.items():
        st.markdown(f"- **{k}** : {v}")

    correct_map = {"Abschnitt A": "2", "Abschnitt B": "3", "Abschnitt C": "1"}
    choices = ["— wählen —"] + [str(i) for i in range(1, 9)]
    answers = {}
    for abschnitt in paragraphes:
        ans = st.selectbox(f"Überschrift für **{abschnitt}** :", choices, key=f"lt5_sel_{abschnitt}")
        answers[abschnitt] = ans

    if st.button("Vérifier mes réponses", key="lt5_check"):
        score = 0
        for abschnitt, correct in correct_map.items():
            ans = answers[abschnitt]
            if ans == correct:
                st.success(f"**{abschnitt}** : Correct ✓ (Überschrift {correct})")
                score += 1
            elif ans != "— wählen —":
                st.error(f"**{abschnitt}** : Incorrect — réponse correcte : **{correct}** (*{ueberschriften[correct]}*)")
            else:
                st.warning(f"**{abschnitt}** : Non répondu — réponse correcte : **{correct}** (*{ueberschriften[correct]}*)")
        st.metric("Score", f"{score} / 3")


def exercices_b2_lesen():
    st.header("Lesen — Compréhension écrite B2")
    teil = st.radio(
        "Choisir un exercice :",
        ["Teil 1 — Zuordnung Forum", "Teil 2 — Lückentext", "Teil 3 — Multiple Choice",
         "Teil 4 — Meinungen zuordnen", "Teil 5 — Überschriften"],
        key="lesen_teil_select"
    )
    st.divider()
    if teil == "Teil 1 — Zuordnung Forum":
        _lesen_teil1()
    elif teil == "Teil 2 — Lückentext":
        _lesen_teil2()
    elif teil == "Teil 3 — Multiple Choice":
        _lesen_teil3()
    elif teil == "Teil 4 — Meinungen zuordnen":
        _lesen_teil4()
    elif teil == "Teil 5 — Überschriften":
        _lesen_teil5()


# ============================================================

def _schreiben_teil1():
    st.subheader("Teil 1 — Forumsbeitrag (~250 Wörter)")
    st.markdown("""
**Aufgabe :** Sie haben in einem Online-Forum folgenden Beitrag gelesen :

> *„Ich frage mich, ob Universitäten noch zeitgemäß sind. In Zeiten von YouTube-Tutorials, Online-Kursen
> und KI-Assistenten braucht man keinen Professor mehr, um etwas zu lernen. Das klassische Studium kostet
> Jahre und viel Geld — für Jobs, die es in zehn Jahren vielleicht gar nicht mehr gibt. Ich denke, das
> traditionelle Studium ist ein Auslaufmodell."*

Schreiben Sie einen Beitrag für das Forum (ca. 250 Wörter). Gehen Sie dabei auf folgende Punkte ein :
- Ihre persönliche Meinung zu diesem Standpunkt
- Welche Vorteile hat ein Universitätsstudium, die Online-Lernen nicht ersetzen kann ?
- Wie sollten Universitäten sich Ihrer Meinung nach verändern ?
- Ein konkretes Beispiel aus Ihrem eigenen Erfahrungsbereich
""")
    texte = st.text_area("Votre réponse (environ 250 mots) :", height=400, key="schreiben_t1")
    word_count = len(texte.split()) if texte.strip() else 0
    st.caption(f"Nombre de mots : **{word_count}** / 250")

    with st.expander("📝 Voir un exemple de réponse modèle"):
        st.markdown("""
Der Beitrag von „DigitalNomad_99" spricht ein wichtiges Thema an, vereinfacht aber meiner Meinung nach zu stark.

Es stimmt, dass digitale Lernplattformen das Bildungssystem revolutioniert haben. Ich selbst habe
Programmiersprachen online gelernt, die mir im Beruf täglich nützlich sind. Online-Lernen ist flexibel,
kostengünstig und oft sehr effektiv — besonders für technische Fähigkeiten.

Dennoch kann das traditionelle Studium Dinge bieten, die ein YouTube-Tutorial niemals ersetzen kann. An
der Universität lernt man nicht nur Inhalte, sondern auch, wie man denkt: kritisch argumentiert,
wissenschaftlich recherchiert, in Teams arbeitet. Die Diskussionen im Seminar, die Betreuung durch
erfahrene Wissenschaftler, die sozialen Netzwerke, die man aufbaut — das hat einen Wert, der sich nicht
in einem Online-Zertifikat messen lässt.

Aus meiner eigenen Erfahrung weiß ich, dass meine Kommilitoninnen und Kommilitonen meine wichtigsten
Lehrenden waren. Ich habe durch sie Perspektiven kennengelernt, die ich alleine niemals gefunden hätte.

Universitäten müssen sich allerdings verändern: mehr Praxisbezug, flexible Studienmodelle, engere
Zusammenarbeit mit der Arbeitswelt und eine ehrliche Auseinandersetzung mit den Möglichkeiten der KI.
Das klassische Vorlesungsmodell allein reicht nicht mehr.

**Fazit :** Das traditionelle Studium ist kein Auslaufmodell — aber es muss sich neu erfinden. Nicht gegen
das digitale Lernen, sondern gemeinsam damit.

---
*Points linguistiques B2 illustrés : Konjunktiv II (würde/könnte/müsste), phrases subordonnées complexes, connecteurs (dennoch, allerdings, jedoch), structures argumentatives.*
""")


def _schreiben_teil2():
    st.subheader("Teil 2 — Formelle E-Mail (~150 Wörter)")
    st.markdown("""
**Aufgabe :** Sie haben vor drei Wochen bei einem Onlineshop ein Fahrrad für Ihre Tochter bestellt
(Bestellnummer : 47821-B). Das Paket ist nie angekommen, obwohl Sie eine Versandbestätigung erhalten
haben. Der automatische Kundenservice hat Ihre zwei E-Mails nicht beantwortet.

Schreiben Sie eine formelle Beschwerde-E-Mail (ca. 150 Wörter) an den Kundendienst. Beachten Sie
folgende Punkte :
- Formelle Anrede und Schlussformel
- Klare Darstellung des Problems mit Bestellnummer und Daten
- Konkrete Forderung (Lieferung oder Rückerstattung) mit Frist
- Ton : höflich aber bestimmt
""")
    texte = st.text_area("Votre réponse (environ 150 mots) :", height=300, key="schreiben_t2")
    word_count = len(texte.split()) if texte.strip() else 0
    st.caption(f"Nombre de mots : **{word_count}** / 150")

    with st.expander("📝 Voir un exemple de réponse modèle"):
        st.markdown("""
**Betreff :** Beschwerde – Nicht erhaltenes Paket, Bestellnummer 47821-B

Sehr geehrte Damen und Herren,

am 8. Mai 2026 habe ich über Ihren Onlineshop ein Fahrrad für meine Tochter bestellt (Bestellnummer :
47821-B). Laut Ihrer Versandbestätigung vom 10. Mai sollte das Paket spätestens am 15. Mai eintreffen.
Bis heute, dem 30. Mai, habe ich die Lieferung jedoch nicht erhalten.

Ich habe Ihren Kundenservice am 18. und 24. Mai per E-Mail kontaktiert, bislang aber keine Antwort
erhalten. Dieses Vorgehen ist für mich nicht akzeptabel.

Ich fordere Sie daher auf, mir das bestellte Fahrrad bis spätestens zum 10. Juni 2026 zu liefern oder
den vollen Kaufpreis in Höhe von 349,00 € auf mein Konto zurückzuerstatten. Sollte ich bis zu diesem
Datum keine Rückmeldung erhalten, werde ich rechtliche Schritte einleiten.

Mit freundlichen Grüßen,
[Ihr Name]

---
*Points linguistiques B2 illustrés : formules épistolaires formelles, Konjunktiv II (sollte), passif (wurde bestellt), connecteurs temporels (bis, sobald), registre soutenu.*
""")


def exercices_b2_schreiben():
    st.header("Schreiben — Expression écrite B2")
    teil = st.radio(
        "Choisir un exercice :",
        ["Teil 1 — Forumsbeitrag (~250 Wörter)", "Teil 2 — Formelle E-Mail (~150 Wörter)"],
        key="schreiben_teil_select"
    )
    st.divider()
    if teil == "Teil 1 — Forumsbeitrag (~250 Wörter)":
        _schreiben_teil1()
    elif teil == "Teil 2 — Formelle E-Mail (~150 Wörter)":
        _schreiben_teil2()


# ============================================================

def _hoeren_teil1():
    st.subheader("Teil 1 — Radiosendung : KI in der Medizin")
    st.info("Lisez le transcript de cette émission de radio comme si vous l'écoutiez, puis répondez aux questions.")

    with st.expander("🎙️ Transcript — SWR2 Wissen aktuell"):
        st.markdown("""
**Moderatorin :** Herzlich willkommen zu „Wissen aktuell". Heute sprechen wir über den Einsatz
künstlicher Intelligenz in der Diagnostik. Zu Gast ist Dr. Elena Vogel, Radiologin an der
Universitätsklinik Freiburg. Frau Vogel, KI soll Krebs früher erkennen als Menschen — stimmt das?

**Dr. Vogel :** Das ist eine Vereinfachung, aber es steckt Wahrheit darin. In kontrollierten Studien hat
KI bei bestimmten Krebsarten — vor allem Brust- und Lungenkrebs — eine höhere Erkennungsrate gezeigt als
einzelne Radiologen. Aber : Diese Studien laufen unter Laborbedingungen. Im Klinikalltag sieht das anders
aus.

**Moderatorin :** Was sind die größten Hürden?

**Dr. Vogel :** Erstens die Datenlage. Ein KI-Modell ist nur so gut wie die Daten, mit denen es trainiert
wurde. Wenn ein Modell hauptsächlich mit Bilddaten aus US-amerikanischen Krankenhäusern trainiert wurde,
funktioniert es möglicherweise schlechter bei europäischen Patientenpopulationen. Zweitens die rechtliche
Verantwortung — wenn die KI einen Fehler macht, wer haftet dann? Der Arzt, der Hersteller, das
Krankenhaus? Diese Frage ist noch nicht geklärt.

**Moderatorin :** Und die Ärzte — fürchten sie um ihre Jobs?

**Dr. Vogel :** Das ist interessant. Die jüngeren Kolleginnen und Kollegen sehen KI eher als Werkzeug,
das ihnen Routine-Aufgaben abnimmt, damit sie sich auf komplexe Fälle konzentrieren können. Ältere
Kollegen sind skeptischer. Aber ich glaube : Die KI wird den Radiologen nicht ersetzen. Sie wird ihn
verändern.
""")

    fragen = [
        {
            "frage": "Was ist laut Dr. Vogel das zentrale Problem bei KI-trainierten Modellen?",
            "optionen": [
                "a) Sie sind zu langsam für den Klinikalltag.",
                "b) Sie wurden möglicherweise mit nicht repräsentativen Daten trainiert.",
                "c) Sie können nur bei Lungenkrebs eingesetzt werden.",
            ],
            "correct": "b",
        },
        {
            "frage": "Welche Frage ist laut Dr. Vogel noch ungeklärt?",
            "optionen": [
                "a) Ob KI in Zukunft Chirurgen ersetzen kann.",
                "b) Wer bei einem KI-Fehler rechtlich verantwortlich ist.",
                "c) Ob KI-Systeme günstiger als menschliche Radiologen sind.",
            ],
            "correct": "b",
        },
        {
            "frage": "Wie reagieren jüngere Ärzte laut Dr. Vogel auf KI?",
            "optionen": [
                "a) Sie sind mehrheitlich skeptisch.",
                "b) Sie sehen KI als hilfreiches Werkzeug, das Routineaufgaben übernimmt.",
                "c) Sie fordern strengere Regulierung.",
            ],
            "correct": "b",
        },
        {
            "frage": "Was behauptet Dr. Vogel über KI und menschliche Radiologen im Vergleich?",
            "optionen": [
                "a) KI ist in allen Bereichen dem Menschen überlegen.",
                "b) Unter Studienbedingungen zeigte KI bei bestimmten Krebsarten bessere Ergebnisse.",
                "c) KI hat bisher keine besseren Ergebnisse erzielt.",
            ],
            "correct": "b",
        },
        {
            "frage": "Was ist Dr. Vogels Gesamteinschätzung zur Zukunft des Radiologen-Berufs?",
            "optionen": [
                "a) KI wird Radiologen vollständig ersetzen.",
                "b) Der Beruf wird sich durch KI verändern, aber nicht verschwinden.",
                "c) KI hat keinen signifikanten Einfluss auf den Beruf.",
            ],
            "correct": "b",
        },
    ]

    answers = []
    for i, f in enumerate(fragen):
        st.write(f"**{i+1}.** {f['frage']}")
        ans = st.radio("", f["optionen"], key=f"ht1_radio_{i}", index=None, label_visibility="collapsed")
        answers.append(ans)

    if st.button("Vérifier mes réponses", key="ht1_check"):
        score = 0
        for i, (ans, f) in enumerate(zip(answers, fragen)):
            corr_text = next(o for o in f["optionen"] if o.startswith(f["correct"] + ")"))
            if ans is not None and ans.startswith(f["correct"] + ")"):
                st.success(f"**{i+1}** : Correct ✓")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : *{corr_text}*")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : *{corr_text}*")
        st.metric("Score", f"{score} / {len(fragen)}")


def _hoeren_teil2():
    st.subheader("Teil 2 — Kurze Nachrichten")
    st.info("Lisez les 3 brèves et répondez à une question par meldung.")

    with st.expander("📻 Transcript — Drei Kurzmeldungen"):
        st.markdown("""
**Meldung 1 :** Die Stadt München hat beschlossen, bis 2035 klimaneutral zu werden. Dazu soll der
öffentliche Nahverkehr massiv ausgebaut und der private Autoverkehr in der Innenstadt stark reduziert
werden. Kritiker warnen, dass dies zu massiven Einschränkungen für Pendler führen werde, die keine
Alternative zum Auto haben.

---

**Meldung 2 :** Eine neue Studie der Humboldt-Universität zeigt, dass Kinder, die zweisprachig
aufwachsen, in Tests zu exekutiven Funktionen — also Aufmerksamkeitskontrolle und Problemlösung —
besser abschneiden als einsprachige Kinder. Die Forscher betonen jedoch, dass Zweisprachigkeit keine
Garantie sei und weitere Faktoren eine Rolle spielen.

---

**Meldung 3 :** Die Deutsche Bahn hat angekündigt, bis 2030 alle Nahverkehrszüge auf Wasserstoffantrieb
oder Elektrobetrieb umzustellen. Die Kosten für dieses Programm werden auf über 12 Milliarden Euro
geschätzt. Ob die Finanzierung gesichert ist, ist jedoch noch offen.
""")

    nachrichten = [
        {
            "titel": "Meldung 1 — München",
            "frage": "Was ist ein Kritikpunkt am Münchener Klimaplan?",
            "optionen": [
                "a) Er sei zu ambitioniert und technisch nicht realisierbar.",
                "b) Pendler ohne Alternativen könnten benachteiligt werden.",
                "c) Der Plan koste zu viel Steuergeld.",
            ],
            "correct": "b",
        },
        {
            "titel": "Meldung 2 — Zweisprachigkeit",
            "frage": "Was zeigt die Studie der Humboldt-Universität?",
            "optionen": [
                "a) Zweisprachigkeit führt garantiert zu besserem Schulerfolg.",
                "b) Zweisprachige Kinder zeigen tendenziell bessere kognitive Leistungen.",
                "c) Einsprachige Kinder sind in Mathematik besser.",
            ],
            "correct": "b",
        },
        {
            "titel": "Meldung 3 — Deutsche Bahn",
            "frage": "Was ist beim Bahnprogramm noch unklar?",
            "optionen": [
                "a) Welche Technologie eingesetzt werden soll.",
                "b) Ob die nötigen Mittel zur Verfügung stehen.",
                "c) Bis wann die Umstellung abgeschlossen sein soll.",
            ],
            "correct": "b",
        },
    ]

    answers = []
    for n in nachrichten:
        st.markdown(f"**{n['titel']}** — {n['frage']}")
        ans = st.radio("", n["optionen"], key=f"ht2_radio_{n['titel']}", index=None, label_visibility="collapsed")
        answers.append(ans)

    if st.button("Vérifier mes réponses", key="ht2_check"):
        score = 0
        for i, (ans, n) in enumerate(zip(answers, nachrichten)):
            corr_text = next(o for o in n["optionen"] if o.startswith(n["correct"] + ")"))
            if ans is not None and ans.startswith(n["correct"] + ")"):
                st.success(f"**{n['titel']}** : Correct ✓")
                score += 1
            elif ans is not None:
                st.error(f"**{n['titel']}** : Incorrect — réponse correcte : *{corr_text}*")
            else:
                st.warning(f"**{n['titel']}** : Non répondu — réponse correcte : *{corr_text}*")
        st.metric("Score", f"{score} / 3")


def exercices_b2_hoeren():
    st.header("Hören — Compréhension orale B2 (transcripts)")
    st.info("Les exercices d'écoute sont simulés avec des transcriptions. Lisez le transcript comme si vous l'écoutiez, puis répondez aux questions.")
    teil = st.radio(
        "Choisir un exercice :",
        ["Teil 1 — Radiosendung (Interview)", "Teil 2 — Kurze Nachrichten"],
        key="hoeren_teil_select"
    )
    st.divider()
    if teil == "Teil 1 — Radiosendung (Interview)":
        _hoeren_teil1()
    elif teil == "Teil 2 — Kurze Nachrichten":
        _hoeren_teil2()


# ============================================================

def _grammatik_konjunktiv2():
    st.subheader("Konjunktiv II")

    st.markdown("#### Exercice 1 — würde + Infinitiv")
    st.write("Transformez chaque phrase en utilisant le Konjunktiv II avec *würde*.")

    phrases = [
        ("Ich lerne mehr Deutsch.", "Ich würde mehr Deutsch lernen."),
        ("Sie nimmt das Angebot an.", "Sie würde das Angebot annehmen."),
        ("Wir fahren nach Berlin.", "Wir würden nach Berlin fahren."),
        ("Er hilft mir dabei.", "Er würde mir dabei helfen."),
        ("Du sagst die Wahrheit.", "Du würdest die Wahrheit sagen."),
        ("Ihr kommt früher.", "Ihr würdet früher kommen."),
    ]
    with st.expander("📝 Voir les corrections — würde + Infinitiv"):
        for ind, cor in phrases:
            st.markdown(f"- *{ind}* → **{cor}**")

    st.markdown("#### Exercice 2 — Konjunktiv II Vergangenheit (hätte/wäre + Partizip II)")
    st.write("Choisissez la bonne forme du Konjunktiv II du passé.")

    kv_fragen = [
        (
            "Wenn ich mehr Zeit ___ (haben), hätte ich das Buch gelesen.",
            ["gehabt hätte", "hatte gehabt", "hätte gehabt", "gehabt hat"],
            "gehabt hätte",
        ),
        (
            "Sie ___ nicht ___ (kommen), wenn sie gewusst hätte, wie schwierig es war.",
            ["wäre … gekommen", "hätte … gekommen", "war … gekommen", "wurde … gekommen"],
            "wäre … gekommen",
        ),
        (
            "Wir ___ die Prüfung ___ (bestehen), wenn wir fleißiger gelernt hätten.",
            ["hätten … bestanden", "wären … bestanden", "haben … bestanden", "hatten … bestanden"],
            "hätten … bestanden",
        ),
        (
            "Er ___ Arzt ___ (werden), wenn er Biologie studiert hätte.",
            ["wäre … geworden", "hätte … geworden", "wurde … geworden", "war … geworden"],
            "wäre … geworden",
        ),
    ]
    kv_answers = []
    for i, (phrase, opts, _) in enumerate(kv_fragen):
        st.write(f"**{i+1}.** {phrase}")
        ans = st.selectbox("Forme correcte :", opts, key=f"gr_kv2_{i}", index=None)
        kv_answers.append(ans)

    if st.button("Vérifier", key="gr_kv2_check"):
        score = 0
        for i, (ans, (_, _, correct)) in enumerate(zip(kv_answers, kv_fragen)):
            if ans == correct:
                st.success(f"**{i+1}** : Correct ✓ — *{correct}*")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}**")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}**")
        st.metric("Score", f"{score} / {len(kv_fragen)}")

    st.markdown("#### Exercice 3 — Konjunktiv II : formule de politesse")
    st.write("Quelle est la formulation la plus polie ?")

    politesse = [
        (
            "Demander une faveur",
            ["a) Hilf mir!", "b) Könntest du mir helfen?", "c) Du sollst mir helfen."],
            "b",
        ),
        (
            "Faire une suggestion",
            ["a) Wir gehen ins Kino.", "b) Wir gehen ins Kino, oder?", "c) Wir könnten ins Kino gehen."],
            "c",
        ),
        (
            "Exprimer un souhait",
            ["a) Ich will mehr schlafen.", "b) Ich bräuchte mehr Schlaf.", "c) Ich muss mehr schlafen."],
            "b",
        ),
    ]
    pol_answers = []
    for i, (ctx, opts, _) in enumerate(politesse):
        st.write(f"**{i+1}. Situation :** {ctx}")
        ans = st.radio("", opts, key=f"gr_pol_{i}", index=None, label_visibility="collapsed")
        pol_answers.append(ans)

    if st.button("Vérifier", key="gr_pol_check"):
        score = 0
        for i, (ans, (_, opts, correct)) in enumerate(zip(pol_answers, politesse)):
            corr_text = next(o for o in opts if o.startswith(correct + ")"))
            if ans is not None and ans.startswith(correct + ")"):
                st.success(f"**{i+1}** : Correct ✓")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : *{corr_text}*")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : *{corr_text}*")
        st.metric("Score", f"{score} / {len(politesse)}")


def _grammatik_passiv():
    st.subheader("Passiv")

    st.markdown("#### Exercice 1 — Aktiv → Vorgangspassiv")
    st.write("Choisissez la transformation passive correcte.")

    aktiv_passiv = [
        (
            "Die Arbeiter bauen das Haus.",
            ["Das Haus wird von den Arbeitern gebaut.",
             "Das Haus wurde von den Arbeitern gebaut.",
             "Das Haus ist von den Arbeitern gebaut worden."],
            "Das Haus wird von den Arbeitern gebaut.",
        ),
        (
            "Man hat das Gesetz geändert.",
            ["Das Gesetz wird geändert.",
             "Das Gesetz wurde geändert.",
             "Das Gesetz ist geändert."],
            "Das Gesetz wurde geändert.",
        ),
        (
            "Die Ärztin untersucht den Patienten.",
            ["Der Patient wird von der Ärztin untersucht.",
             "Der Patient wurde von der Ärztin untersucht.",
             "Der Patient ist von der Ärztin untersucht worden."],
            "Der Patient wird von der Ärztin untersucht.",
        ),
    ]
    ap_answers = []
    for i, (aktiv, opts, _) in enumerate(aktiv_passiv):
        st.write(f"**{i+1}.** *{aktiv}*")
        ans = st.radio("Passivform :", opts, key=f"gr_ap_{i}", index=None)
        ap_answers.append(ans)

    if st.button("Vérifier", key="gr_ap_check"):
        score = 0
        for i, (ans, (_, _, correct)) in enumerate(zip(ap_answers, aktiv_passiv)):
            if ans == correct:
                st.success(f"**{i+1}** : Correct ✓ — *{correct}*")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}**")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}**")
        st.metric("Score", f"{score} / {len(aktiv_passiv)}")

    st.markdown("#### Exercice 2 — Vorgangspassiv vs. Zustandspassiv")
    st.write("Choisissez le bon type de passif (*wird...* = action en cours / *ist...* = état résultant).")

    vz_fragen = [
        ("Das Auto ___ gerade repariert.", "Vorgangspassiv (wird … repariert)", "Zustandspassiv (ist … repariert)"),
        ("Die Tür ___ bereits geschlossen.", "Zustandspassiv (ist … geschlossen)", "Vorgangspassiv (wird … geschlossen)"),
        ("Ein neues Museum ___ im Zentrum gebaut.", "Vorgangspassiv (wird … gebaut)", "Zustandspassiv (ist … gebaut)"),
        ("Der Brief ___ schon unterschrieben.", "Zustandspassiv (ist … unterschrieben)", "Vorgangspassiv (wird … unterschrieben)"),
    ]
    vz_answers = []
    for i, (phrase, correct, wrong) in enumerate(vz_fragen):
        st.write(f"**{i+1}.** {phrase}")
        opts = [correct, wrong]
        ans = st.radio("", opts, key=f"gr_vz_{i}", index=None, label_visibility="collapsed")
        vz_answers.append((ans, correct))

    if st.button("Vérifier", key="gr_vz_check"):
        score = 0
        for i, (ans, correct) in enumerate(vz_answers):
            if ans == correct:
                st.success(f"**{i+1}** : Correct ✓ — *{correct}*")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}**")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}**")
        st.metric("Score", f"{score} / {len(vz_fragen)}")

    st.markdown("#### Exercice 3 — Passiv mit Modalverb")
    st.write("Choisissez le verbe modal qui convient au contexte.")

    modal_fragen = [
        (
            "Dieses Problem ___ sofort gelöst werden.",
            ["muss", "darf", "mag"],
            "muss",
            "Obligation → *muss*",
        ),
        (
            "Die Hausaufgaben ___ bis Montag abgegeben werden.",
            ["sollen", "wollen", "mögen"],
            "sollen",
            "Instruction → *sollen*",
        ),
        (
            "In der Bibliothek ___ nicht laut gesprochen werden.",
            ["darf", "soll", "muss"],
            "darf",
            "Interdiction → *darf nicht*",
        ),
    ]
    modal_answers = []
    for i, (phrase, opts, _, _) in enumerate(modal_fragen):
        st.write(f"**{i+1}.** {phrase}")
        ans = st.radio("", opts, key=f"gr_modal_{i}", index=None, label_visibility="collapsed")
        modal_answers.append(ans)

    if st.button("Vérifier", key="gr_modal_check"):
        score = 0
        for i, (ans, (_, _, correct, expl)) in enumerate(zip(modal_answers, modal_fragen)):
            if ans == correct:
                st.success(f"**{i+1}** : Correct ✓ — {expl}")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}** ({expl})")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}** ({expl})")
        st.metric("Score", f"{score} / {len(modal_fragen)}")


def _grammatik_relativsaetze():
    st.subheader("Relativsätze")

    st.markdown("#### Exercice 1 — Relativpronomen wählen")
    st.write("Choisissez le bon pronom relatif.")

    rel_fragen = [
        (
            "Das Buch, ___ ich dir empfohlen habe, war sehr interessant.",
            ["das", "der", "die", "dem"],
            "das",
            "Buch = neutre, accusatif → *das*",
        ),
        (
            "Der Mann, ___ Auto gestohlen wurde, wohnt nebenan.",
            ["dessen", "dem", "der", "den"],
            "dessen",
            "Génitif masculin → *dessen*",
        ),
        (
            "Die Studentin, ___ wir gestern geholfen haben, heißt Mia.",
            ["der", "die", "deren", "denen"],
            "der",
            "Frau, datif → *der*",
        ),
        (
            "Ich kenne jemanden, ___ dir bei diesem Problem helfen kann.",
            ["der", "die", "das", "dem"],
            "der",
            "*jemand* → masculin, nominatif → *der*",
        ),
        (
            "Das ist die Stadt, ___ ich geboren wurde.",
            ["in der", "in die", "wo", "in der / wo"],
            "in der",
            "Préposition *in* + datif féminin → *in der* (forme soutenue)",
        ),
    ]
    rel_answers = []
    for i, (phrase, opts, _, _) in enumerate(rel_fragen):
        st.write(f"**{i+1}.** {phrase}")
        ans = st.selectbox("Pronom relatif :", opts, key=f"gr_rel_{i}", index=None)
        rel_answers.append(ans)

    if st.button("Vérifier", key="gr_rel_check"):
        score = 0
        for i, (ans, (_, _, correct, expl)) in enumerate(zip(rel_answers, rel_fragen)):
            if ans == correct:
                st.success(f"**{i+1}** : Correct ✓ — {expl}")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}** ({expl})")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}** ({expl})")
        st.metric("Score", f"{score} / {len(rel_fragen)}")

    st.markdown("#### Exercice 2 — Relative avec préposition")
    st.write("Reformulez en utilisant une proposition relative avec préposition. Comparez avec la correction modèle.")

    rel_prep = [
        (
            "Ich denke oft an das Gespräch. Wir haben das Gespräch gestern geführt.",
            "Das Gespräch, an das ich oft denke, haben wir gestern geführt.",
        ),
        (
            "Er arbeitet in einem Büro. Das Büro hat keine Fenster.",
            "Das Büro, in dem er arbeitet, hat keine Fenster.",
        ),
        (
            "Sie hat einen Freund. Mit diesem Freund reist sie jedes Jahr.",
            "Der Freund, mit dem sie jedes Jahr reist, wohnt in Hamburg.",
        ),
    ]
    for i, (phrases, _) in enumerate(rel_prep):
        st.write(f"**{i+1}.** {phrases}")
        st.text_area("Votre réponse :", key=f"gr_relp_{i}", height=80)

    with st.expander("📝 Voir les corrections"):
        for i, (_, corr) in enumerate(rel_prep):
            st.markdown(f"**{i+1}.** {corr}")

    st.markdown("#### Exercice 3 — Quelle phrase est grammaticalement correcte ?")

    syn_fragen = [
        (
            ["a) Ein Student, der fleißig lernt, hat Erfolg.",
             "b) Ein Student, das fleißig lernt, hat Erfolg.",
             "c) Ein Student, dem fleißig lernt, hat Erfolg."],
            "a",
            "*Student* = masculin, nominatif → *der*",
        ),
        (
            ["a) Die Freunde, mit denen ich reise, sind zuverlässig.",
             "b) Die Freunde, mit die ich reise, sind zuverlässig.",
             "c) Die Freunde, mit der ich reise, sind zuverlässig."],
            "a",
            "Pluriel datif avec *mit* → *denen*",
        ),
        (
            ["a) Das Hotel, in dem wir übernachten, ist schön.",
             "b) Das Hotel, in das wir übernachten, ist schön.",
             "c) Das Hotel, das wir übernachten, ist schön."],
            "a",
            "*übernachten in* + datif → *in dem* (neutre datif)",
        ),
    ]
    syn_answers = []
    for i, (opts, _, _) in enumerate(syn_fragen):
        st.write(f"**{i+1}.** Quelle phrase est correcte ?")
        ans = st.radio("", opts, key=f"gr_syn_{i}", index=None, label_visibility="collapsed")
        syn_answers.append(ans)

    if st.button("Vérifier", key="gr_syn_check"):
        score = 0
        for i, (ans, (opts, correct, expl)) in enumerate(zip(syn_answers, syn_fragen)):
            corr_text = next(o for o in opts if o.startswith(correct + ")"))
            if ans is not None and ans.startswith(correct + ")"):
                st.success(f"**{i+1}** : Correct ✓ — {expl}")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : *{corr_text}* ({expl})")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : *{corr_text}* ({expl})")
        st.metric("Score", f"{score} / {len(syn_fragen)}")


def _grammatik_konnektoren():
    st.subheader("Konnektoren")

    st.markdown("#### Exercice 1 — Konnektoren einsetzen")
    st.write("Complétez avec le connecteur approprié. **Banque de mots :** *obwohl, sodass, damit, nachdem, wohingegen, je … desto*")

    konn_fragen = [
        ("___ er sehr müde war, arbeitete er weiter.", "obwohl", "Concession → *obwohl* + verbe en fin de subordonnée"),
        ("Sie sprach sehr laut, ___ alle sie hören konnten.", "sodass", "Conséquence → *sodass*"),
        ("Ich lerne Deutsch, ___ ich in Deutschland studieren kann.", "damit", "But → *damit* (différent sujet)"),
        ("Er ging nach Hause, ___ er seine Aufgaben erledigt hatte.", "nachdem", "Antériorité → *nachdem* + Plusquamperfekt"),
        ("Männer interessieren sich oft für Technik, ___ Frauen eher soziale Berufe bevorzugen.", "wohingegen", "Opposition → *wohingegen*"),
        ("___ mehr ich lerne, ___ besser werde ich.", "je … desto", "Proportionnalité → *je … desto*"),
    ]
    word_bank = ["— wählen —", "obwohl", "sodass", "damit", "nachdem", "wohingegen", "je … desto"]
    konn_answers = []
    for i, (phrase, _, _) in enumerate(konn_fragen):
        st.write(f"**{i+1}.** {phrase}")
        ans = st.selectbox("Connecteur :", word_bank, key=f"gr_konn_{i}")
        konn_answers.append(ans)

    if st.button("Vérifier", key="gr_konn_check"):
        score = 0
        for i, (ans, (_, correct, expl)) in enumerate(zip(konn_answers, konn_fragen)):
            if ans == correct:
                st.success(f"**{i+1}** : Correct ✓ — {expl}")
                score += 1
            elif ans != "— wählen —":
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}** ({expl})")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}** ({expl})")
        st.metric("Score", f"{score} / {len(konn_fragen)}")

    st.markdown("#### Exercice 2 — Ordre des mots dans la subordonnée")
    st.write("Choisissez la phrase avec la syntaxe correcte.")

    ordre_fragen = [
        (
            ["a) Obwohl es regnet, ich bleibe zuhause.",
             "b) Obwohl es regnet, bleibe ich zuhause.",
             "c) Obwohl es regnet, zuhause ich bleibe."],
            "b",
            "Après une subordonnée, inversion sujet-verbe en proposition principale.",
        ),
        (
            ["a) Damit du bestehst, musst du mehr lernen.",
             "b) Damit du bestehst, mehr lernen musst du.",
             "c) Damit du bestehst, du musst mehr lernen."],
            "a",
            "Même règle : verbe conjugué en position 2 dans la principale.",
        ),
        (
            ["a) Nachdem er gegessen hat, er macht Hausaufgaben.",
             "b) Nachdem er gegessen hat, macht er Hausaufgaben.",
             "c) Nachdem er gegessen hat, er Hausaufgaben macht."],
            "b",
            "Inversion sujet-verbe obligatoire après la subordonnée.",
        ),
    ]
    ordre_answers = []
    for i, (opts, _, _) in enumerate(ordre_fragen):
        st.write(f"**{i+1}.** Quelle phrase est correcte ?")
        ans = st.radio("", opts, key=f"gr_ordre_{i}", index=None, label_visibility="collapsed")
        ordre_answers.append(ans)

    if st.button("Vérifier", key="gr_ordre_check"):
        score = 0
        for i, (ans, (opts, correct, expl)) in enumerate(zip(ordre_answers, ordre_fragen)):
            corr_text = next(o for o in opts if o.startswith(correct + ")"))
            if ans is not None and ans.startswith(correct + ")"):
                st.success(f"**{i+1}** : Correct ✓ — {expl}")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : *{corr_text}* ({expl})")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : *{corr_text}* ({expl})")
        st.metric("Score", f"{score} / {len(ordre_fragen)}")

    st.markdown("#### Exercice 3 — *obwohl* vs *trotzdem* vs *obgleich*")
    st.write("Choisissez le connecteur le plus approprié.")

    nuance_fragen = [
        (
            "___ ich ihm erklärt habe, wie man es macht, versteht er es nicht.",
            ["Obwohl", "Trotzdem", "Weil"],
            "Obwohl",
            "*Obwohl* introduit une subordonnée (verbe en fin). *Trotzdem* connecte deux propositions principales.",
        ),
        (
            "Ich war müde. ___ bin ich ins Training gegangen.",
            ["Obwohl", "Trotzdem", "Damit"],
            "Trotzdem",
            "*Trotzdem* = adverbe, relie deux propositions principales. Verbe conjugué en position 2 après.",
        ),
        (
            "Sie hat hart gearbeitet, ___ ihr Chef sie nie gelobt hat.",
            ["obwohl", "trotzdem", "sodass"],
            "obwohl",
            "*obwohl* en proposition subordonnée enchâssée dans la phrase.",
        ),
    ]
    nuance_answers = []
    for i, (phrase, opts, _, _) in enumerate(nuance_fragen):
        st.write(f"**{i+1}.** {phrase}")
        ans = st.radio("", opts, key=f"gr_nuance_{i}", index=None, label_visibility="collapsed")
        nuance_answers.append(ans)

    if st.button("Vérifier", key="gr_nuance_check"):
        score = 0
        for i, (ans, (_, _, correct, expl)) in enumerate(zip(nuance_answers, nuance_fragen)):
            if ans == correct:
                st.success(f"**{i+1}** : Correct ✓ — {expl}")
                score += 1
            elif ans is not None:
                st.error(f"**{i+1}** : Incorrect — réponse correcte : **{correct}** — {expl}")
            else:
                st.warning(f"**{i+1}** : Non répondu — réponse correcte : **{correct}** — {expl}")
        st.metric("Score", f"{score} / {len(nuance_fragen)}")


def exercices_b2_grammatik():
    st.header("Grammatik B2")
    thema = st.radio(
        "Choisir un thème :",
        ["Konjunktiv II", "Passiv", "Relativsätze", "Konnektoren"],
        key="grammatik_thema_select"
    )
    st.divider()
    if thema == "Konjunktiv II":
        _grammatik_konjunktiv2()
    elif thema == "Passiv":
        _grammatik_passiv()
    elif thema == "Relativsätze":
        _grammatik_relativsaetze()
    elif thema == "Konnektoren":
        _grammatik_konnektoren()


def exercices_b2():
    st.title("Exercices B2 — Goethe-Zertifikat B2")
    st.markdown(
        "Ces exercices s'inspirent du format officiel du **Goethe-Zertifikat B2**. "
        "Chaque module correspond à une partie de l'examen réel."
    )
    module = st.sidebar.radio(
        "Module B2",
        ["Lesen", "Schreiben", "Hören", "Grammatik B2"],
        key="b2_module_select"
    )
    if module == "Lesen":
        exercices_b2_lesen()
    elif module == "Schreiben":
        exercices_b2_schreiben()
    elif module == "Hören":
        exercices_b2_hoeren()
    elif module == "Grammatik B2":
        exercices_b2_grammatik()


# Fonction principale pour structurer l'application
def main():
    st.title("Eya learning 3000 - Apprenez la Grammaire Allemande 🌭")
    
    menu = ["Accueil", "Leçons de grammaire", "Exercices", "Tableau de conjugaison", "Exos_infini", "Exercices B2 - Goethe"]
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

    elif choix == "Exercices B2 - Goethe":
        exercices_b2()
if __name__ == "__main__":
    main()
