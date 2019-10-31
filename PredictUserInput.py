from tkinter import *
import sys
	
user_input_window = Tk()
#from MyModel import clean, View_ConfusionMatrix, Visualize_ActualDataSet
import pickle

clf_classifier = pickle.load(open( "classifier.sav", "rb" ))

user_input_window.title("Predict User Input Comment")
#user_input_window.wm_attributes("-fullscreen", "true")
user_input_window.config(bg="cyan")
user_input_window.iconbitmap("img/lpu_logo.ico")

PositiveImage = PhotoImage(file = 'img/positive.gif')
NegativeImage = PhotoImage(file = 'img/negative.gif')
NeutralImage = PhotoImage(file = 'img/neutral.gif')


def Predict_User_Input():
	user_input = Input_String.get()
	user_input = clean(user_input)
	user_input = [user_input]
	user_input_vector = current_vector.transform(user_input)
	Sentiment_user_input = clf_classifier.predict(user_input_vector)
	#Label(user_input_window, text = Sentiment_user_input).grid(row = 2, columnspan = 2)
	if Sentiment_user_input == 'Positive':
		Label(user_input_window, image=PositiveImage).grid(row = 2)
	elif Sentiment_user_input == 'Negative':
		Label(user_input_window, image=NegativeImage).grid(row = 2)
	else:
		Label(user_input_window, image=NeutralImage).grid(row = 2)
Label(user_input_window, text = 'Enter your comment').grid(row = 0, column = 0)
Input_String = StringVar()
Entry(user_input_window, textvariable = Input_String, bd = 5).grid(row = 0, column = 1)
Button(user_input_window, text = 'Predict Sentiment', command = Predict_User_Input).grid(row = 1, columnspan = 2)
user_input_window.mainloop()
