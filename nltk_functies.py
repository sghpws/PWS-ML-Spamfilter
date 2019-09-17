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
# FUNCTIES VOOR TEXT FILTERING

# 1. splitst woorden en leestekens uit een string(tekst) en zet deze als elementen in een lijst
tekst = " call me if you have any questions. i will work to get the revised estimates work into pops today. "
spl = word_tokenize(tekst)

print(spl)

# 2. filtert alle leestekens uit de lijst en maakt een nieuwe lijst met alleen de woorden
leesteken = string.punctuation
clean_tekst = []
for element in spl:
    if element not in leesteken:
        clean_tekst.append(element)

print(clean_tekst)

# 3. geeft de woordsoorten van woorden in een string(clean_tekst), website voor de betekenissen:
# https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# dit werkt alleen voor strings in het Engels,
# nltk.help.upenn_tagset() , dit print een helppagina hiervoor
woordsoort = nltk.pos_tag(clean_tekst)
print(woordsoort)

# 4. filtert alle stopwoorden die niet belangrijk zijn uit een string
# en maakt een lijst van alleen de belangrijke woorden
stopw = set(stopwords.words('english'))
useful_words = []
for word in clean_tekst:
    if word not in stopw:
        useful_words.append(word)



print(useful_words)

#print(movie_reviews.words())
# freq_dist = nltk.FreqDist(filmreviews)
# print(freq_dist.most_common(50))

# print(type(filmreviews))



def create_word_features():
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

#print(create_word_features())

neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = (movie_reviews.words(fileid))
    neg_reviews.append((create_word_features(words), "negative"))

print(neg_reviews[0])
print(len(neg_reviews))
