from tkinter import *
import sys
import os

about_us_window = Tk()
about_us_window.title("About Us")
about_us_window.wm_attributes("-fullscreen", "true")
about_us_window.config(bg="cyan")
about_us_window.iconbitmap("img/lpu_logo.ico")

image1 = PhotoImage(file="img/subhadip.gif")
image2 = PhotoImage(file="img/smaranika.gif")
image3 = PhotoImage(file="img/abuzar.gif")
image4 = PhotoImage(file="img/amrita.gif")

Label(about_us_window, text="Sentiment Analysis on Roman Urdu Dataset", font="bingo 30 underline", bg="cyan").pack(pady = 5)

about_us_window2 = Frame(about_us_window, bg="cyan")
about_us_window2.pack(anchor = NW)

Label(about_us_window2, text="About Developers", font="halston 20 italic underline", bg="cyan").pack(padx=50, pady=5)

about_us_window3 = Frame(about_us_window, bg="cyan")
about_us_window3.pack(side = LEFT)

Label(about_us_window3, image=image1).pack(padx=30, pady=5)
Label(about_us_window3, image=image2).pack(padx=30, pady=5)
Label(about_us_window3, image=image3).pack(padx=30, pady=5)
Label(about_us_window3, image=image4).pack(padx=30, pady=5)

about_us_window4 = Frame(about_us_window, bg="cyan")
about_us_window4.pack(side = LEFT)

Label(about_us_window4, text="Name: Subhadip Mondal", font="halston 15 italic", bg="cyan").pack(anchor=NW)
Label(about_us_window4, text="Reg. No. 11701711", font="halston 15 italic", bg="cyan").pack(anchor=NW)
Label(about_us_window4, text="Roll No. A13", font="halston 15 italic", bg="cyan").pack(anchor=NW)

Label(about_us_window4, bg="cyan").pack(anchor=NW, pady=30)

Label(about_us_window4, text="Name: Smaranika Datta", font="halston 15 italic", bg="cyan", fg="blue").pack(anchor=NW)
Label(about_us_window4, text="Reg. No. 11701716", font="halston 15 italic", bg="cyan", fg="blue").pack(anchor=NW)
Label(about_us_window4, text="Roll No. A14", font="halston 15 italic", bg="cyan", fg="blue").pack(anchor=NW)

Label(about_us_window4, bg="cyan").pack(anchor=NW, pady=30)

Label(about_us_window4, text="Name: Mohammad Abuzar", font="halston 15 italic", bg="cyan").pack(anchor=NW)
Label(about_us_window4, text="Reg. No. 11702551", font="halston 15 italic", bg="cyan").pack(anchor=NW)
Label(about_us_window4, text="Roll No. A15", font="halston 15 italic", bg="cyan").pack(anchor=NW)

Label(about_us_window4, bg="cyan").pack(anchor=NW, pady=30)

Label(about_us_window4, text="Name: Amrita Chaudri", font="halston 15 italic", bg="cyan", fg="blue").pack(anchor=NW)
Label(about_us_window4, text="Reg. No. 11703127", font="halston 15 italic", bg="cyan", fg="blue").pack(anchor=NW)
Label(about_us_window4, text="Roll No. A16", font="halston 15 italic", bg="cyan", fg="blue").pack(anchor=NW)

Label(about_us_window, text="Current Version : " + str(sys.version), font="halston 15 italic", bg="cyan", fg="orange").pack(padx=10, pady=5)

image5 = PhotoImage(file="img/sentiment_analysis.gif")
Label(about_us_window, image=image5).pack(padx=10, pady=10)
Label(about_us_window, text="Module Used", font="halston 20 italic underline", bg="cyan").pack(padx = 20, pady = 10)

about_us_window5 = Frame(about_us_window, bg="cyan")
about_us_window5.pack(anchor = N)

image6 = PhotoImage(file="img/sklearn.gif")
image7 = PhotoImage(file="img/nltk.gif")
image8 = PhotoImage(file="img/python.gif")
image9 = PhotoImage(file="img/tkinter.gif")
image10 = PhotoImage(file="img/numpy.gif")
image11 = PhotoImage(file="img/pandas.gif")
image12 = PhotoImage(file="img/matplotlib.gif")
image13 = PhotoImage(file="img/spyder.gif")

Label(about_us_window5, image=image6).grid(row = 0, column = 0)
Label(about_us_window5, image=image7).grid(row = 0, column = 1)
Label(about_us_window5, image=image8).grid(row = 0, column = 2)
Label(about_us_window5, image=image9).grid(row = 0, column = 3)
Label(about_us_window5, image=image10).grid(row = 1, column = 0, padx=10, pady=5)
Label(about_us_window5, image=image11).grid(row = 1, column = 1, padx=10, pady=5)
Label(about_us_window5, image=image12).grid(row = 1, column = 2, padx=10, pady=5)
Label(about_us_window5, image=image13).grid(row = 1, column = 3, padx=10, pady=5)

def home_page():
    about_us_window.destroy()
    os.system("python home.py")
home_button = PhotoImage(file="img/home_button.gif")
Button(about_us_window5, image=home_button, cursor="hand2", command=home_page).grid(row = 2, column = 0, columnspan = 3, pady=10)

def exit_window():
	about_us_window.destroy()
exit_image = PhotoImage(file = 'img/exit_image.gif')
Button(about_us_window5, image=exit_image, cursor="hand2", command = exit_window).grid(row = 2, column = 3, pady=10)

about_us_window.mainloop()
