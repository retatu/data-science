import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]
print(messages[0])
print(messages[1])
print(messages[2])

for number, message in enumerate(messages[:15]):
    print(number, message)
    print('\n')


messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t', names={'message', 'label'})

print(messages.head())
print(messages.describe())

#print(messages.groupby('label').describe())

messages['length'] = messages['message'].apply(len)
print(messages.head())

messages['length'].plot(kind='hist', bins = 150)
plt.show()

messages.hist(bins=150, column = 'length',by='label')
plt.show()

mess = "Menssagem de exemplo: Teste."
sem_ponto = [char for char in mess if char not in string.punctuation]
print(sem_ponto) 
sem_ponto = ''.join(sem_ponto)
print(sem_ponto)

#Palavras comuns que não agregam muito.
print(stopwords.words('english'))

teste_string = 'Sample message! Notice: it has punctuation.'
msg_limpa = [word for word in teste_string.split() if word.lower not in stopwords.words('english')]
#Msg sem stopwords
print(msg_limpa)


def remover_pontos_stopword(msg):
    #Remove os pontos
    sem_pontos = [c for c in msg if c not in string.punctuation]
    sem_pontos = ''.join(sem_pontos)
    #Remove as stopwords
    sem_stop_words = [w for w in sem_pontos.split() if w.lower not in stopwords.words('english')]
    return sem_stop_words

#bow_transformer = CountVectorizer(analyzer=remover_pontos_stopword).fit(messages['message'])
#messages_bow = bow_transformer.transform([messages['message']])
#tfidf_transformer = TfidfTransformer()
#tfidf_transformer = tfidf_transformer.fit(messages_bow)
#messages_tfidf = tfidf_transformer.transform(messages_bow)
#spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])


msg_train, msg_test, label_train, label_test = train_test_split(messages['message'], messages['label'], test_size = 0.2)

pipeline = Pipeline([
    ('bow', CountVectorizer(analyzer = remover_pontos_stopword)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB()),
])

pipeline.fit(msg_train, label_train)
predictions = pipeline.predict(msg_test)
