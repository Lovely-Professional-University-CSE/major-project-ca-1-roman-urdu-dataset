# Importing the libraries
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



dataset = pd.read_csv('F:\Sentiment Analysis on Roman Urdu Dataset\Roman Urdu DataSet.csv', names=['Comment', 'sentiment', 'nan'])

print(dataset.head())
print(dataset.shape)

