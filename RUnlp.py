'''
Step 1: Importing all necessary modules
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
import re
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from nltk import word_tokenize

print('Wait Model is learning...')

'''
Step 2: Import Dataset
'''
dataset = pd.read_csv('Roman Urdu DataSet.csv', names=['comment', 'sentiment', 'nan'])

'''
Step 3: Lets have a look at our data set
'''

Pos = dataset[dataset['sentiment'] == 'Positive'].shape[0]
Neg = dataset[dataset['sentiment'] == 'Negative'].shape[0]
Neu = dataset[dataset['sentiment'] == 'Neutral'].shape[0]
plt.bar(10,Pos,3, label="Positve")
plt.bar(15,Neg,3, label="Negative")
plt.bar(20,Neu,3, label="Neutral")
plt.legend()
plt.ylabel('Number of examples')
plt.title('Proportion of examples')
plt.show()

'''
Step 4: We have y in form of categorical data
'''
y = dataset['sentiment']


'''
Step 5: Cleaning
'''
# created user defined stopwords
stopwords=['ai', 'ayi', 'hy', 'hai', 'main', 'ki', 'tha', 'koi', 'ko', 'sy', 'woh', 'bhi', 'aur', 'wo', 'yeh', 'rha', 'hota', 'ho', 'ga', 'ka', 'le', 'lye', 'kr', 'kar', 'lye', 'liye', 'hotay', 'waisay', 'gya', 'gaya', 'kch', 'ab', 'thy', 'thay', 'houn', 'hain', 'han', 'to', 'is', 'hi', 'jo', 'kya', 'thi', 'se', 'pe', 'phr', 'wala', 'waisay', 'us', 'na', 'ny', 'hun', 'rha', 'raha', 'ja', 'rahay', 'abi', 'uski', 'ne', 'haan', 'acha', 'nai', 'sent', 'photo', 'you', 'kafi', 'gai', 'rhy', 'kuch', 'jata', 'aye', 'ya', 'dono', 'hoa', 'aese', 'de', 'wohi', 'jati', 'jb', 'krta', 'lg', 'rahi', 'hui', 'karna', 'krna', 'gi', 'hova', 'yehi', 'jana', 'jye', 'chal', 'mil', 'tu', 'hum', 'par', 'hay', 'kis', 'sb', 'gy', 'dain', 'krny', 'tou']

def clean(x):
    review_with_no_special_character = re.sub('[^a-zA-Z]',' ',str(x))
    review_in_lowercase = review_with_no_special_character.lower()
    review_in_tokens = word_tokenize(review_in_lowercase)
    review_with_no_stopwords = [word for word in review_in_tokens if not word in stopwords]
    review_in_sentence = ' '.join(review_with_no_stopwords)
    return review_in_sentence

dataset['comment'] = dataset['comment'].apply(lambda x:clean(x))

X = dataset['comment']
