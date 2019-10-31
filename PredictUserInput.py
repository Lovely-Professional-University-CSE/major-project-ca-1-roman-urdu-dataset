from tkinter import *
import sys
	
user_input_window = Tk()
#from MyModel import clean, View_ConfusionMatrix, Visualize_ActualDataSet
import pickle
import MyModel


clf_classifier = pickle.load(open( "classifier.sav", "rb" ))

user_input_window.title("Predict User Input Comment")
#user_input_window.wm_attributes("-fullscreen", "true")
user_input_window.config(bg="cyan")
user_input_window.iconbitmap("img/lpu_logo.ico")

PositiveImage = PhotoImage(file = 'img/positive.gif')
NegativeImage = PhotoImage(file = 'img/negative.gif')
NeutralImage = PhotoImage(file = 'img/neutral.gif')
