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

'''
Step 6: Split data set into training and testing sets
'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)

'''
Step 6: convert a collection of raw documents to a matrix
'''
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_vector = vectorizer.fit_transform(X_train)
X_test_vector = vectorizer.transform(X_test)

'''
Step 8: Creating classifier and fitting data in classifier
'''
from sklearn.svm import SVC
classifier = SVC(kernel='linear', C=1.0, degree=3, random_state=0)
classifier.fit(X_train_vector, y_train)

'''
Step 9 : Pickling the Model
'''
import pickle
#To reuse, we can dump the model and load whenever or where-ever you want. 
#Vocabulary is also needed to vectorize the new documents while predicting the label.

# pickling the vectorizer
pickle.dump(vectorizer, open('vectorizer.sav', 'wb'))
# pickling the model
pickle.dump(classifier, open('classifier.sav', 'wb'))

'''
Step 9: Perform Prediction
'''
y_pred=classifier.predict(X_test_vector)

'''
Step 10: Create Confusion Matrix
'''
ConfusionMatrix=confusion_matrix(y_test, y_pred)

'''
Step 11: Evaluation
'''

Accuracy = format(classifier.score(X_test_vector, y_test)*100, '.2f')+ ' %'
file = open('AccuracyPercentage', 'wb')
pickle.dump(Accuracy, file)
file.close()

print('Learning end')

#visualizing confusion matrix

labels=['Positive','Neutral','Negative']
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(ConfusionMatrix)
plt.title('Confusion matrix of the classifier \n')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
"""
#classifier1
classifier=LogisticRegression(random_state=0,solver='liblinear',multi_class='ovr')
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)
print(y_pred)

#confusion matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)

#accuracy of LogisticRegression
print('Accuracy is {} '.format(accuracy_score(y_test, y_pred)))


labels=['Positive','Neutral','Negative']
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(cm)
plt.title('Confusion matrix of the classifier \n')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()

"""
