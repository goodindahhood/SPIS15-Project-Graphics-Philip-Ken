# -*- coding: utf-8 -*-
from Tkinter import *
from ttk import Frame, Style
from Seams import *
from PIL import Image, ImageTk

class Application(Frame):

    def __init__(self,master):
        """initializes the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """create button, text, and entry widget"""

        background = "WHITE"
        textColor = "BLACK"

        self.text = Label(self, text = "This program is still in Alpha", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row = 0, column = 0,sticky=(W+E),padx=0,pady=0)

        self.text = Label(self, text = "stages.  ", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=0,column=1,sticky=W+E,padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=1, column=0, sticky = W+E)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=1, column=1, sticky = W+E)
        
        self.instruction = Label(self, text = "Enter Pixels (width)", fg = textColor, background = background, highlightthickness = 0)
        self.instruction.grid(row=2,column=0,sticky=W+E,padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=2, column=1, sticky = W+E)

        self.input = Entry(self)
        self.input.grid(row=3,column=0,sticky=W+E,padx=0,pady=0)

        self.submit_button = Button(self,text="Carve",bg = 'red', command = self.reveal, fg = textColor, background = background)
        self.submit_button.grid(row=3,column=1,sticky=W,padx=0,pady=0)

        self.instruction = Label(self, text = "Enter Pixels (height)", fg = textColor, background = background, highlightthickness = 0)
        self.instruction.grid(row=4,column=0,columnspan=1,sticky=W+E,padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=4, column=1, sticky = W+E)

        self.input1 = Entry(self)
        self.input1.grid(row=5,column=0,sticky=W+E,padx=0,pady=0)

        self.submit_button = Button(self,text="Carve", bg='blue', command = self.reveal1, fg = textColor, background = background)
        self.submit_button.grid(row=5,column=1,sticky=W,padx=0,pady=0)

        self.text = Label(self, text = "(ﾉಥ益ಥ）ﾉ﻿ ┻━┻", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row = 6, column = 0,sticky=(W+E),padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=6, column=1, sticky = W+E)

        self.text = Label(self, text = "(ノಠ ∩ಠ)ノ彡( o°o)", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row = 7, column = 0,sticky=(W+E),padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=7, column=1, sticky = W+E)

        self.text = Label(self, text = "/( .□.) ︵╰(゜益゜)╯︵ /(.□. /)", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row = 8, column = 0,sticky=(W+E),padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=8, column=1, sticky = W+E)

        self.text = Label(self, text = "ಠ_ಠ I ಠ_ಠ I ಠ_ಠ", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row = 9, column = 0,sticky=(W+E),padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=9, column=1, sticky = W+E)

        self.text = Label(self, text = "(੭ ˘•ω•˘)੭ु⁾⁾", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row = 10, column = 0,sticky=(W+E),padx=0,pady=0)

        self.text = Label(self, text = "", fg = textColor, background = background, highlightthickness = 0)
        self.text.grid(row=10, column=1, sticky = W+E)

    def reveal(self):
        """Initiates seam carving"""
        content = self.input.get()
        seampractice(land, int(content))

    def reveal1(self):
        """Initiates seam carving"""
        content = self.input1.get()
        seampractice1(land, int(content))


def main():
    root = Tk()
    root.title("Seam Carving")
    root.geometry("450x450")

    image = Image.open('Saber.jpg')
    w1, h1 = image.size
    tkpi = ImageTk.PhotoImage(image)        
    label_image = Label(root, image=tkpi)
    label_image.place(x=1,y=1,width=w1,height=h1)

    app = Application(root)
    root.mainloop()

if __name__=='__main__':
    main()
        
