# ALLE NLTK IMPORTS

import nltk.classify.util
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import movie_reviews
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from string import digits
import locale

# FUNCTIES VOOR TEXT FILTERING

tekst = " Call me if you have any questions 6$ . i will  € € 100 £ 76 € work to get the revised estimates work into pops today."
print(tekst)

# 1. zorgt ervoor dat alle letters in lowercase zijn, dat is de manier hoe de functies de string(tekst) verwachten
tekst = tekst.lower()
print(tekst)

# 2. splitst woorden en leestekens uit een string(tekst) en zet deze als elementen in de lijst (lijst_met_woorden)
lijst_met_woorden = word_tokenize(tekst)
print(lijst_met_woorden)

#2.1 zorgt evoor dat alle currencies worden vervangen door het woord "geldteken"
 #hiervoor importeren we de codes voor currencies uit een package dat forex_python heet
 #de lijst heet CurrencyCodes

currencies = {'$', '€', '£', '¥', 'usd', 'eur', 'gbp', 'yen'}
for c in lijst_met_woorden:
    b = lijst_met_woorden.index(c)
    if c in currencies:
        lijst_met_woorden[b] = "geldteken"
print(" hieronder wordt lijst_met_woorden geprint zonder geldtekens")
print(lijst_met_woorden)

# 3. filtert alle leestekens uit de lijst en maakt een nieuwe lijst met alleen de woorden
leesteken = string.punctuation
for element in lijst_met_woorden:
    q = lijst_met_woorden.index(element)
    if element in leesteken:
        del lijst_met_woorden[q]
print(" hieronder wordt lijst_met_woorden geprint zonder leestekens")
print(lijst_met_woorden)

# 4. geeft de woordsoorten van woorden in een string(clean_tekst), website voor de betekenissen:
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# dit werkt alleen voor strings in het Engels,
# nltk.help.upenn_tagset() , dit print een helppagina hiervoor
woordsoort_functie = nltk.pos_tag(lijst_met_woorden)
print(" hieronder wordt lijst_met_woorden geprint met de woordsoort in het Engels erbij")
print(woordsoort_functie)

# 5. filtert alle stopwoorden die niet belangrijk zijn uit de lijst
# en maakt een lijst van alleen de belangrijke woorden
stopw = set(stopwords.words('english'))
for word in lijst_met_woorden:
    z = lijst_met_woorden.index(word)
    if word in stopw:
        del lijst_met_woorden[z]
print(" hieronder wordt lijst_met_woorden geprint zonder stopwoorden")
print(lijst_met_woorden)

#6. filtert alle getallen uit de lijst en vervangt deze voor het woord "getal"
for q in lijst_met_woorden:
    a = lijst_met_woorden.index(q)
    if q.isdigit():
        lijst_met_woorden[a] = "getal"
print(" hieronder wordt lijst_met_woorden geprint zonder getallen")
print(lijst_met_woorden)

