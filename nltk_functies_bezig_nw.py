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

# FUNCTIES VOOR TEXT FILTERING

tekst = "Call me if you have any questions 6 . i will 100 76 work to get the revised estimates work into pops today."
print(tekst)

# 1. zorgt ervoor dat alle letters in lowercase zijn, dat is de manier hoe de functies de string(tekst) verwachten
lowercase_functie = tekst.lower()
print(lowercase_functie)

# 2. splitst woorden en leestekens uit een string(tekst) en zet deze als elementen in een lijst
split_functie = word_tokenize(lowercase_functie)
print(split_functie)

# 3. filtert alle leestekens uit de lijst en maakt een nieuwe lijst met alleen de woorden
leesteken = string.punctuation
leesteken_functie = []
for element in split_functie:
    if element not in leesteken:
        leesteken_functie.append(element)

print(leesteken_functie)

# 4. geeft de woordsoorten van woorden in een string(clean_tekst), website voor de betekenissen:
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# dit werkt alleen voor strings in het Engels,
# nltk.help.upenn_tagset() , dit print een helppagina hiervoor
woordsoort_functie = nltk.pos_tag(leesteken_functie)
print(woordsoort_functie)

# 5. filtert alle stopwoorden die niet belangrijk zijn uit de lijst
# en maakt een lijst van alleen de belangrijke woorden
stopw = set(stopwords.words('english'))
stopwoorden_functie = []
for word in leesteken_functie:
    if word not in stopw:
        stopwoorden_functie.append(word)

print(stopwoorden_functie)

#6. filtert alle getallen uit de lijst en vervangt deze voor het woord "getal"
for q in stopwoorden_functie:
    a = stopwoorden_functie.index(q)
    if q.isdigit():
        stopwoorden_functie[a] = "getal"

print(stopwoorden_functie)