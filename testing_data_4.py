# TEST ANALYSING KEN LAY DATA

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import time

start_time = time.time()

with open("ken_lay_emails.txt", "r") as f:
    data = f.read()


words = data.lower()
words = word_tokenize(words)

stopw = set(stopwords.words())

useful_words = [element5 for element5 in words if element5 not in stopw]

leesteken = string.punctuation

lijst = [element3 for element3 in useful_words if element3 not in leesteken]

frequency = nltk.FreqDist(lijst)

print(frequency.most_common(50))

print("--- %s seconds ---" % (time.time() - start_time))
