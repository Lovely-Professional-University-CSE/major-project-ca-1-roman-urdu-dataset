from tkinter import *
import os
	
user_input_window = Tk()
user_input_window.title("Predict User Input Comment")
user_input_window.wm_attributes("-fullscreen", "true")
user_input_window.config(bg="cyan")
user_input_window.iconbitmap("img/lpu_logo.ico")

#from MyModel import clean, View_ConfusionMatrix, Visualize_ActualDataSet
import pickle
current_vector = pickle.load(open("vectorizer.sav", "rb" ))
clf_classifier = pickle.load(open( "classifier.sav", "rb" ))

def See_Main_Data():
	user_input_window.destroy()
	
	image_window = Tk()
	image_window.title("Actual Dataset")
	image_window.config(bg="cyan")
	image_window.iconbitmap("img/lpu_logo.ico")
	actual_dataset = PhotoImage(file = 'img/actual_data.gif')
	Label(image_window, image = actual_dataset).grid(row = 0, column = 0)
	image_window.mainloop()
	
	os.system('python PredictUserInput.py')

def Visualize_C_Matrix():
	user_input_window.destroy()
	
	image_window = Tk()
	image_window.title("Confusion Matrix")
	image_window.config(bg="cyan")
	image_window.iconbitmap("img/lpu_logo.ico")
	confusion_matrix = PhotoImage(file = 'img/confusion_matrix.gif')
	Label(image_window, image = confusion_matrix).grid(row = 0, column = 0)
	image_window.mainloop()
	
	os.system('python PredictUserInput.py')

def View_Model_Accuracy():
	file = open('AccuracyPercentage', 'rb')
	Accuracy = pickle.load(file)
	file.close()
	from tkinter import messagebox
	messagebox.showinfo('Model Accuracy', 'Accuracy is ' + Accuracy)

def Home_Page():
    user_input_window.destroy()
    os.system("python home.py")

def About_Developer():
	user_input_window.destroy()
	os.system("python about_us.py")

def Take_Help():
	from tkinter import messagebox
	messagebox.showinfo('Help', 'Write your own comment or review on the box.\nNote, Comment sholud be wrote in Hindi language.\nE.g. "kharab hai".\nThen click the "Predict Sentiment" Button to see whether the sentiment is "POSITIVE or NEUTRAL or NEGATIVE".')

def exit_window():
	user_input_window.destroy()

PositiveImage = PhotoImage(file = 'img/positive.gif')
NegativeImage = PhotoImage(file = 'img/negative.gif')
NeutralImage = PhotoImage(file = 'img/neutral.gif')

def Predict_User_Input():
	
	import re
	from nltk import word_tokenize
	# created user defined stopwords
	stopwords=['ai', 'ayi', 'hy', 'hai', 'main', 'ki', 'tha', 'koi', 'ko', 'sy', 'woh', 'bhi', 'aur', 'wo', 'yeh', 'rha', 'hota', 'ho', 'ga', 'ka', 'le', 'lye', 'kr', 'kar', 'lye', 'liye', 'hotay', 'waisay', 'gya', 'gaya', 'kch', 'ab', 'thy', 'thay', 'houn', 'hain', 'han', 'to', 'is', 'hi', 'jo', 'kya', 'thi', 'se', 'pe', 'phr', 'wala', 'waisay', 'us', 'na', 'ny', 'hun', 'rha', 'raha', 'ja', 'rahay', 'abi', 'uski', 'ne', 'haan', 'acha', 'nai', 'sent', 'photo', 'you', 'kafi', 'gai', 'rhy', 'kuch', 'jata', 'aye', 'ya', 'dono', 'hoa', 'aese', 'de', 'wohi', 'jati', 'jb', 'krta', 'lg', 'rahi', 'hui', 'karna', 'krna', 'gi', 'hova', 'yehi', 'jana', 'jye', 'chal', 'mil', 'tu', 'hum', 'par', 'hay', 'kis', 'sb', 'gy', 'dain', 'krny', 'tou']

	def cleaning(user_input):
		review_with_no_special_character = re.sub('[^a-zA-Z]',' ',str(user_input))
		review_in_lowercase = review_with_no_special_character.lower()
		review_in_tokens = word_tokenize(review_in_lowercase)
		review_with_no_stopwords = [word for word in review_in_tokens if not word in stopwords]
		return ' '.join(review_with_no_stopwords)
		
	user_input = Input_String.get()	
	user_input = cleaning(user_input)
	user_input = [user_input]
	
	user_input_vector = current_vector.transform(user_input)
	Sentiment_user_input = clf_classifier.predict(user_input_vector)
	
	if Sentiment_user_input == 'Positive':
		Label(user_input_window, image=PositiveImage).grid(row = 3, column = 1)
	elif Sentiment_user_input == 'Negative':
		Label(user_input_window, image=NegativeImage).grid(row = 3, column = 1)
	else:
		Label(user_input_window, image=NeutralImage).grid(row = 3, column = 1)

data_image = PhotoImage(file = 'img/f_data_image.gif')
Button(user_input_window, image = data_image, cursor="hand2", command = See_Main_Data).grid(row = 0, column = 0, padx =5, pady = 5)
confusion_image = PhotoImage(file = 'img/f_confusion_image.gif')
Button(user_input_window, image = confusion_image, cursor="hand2", command = Visualize_C_Matrix).grid(row = 1, column = 0, padx =5, pady = 5)
accuracy_image = PhotoImage(file = 'img/f_accuracy_image.gif')
Button(user_input_window, image = accuracy_image, cursor="hand2", command = View_Model_Accuracy).grid(row = 2, column = 0, padx =5, pady = 5)

Label(user_input_window, text = 'Enter Comment / Review in Hindi', font="halston 20 italic", bg = 'cyan').grid(row = 0, column = 1)
Input_String = StringVar()
Entry(user_input_window, textvariable = Input_String, bd = 10, bg = 'bisque', fg = 'green', font="halston 20 italic",).grid(row = 1, column = 1)
predict_image = PhotoImage(file = 'img/f_predict_image.gif')
Button(user_input_window, image = predict_image, cursor="hand2", command = Predict_User_Input).grid(row = 2, column = 1)

home_image = PhotoImage(file = 'img/home_button.gif')
Button(user_input_window, image = home_image, cursor="hand2", command = Home_Page).grid(row = 0, column = 2, padx =5, pady = 5)
about_image = PhotoImage(file = 'img/f_about_image.gif')
Button(user_input_window, image = about_image, cursor="hand2", command = About_Developer).grid(row = 1, column = 2, padx =5, pady = 5)
help_image = PhotoImage(file = 'img/f_help_image.gif')
Button(user_input_window, image = help_image, cursor="hand2", command = Take_Help).grid(row = 2, column = 2, padx =5, pady = 5)
exit_image = PhotoImage(file = 'img/f_exit_image.gif')
Button(user_input_window, image = exit_image, cursor="hand2", command = exit_window).grid(row = 1, column = 3, padx =5, pady = 5)

user_input_window.mainloop()
