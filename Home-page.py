from tkinter import *
import os
import sys
from PIL import ImageTk, Image
about_us= Tk()
about_us.title("ROMAN URDU DATASET")
about_us.wm_attributes("-fullscreen", "true")
about_us.config(bg="White")


win1 = Frame(about_us, bg="white")
about_us.pack(side=LEFT)

win2= Frame(about_us, bg="white")
about_us.pack(side=LEFT, pady=50)

win3= Frame(about_us, bg="white")
about_us.pack(side=LEFT, pady=50)

img1 = PhotoImage(file="Subhadip.gif")
img2 = PhotoImage(file="smaranika.gif")
img3 = PhotoImage(file="abuzar.gif")
img4 = PhotoImage(file="amrita.gif")

Label(win1, image=img1).pack(padx=50, pady=10)
Label(win1, image=img2).pack(padx=50, pady=10)
Label(win1, image=img3).pack(padx=50, pady=10)
Label(win1, image=img4).pack(padx=50, pady=10)

Label(win3, text="ABOUT US", font="Times", bg="white", fg="black").pack(anchor=NW)


Label(win2, text="Name: Subhadip Mondal", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Reg. No: 11701711", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Roll No: A13", font="Times", bg="white", fg="blue").pack(anchor=NW)

Label(win2, bg="white").pack(anchor=NW, pady=40)

Label(win2, text="Name: Smaranika Datta", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Reg. No: 11701716", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Roll No: A14", font="Times", bg="white", fg="blue").pack(anchor=NW)

Label(win2, bg="white").pack(anchor=NW, pady=40)

Label(win2, text="Name: Mohammad Abuzar", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Reg. No: 11702551", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Roll No: A15, font="Times", bg="white", fg="blue").pack(anchor=NW)

Label(win2, bg="white").pack(anchor=NW, pady=40)

Label(win2, text="Name: Amrita Chaudri", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Reg. No: 11703127", font="Times", bg="white", fg="blue").pack(anchor=NW)
Label(win2, text="Roll No: A16", font="Times", bg="white", fg="blue").pack(anchor=NW)

Label(win2, bg="white").pack(anchor=NW, pady=40)

technology = PhotoImage(file="animation.gif")
start = PhotoImage(file="start_button.gif")

Label(win3, text="Technology we used", font="Times", bg="white", fg="blue").pack(anchor=NW, padx=90, pady=20)
Label(win3, image=technology).pack(anchor=NW, padx=90, pady=20)
Label(win3, text="Click the START button", font="Times", bg="white", fg="black").pack(anchor=NW)
Button(win3, image=start).pack(anchor=NW, padx=300, pady=50)

about_us.mainloop()

