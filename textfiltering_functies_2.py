# FUNCTIES VOOR TEXT FILTERING

# ALLE IMPORTS
import string
import nltk.classify.util
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


tekst = " get your him free , @ < . /?#, adware scan and removal download 6$ gbp now. http : / / zk"
print(tekst)

# 1. zorgt ervoor dat alle letters in lowercase zijn, dat is de manier hoe de functies de string(tekst) verwachten
tekst = tekst.lower()
print(tekst)

# 2. splitst woorden en leestekens uit een string(tekst) en zet deze als elementen in de lijst (lijst_met_woorden)
lijst_met_woorden = word_tokenize(tekst)
print(lijst_met_woorden)

# 2.1 zorgt evoor dat alle currencies en valuta afkortingen in lijst_met_woorden
#     worden vervangen door het woord "geldteken"

currencies = {'$', '€', '£', '¥', 'usd', 'eur', 'gbp', 'yen'}
for c in lijst_met_woorden:
    b = lijst_met_woorden.index(c)
    if c in currencies:
        lijst_met_woorden[b] = "geldteken"

print(" hieronder wordt lijst_met_woorden geprint zonder geldtekens")
print(lijst_met_woorden)


# 3. filtert alle leestekens uit de lijst en zorgt ervoor dat lijst_met_woorden alleen uit woorden bestaat
leesteken = string.punctuation

lijst_met_woorden = [element3 for element3 in lijst_met_woorden if element3 not in leesteken]
print("hieronder wordt lijst_met_woorden geprint zonder leestekens")
print(lijst_met_woorden)


# 4. geeft de woordsoorten van woorden in een lijst_met_woorden, website voor de betekenissen:
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# dit werkt alleen voor strings in het Engels,
# nltk.help.upenn_tagset() , dit print een helppagina hiervoor
woordsoort_functie = nltk.pos_tag(lijst_met_woorden)

print(" hieronder wordt lijst_met_woorden geprint met de woordsoort in het Engels erbij")
print(woordsoort_functie)


# 5. filtert alle stopwoorden die niet belangrijk zijn uit lijst_met_woorden
#    en zo wordt er alleen doorgegaan met de belangrijke woorden,
#    element5 wordt als een variabele beschouwd, dit is dus een element uit lijst_met_woorden
stopw = set(stopwords.words())

lijst_met_woorden = [element5 for element5 in lijst_met_woorden if element5 not in stopw]
print(" hieronder wordt lijst_met_woorden geprint zonder stopwoorden")
print(lijst_met_woorden)


# 6. filtert alle getallen uit lijst_met_woorden en vervangt deze voor het woord "getal"
for po in lijst_met_woorden:
    a = lijst_met_woorden.index(po)
    if po.isdigit():
        lijst_met_woorden[a] = "getal"
print(" hieronder wordt lijst_met_woorden geprint zonder getallen")
print(lijst_met_woorden)

# 7. filter website adressen, (nog niet compleet)
website_kenmerken = {'http', '.com'}
for r in lijst_met_woorden:
    ne = lijst_met_woorden.index(r)
    if r in website_kenmerken:
        lijst_met_woorden[ne] = "websiteadres"
