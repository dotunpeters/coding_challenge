
from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text = "Click Me")
button.pack()
button['text'] = "Press Me"
print(button['text'])
root.mainloop()
print(button.config())
print(str(button))