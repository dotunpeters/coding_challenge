#!/usr/bin/python3
# hello_local.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk

class HelloApp():

    def __init__(self, master):

        self.label = ttk.Label(master, text = "Hi, Tkinter!")
        self.label.grid(row = 0, column = 0, columnspan=2)
        
        ttk.Button(master, text = "Texas",
                   command = self.texas_hello).grid(row = 1, column = 0)

        ttk.Button(master, text = "Hawaii",
                   command = self.hawaii_hello).grid(row = 1, column =1)

        but = ttk.Button(master, text="Default")
        but.grid(row = 2, column = 0, columnspan=2)
        but.config(command = self.default_hello)
        but.state(["disabled"])
        but.instate(["disabled"])

    def texas_hello(self):
        #self.label.config(text = 'Howdy, Tkinter!')
        self.label['text'] = "Howdy, Tkinter!"
        print("Hello")

    def hawaii_hello(self):
        #self.label.config(text = 'Aloha, Tkinter!')
        self.label['text'] = "Aloha, Tkinter!"

    def default_hello(self):
        self.label["text"] = "Hi, Tkinter!"

            
def main():            
    
    root = Tk()
    app = HelloApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
