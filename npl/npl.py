import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk

messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]
print(messages[0])
print(messages[1])
print(messages[2])

for number, message in enumerate(messages[:15]):
    print(number, message)
    print('\n')


messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t', names={'label', 'message'})

print(messages.head())
print(messages.describe())

#print(messages.groupby('label').describe())

messages['length'] = messages['message'].apply(len)
print(messages.head())

messages['length'].plot(kind='hist', bins = 150)
plt.show()

messages.hist(bins=150, column = 'length',by='label')
plt.show()
