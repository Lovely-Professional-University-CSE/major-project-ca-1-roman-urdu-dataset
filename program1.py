import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.utils import shuffle
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
# making corpus or words from comments
import re
from nltk.stem.porter import PorterStemmer
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
dataset = pd.read_csv('Roman Urdu DataSet.csv', names=['Comment', 'sentiment', 'nan'])

print(dataset.head())
print(dataset.shape)

Pos = dataset[dataset['sentiment'] == 'Positive'].shape[0]
Neg = dataset[dataset['sentiment'] == 'Negative'].shape[0]
Neu = dataset[dataset['sentiment'] == 'Neutral'].shape[0]
# bar plot of the 3 classes
plt.bar(10,Pos,3, label="Positve")
plt.bar(15,Neg,3, label="Negative")
plt.bar(20,Neu,3, label="Neutral")
plt.legend()
plt.ylabel('Number of examples')
plt.title('Proportion of examples')
plt.show()


# label selection
y=dataset.iloc[:,1].values
labelEnocder_y=LabelEncoder()
y=labelEnocder_y.fit_transform(y)
# 3 postive 1 negative 2 nuetral

print(y)
print(y.shape)

corpus=[]
stopwords=['ai', 'ayi', 'hy', 'hai', 'main', 'ki', 'tha', 'koi', 'ko', 'sy', 'woh', 'bhi', 'aur', 'wo', 'yeh', 'rha', 'hota', 'ho', 'ga', 'ka', 'le', 'lye', 'kr', 'kar', 'lye', 'liye', 'hotay', 'waisay', 'gya', 'gaya', 'kch', 'ab', 'thy', 'thay', 'houn', 'hain', 'han', 'to', 'is', 'hi', 'jo', 'kya', 'thi', 'se', 'pe', 'phr', 'wala', 'waisay', 'us', 'na', 'ny', 'hun', 'rha', 'raha', 'ja', 'rahay', 'abi', 'uski', 'ne', 'haan', 'acha', 'nai', 'sent', 'photo', 'you', 'kafi', 'gai', 'rhy', 'kuch', 'jata', 'aye', 'ya', 'dono', 'hoa', 'aese', 'de', 'wohi', 'jati', 'jb', 'krta', 'lg', 'rahi', 'hui', 'karna', 'krna', 'gi', 'hova', 'yehi', 'jana', 'jye', 'chal', 'mil', 'tu', 'hum', 'par', 'hay', 'kis', 'sb', 'gy', 'dain', 'krny', 'tou']
for i in range(0,len(y)):
    review = re.sub('[^a-zA-Z]',' ',str(dataset.iloc[:,0].values[i]))
    review=review.lower()
    review=review.split()
    review=[word for word in review if not word in stopwords]
    review=' '.join(review)
    corpus.append(review)
stopwords, len(stopwords)

corpus

cv=CountVectorizer(max_features=2500)
x=cv.fit_transform(corpus).toarray()
x=x[:14646]

print(x.shape)
print(x)

print(y.shape)
print(y)

#split the data
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20)

#classifier  for comparing the other classifier for accuracy
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

# import support vector classifier 
from sklearn.svm import SVC # Support Vector Classifier
classifier1 = SVC(kernel='linear',random_state=0) 
  
# fitting x samples and y classes 
classifier1.fit(x_train, y_train) 

y_pred1=classifier1.predict(x_test)
print(y_pred1)

#confusion matrix
cm1=confusion_matrix(y_test,y_pred1)
print(cm1)

#accuracy of SVM
print('Accuracy is {} '.format(accuracy_score(y_test, y_pred1)))

#visualizing the confusion matrix for classifer1
labels=['Positive','Neutral','Negative']
fig = plt.figure()
ax1 = fig.add_subplot(222)
cax = ax.matshow(cm1)
plt.title('Confusion matrix of the classifier1 \n')
fig.colorbar(cax)
ax.set_xticklabels([''] + labels)
ax.set_yticklabels([''] + labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()
