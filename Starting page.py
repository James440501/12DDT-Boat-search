#importing Tkinter
from tkinter import *
import pandas as pd

#setting up tkinter window
root = Tk()
root.title("Yacht Search")
root.configure(background="Light Grey")
root.minsize(1550, 800)

name = StringVar()
#making function to run second page upon button press
def run_file():
        with open('First_question.py', 'r') as file:
            secondpage = file.read()
            exec(secondpage)

#adding text label to tkinter window
Greeting = Label(text = "Welcome to the New Zealand yacht search tool!", bg = "Light Grey", fg = "Blue2", pady = 30, font=("Arial", 30, "bold", "italic"))
Greeting.pack()

#adding start button to tkinter window
Start_button = Button(text = "Begin Search", padx = 60, pady = 8, bg = "grey90", fg = "Blue2",  font=("Arial", 15), command=run_file)
Start_button.pack()


root.mainloop()