# SPAMFILTER ENRON DATA MET NAIVE BAYES CLASSIFIER

# ALLE IMPORTS

import os
import string
import time
import random

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
import nltk.classify.util

start_time = time.time()

mail_data = "<plak hier de padnaam voor de Enron data, verwijder de <> tekens >"


ham_list = []

spam_list = []

for directory, subdirectory, filenames in os.walk(mail_data):
    if os.path.split(directory)[1] == 'ham':
        print(directory, subdirectory, len(filenames))
        for file in filenames:
            with open(os.path.join(directory, file), encoding="latin-1") as f:
                data = f.read()

                # tekst filter functie, data wordt omgezet naar tekst met alleen kleine letters
                tekst = data.lower()
                # tekst filter functie, elk woord uit tekst wordt als element toegevoegd aan lijst_met_woorden
                lijst_met_woorden = word_tokenize(tekst)

                # tekst filter functie 1
                currencies = {'$', '€', '£', '¥', 'usd', 'eur', 'gbp', 'yen'}
                for element1 in lijst_met_woorden:
                    index_element1 = lijst_met_woorden.index(element1)
                    if element1 in currencies:
                        lijst_met_woorden[index_element1] = "geldteken"
                # tekst filter functie 2
                for element2 in lijst_met_woorden:
                    index_element2 = lijst_met_woorden.index(element2)
                    if element2.isdigit():
                        lijst_met_woorden[index_element2] = "getal"
                # tekst filter functie 3
                leesteken = string.punctuation
                lijst_met_woorden = [element3 for element3 in lijst_met_woorden if element3 not in leesteken]
                # tekst filter functie 4
                stopw = set(stopwords.words())
                lijst_met_woorden = [element4 for element4 in lijst_met_woorden if element4 not in stopw]
                # tekst filter functie 5
                lijst_met_woorden = {element5: True for element5 in lijst_met_woorden}

                ham_list.append((lijst_met_woorden, "ham"))

    if os.path.split(directory)[1] == 'spam':
        print(directory, subdirectory, len(filenames))
        for file in filenames:
            with open(os.path.join(directory, file), encoding="latin-1") as f:
                data = f.read()

                # tekst filter functie, data wordt omgezet naar tekst met alleen kleine letters
                data = data.lower()
                # tekst filter functie, elk woord uit tekst wordt als element toegevoegd aan lijst_met_woorden
                lijst_met_woorden = word_tokenize(data)

                # tekst filter functie 1
                currencies = {'$', '€', '£', '¥', 'usd', 'eur', 'gbp', 'yen'}
                for element1 in lijst_met_woorden:
                    index_element1 = lijst_met_woorden.index(element1)
                    if element1 in currencies:
                        lijst_met_woorden[index_element1] = "geldteken"
                # tekst filter functie 2
                for element2 in lijst_met_woorden:
                    index_element2 = lijst_met_woorden.index(element2)
                    if element2.isdigit():
                        lijst_met_woorden[index_element2] = "getal"
                # tekst filter functie 3
                leesteken = string.punctuation
                lijst_met_woorden = [element3 for element3 in lijst_met_woorden if element3 not in leesteken]
                # tekst filter functie
                stopw = set(stopwords.words())
                lijst_met_woorden = [element4 for element4 in lijst_met_woorden if element4 not in stopw]
                # tekst filter functie 5
                lijst_met_woorden = {element5: True for element5 in lijst_met_woorden}

                spam_list.append((lijst_met_woorden, "spam"))


combined_list = ham_list + spam_list

random.shuffle(combined_list)

training_part = int(len(combined_list) * 0.7)

training_set = combined_list[:training_part]
test_set = combined_list[training_part:]

classifier = NaiveBayesClassifier.train(training_set)

accuracy = nltk.classify.accuracy(classifier, test_set)

test_email = "<plak hier de padnaam naar een e-mail in een txt bestand verwijder de <> tekens>"

with open(test_email, "r") as f:
    file_data = f.read()


def mail_analyse(file_data):

    # tekst filter functie, data wordt omgezet naar tekst met alleen kleine letters
    file_data = file_data.lower()
    # tekst filter functie, elk woord uit tekst wordt als element toegevoegd aan lijst_met_woorden
    lijst_met_woorden = word_tokenize(file_data)

    # tekst filter functie 1
    currencies = {'$', '€', '£', '¥', 'usd', 'eur', 'gbp', 'yen'}
    for element1 in lijst_met_woorden:
        index_element1 = lijst_met_woorden.index(element1)
        if element1 in currencies:
            lijst_met_woorden[index_element1] = "geldteken"
    # tekst filter functie 2
    for element2 in lijst_met_woorden:
        index_element2 = lijst_met_woorden.index(element2)
        if element2.isdigit():
            lijst_met_woorden[index_element2] = "getal"
    # tekst filter functie 3
    leesteken = string.punctuation
    lijst_met_woorden = [element3 for element3 in lijst_met_woorden if element3 not in leesteken]
    # tekst filter functie 4
    woordsoort_functie = nltk.pos_tag(lijst_met_woorden)
    tekens = []
    for element4 in lijst_met_woorden:
        for ws_element4 in woordsoort_functie:
            if ws_element4 == (element4, 'POS') or ws_element4 == (element4, ':')\
                    or ws_element4 == (element4, '``'):
                tekens.append(element4)
    lijst_met_woorden = [element4 for element4 in lijst_met_woorden if element4 not in tekens]
    # tekst filter functie 5
    for element5 in lijst_met_woorden:
        index_element5 = lijst_met_woorden.index(element5)
        for ws_element5 in woordsoort_functie:
            if ws_element5 == (element5, 'CD'):
                lijst_met_woorden[index_element5] = "getal"
    # tekst filter functie 6
    stopw = set(stopwords.words())
    lijst_met_woorden = [element6 for element6 in lijst_met_woorden if element6 not in stopw]
    # tekst filter functie 7
    lijst_met_woorden = {element7: True for element7 in lijst_met_woorden}

    return lijst_met_woorden


gefilterde_mail = mail_analyse(file_data)


print("Eerste ham e-mail:")
print(ham_list[0], "\n")

print("Eerste spam e-mail: ")
print(spam_list[0], "\n")

print("Aantal e-mails in ham_list: ", len(ham_list))
print("Aantal e-mails in spam_list: ", len(spam_list), "\n")


print("Aantal e-mails in training data: ", len(training_set))
print("Aantal e-mails in test data: ", len(test_set))

print("Accuracy = ", accuracy * 100)
classifier.show_most_informative_features(10)

print("Test e-mail is:", classifier.classify(gefilterde_mail))

print("Running tijd is: ", "%s secondes " % (time.time() - start_time))
