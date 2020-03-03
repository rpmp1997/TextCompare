from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as ScrolledText
import re

global leftText, rightText

class mainRoot(Tk):
      def __init__(self):
          super(mainRoot, self).__init__()
          self.title("Text Compare")
          self.geometry("1280x600")
          self.configure(background="#4D4D4D")


################ METHODS ################

def alertBox():
    messagebox.showinfo("Title", str(type(containerRight.get(1.0, END))))

def compareData():
    leftText = containerLeft.get(1.0, END)
    rightText = containerRight.get(1.0, END)

    if leftText != '' and rightText != '':
        leftSplitSentences = leftText.splitlines(keepends=True)
        rightSplitSentences = rightText.splitlines(keepends=True)
        minlen = len(leftSplitSentences) if len(rightSplitSentences) > len(leftSplitSentences) else len(rightSplitSentences)
        for i in range(minlen):
            tempLeft = leftSplitSentences[i]
            tempRight = rightSplitSentences[i]
            if tempLeft != tempRight:


        # containerRight.tag_add("rightColor", "1."+str(i))
        # containerRight.tag_config("rightColor", foreground='red')
        # messagebox.showinfo("Title", rightText)

    else:
        messagebox.showinfo('Title', "One of the fields is blank")

################ MAIN EXECUTION ################

#Initialize Window
main = mainRoot()


#Menu Creation
menu = Menu(main)
main.config(menu=menu)
fileMenu = Menu(menu)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Run", command=alertBox)
fileMenu.add_command(label="Compare", command=compareData)


#Settings for frames and containers
left = Frame(main, borderwidth=2, relief="solid", background="#4D4D4D")
right = Frame(main, borderwidth=2, relief="solid", background="#4D4D4D")
containerLeft = ScrolledText.ScrolledText(left, borderwidth=2, relief="solid", width=50)
containerRight = ScrolledText.ScrolledText(right, borderwidth=2, relief="solid", width=50)

#Setting labels
labelTextColumnLeft = Label(left, text="Text Column 1")
labelTextColumnRight = Label(right, text="Text Column 2")

#Configuring layout
left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")
labelTextColumnLeft.pack()
labelTextColumnRight.pack()
containerLeft.pack(expand=True, fill="both", padx= 5, pady= 5)
containerRight.pack(expand=True, fill="both", padx= 5, pady= 5)

#Executes window
main.mainloop()

