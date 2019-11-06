from tkinter import *
import os
home_window = Tk()
home_window.title("Home")
home_window.wm_attributes("-fullscreen", "true")
home_window.config(bg="cyan")
home_window.iconbitmap("img/lpu_logo.ico")

sentiment1 = PhotoImage(file = 'img/sentiment_home.gif')
about_us_dev = PhotoImage(file = 'img/about_developers.gif')
take_UI = PhotoImage(file = 'img/user_input.gif')

Label(home_window, image = sentiment1).grid(row = 0, column = 0, columnspan = 2, padx = 100, pady = 20)

def exit_window():
	home_window.destroy()
exit_image = PhotoImage(file = 'img/exit_image.gif')
Button(home_window, image=exit_image, cursor="hand2", command = exit_window).grid(row = 0, column = 2)


def About_Dev():
	home_window.destroy()
	os.system('python about_us.py')
Button(home_window, image = about_us_dev, font="halston 20 italic", cursor="hand2", command = About_Dev).grid(row = 1, column = 0)

def Predict_Input():
	home_window.destroy()
	os.system('python PredictUserInput.py')
Button(home_window,  image = take_UI, font="halston 20 italic", cursor="hand2", command = Predict_Input).grid(row = 1, column = 1)

home_window.mainloop()
