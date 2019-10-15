# TEST ANALYSING GIRON-D DATA

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import time

start_time = time.time()

with open("giron_d.txt", "r") as f:
    data = f.read()


words = data.lower()
words = word_tokenize(words)
print(len(words))
stopw = set(stopwords.words())

useful_words = [element5 for element5 in words if element5 not in stopw]

leesteken = string.punctuation

lijst= [element3 for element3 in useful_words if element3 not in leesteken]

tekens = []


woordsoort_functie = nltk.pos_tag(lijst)
print(len(woordsoort_functie))


for gijs in lijst:
    for q in woordsoort_functie:
        if q == (gijs, 'POS') or q == (gijs, ':') or q == (gijs, '``'):
            tekens.append(gijs)

for caspar in lijst:
    d = lijst.index(caspar)
    for h in woordsoort_functie:
        if h == (caspar, 'CD'):
            lijst[d] = "getal"
print(tekens)

lijst = [element for element in lijst if element not in tekens]
frequency = nltk.FreqDist(lijst)

print(frequency.most_common(10))
