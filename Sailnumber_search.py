#Importing
from tkinter import *
import pandas as pd

#setting up tkinter window
root = Tk()
root.title("Yacht Search")
root.configure(bg = "Light Grey")
root.minsize(1550, 800)


#assigning keyword to search bar input
name = StringVar()


#making function to run search
def get_name(*args):
    def clearinfo():#making function for button to clear info from screen
        matchfound.destroy()#destoying info
    df = pd.read_csv('myfile.csv')#assigning .csv file to variable
    result = df[df["Sail no."].isin([name.get()])]#searching for keyword in .csv file
    result = str(result)#converting result to string
    print(result)#printing to terminal(not needed but useful during coding stages)
    matchfound = Label(text = result, pady = 20, bg = "Light Grey", fg = "Grey", font=("Arial", 12))
    matchfound.place(rely = 0.5, relx = 0.5, anchor = CENTER)#adding search results as text label to tkinter window
    clear = Button(text = "Clear", bg = "Grey55", pady=5, padx=35, fg = "Blue3", command = clearinfo, font=(20))
    clear.place(anchor = CENTER, relx = 0.1, rely = 0.5)#adding clear button over enter button

#adding text label to tkinter window
name_selected = Label(text = "Please enter the sail number of the vessel", pady = 10, bg = "Light Grey", fg = "Blue2", font=("Arial", 20, "bold"))
name_selected.place(x=540, y=50)

#adding search bar to tkinter window
searchbar = Entry(textvariable = name, bg = "grey95", fg = "grey2", width = 40, font = ("Arial", 13))
searchbar.place(x=550, y=100)

#adding search button to tkinter window
Searchbutton = Button(text = "Enter", bg = "Grey55", pady=1, padx=25, fg = "Blue3", command=get_name)
Searchbutton.place(x=915, y=99)


root.mainloop()