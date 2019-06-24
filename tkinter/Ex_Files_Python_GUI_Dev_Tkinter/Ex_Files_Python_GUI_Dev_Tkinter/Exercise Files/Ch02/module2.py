
from tkinter import *
from tkinter import ttk

counter = 4
def helloWorld():
    counter = 4
    text = "Hello World" * counter
    print(text)
    counter += 1


root = Tk()
butt = ttk.Button()
butt.config(text = "Click Me")
butt.config(command = helloWorld)
butt.pack()
root.mainloop()
