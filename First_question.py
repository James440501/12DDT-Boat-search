#importing tkinter
from tkinter import *
import pandas as pd

#setting up tkinter window
root = Tk()
root.configure(background="Light Grey")

name = StringVar()
#making function to open different search pages
def run_name():
        root.destroy()
        with open('Name_search.py', 'r') as file:
            secondpage = file.read()
            exec(secondpage)#executing Name search file
def run_sailnum():
        root.destroy()
        with open('Sailnumber_search.py', 'r') as file:
            secondpage = file.read()
            exec(secondpage)#executing sailnumber search file
def run_design():
        root.destroy()
        with open('Design_search.py', 'r') as file:
            secondpage = file.read()
            exec(secondpage)#executing design search file
def run_designer():
        root.destroy()
        with open('Designer_search.py', 'r') as file:
            secondpage = file.read()
            exec(secondpage)#executing designer search file


#adding text label to tkinter window
Ques = Label(text = "What would you like to use for your search?", pady = 30, bg = "Light Grey", fg = "Blue2", font=("Arial", 20, "bold"))
Ques.pack()

#adding name search button
Name_but  = Button(text = "Name", pady = 10, padx = 60, bg = "grey89", fg = "Blue", font=("arial", 14, "italic"), command=run_name)
Name_but.pack()

#adding sail number search button
Sailnumber_but = Button(text = "Sail Number", pady = 10, padx = 60, bg = "grey89", fg = "Blue", font=("arial", 14, "italic"), command=run_sailnum)
Sailnumber_but.pack()

#adding design search button
Design_but = Button(text = "Design", pady = 10, padx = 60, bg = "grey89", fg = "Blue", font=("arial", 14, "italic"), command=run_design)
Design_but.pack()

#adding designer search button
Designer_but = Button(text = "Designer Name", pady = 10, padx = 60, bg = "grey89", fg = "Blue", font=("arial", 14, "italic"), command=run_designer)
Designer_but.pack()

root.mainloop()
