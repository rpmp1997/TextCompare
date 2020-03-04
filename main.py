from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as ScrolledText
import re
import difflib

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

    if rightText != '' and leftText != '':
        leftTextList = leftText.split("\n")
        rightTextList = rightText.split("\n")

        leftSet = set(leftTextList)
        rightSet = set(rightTextList)

        leftAdded = leftSet - rightSet
        leftRemoved = rightSet - leftSet

        countLeftNew = 0
        countLeftOld = 0
        countRightNew = 0
        countRightOld = 0

        for line in leftTextList:
            if line in leftAdded:
                print("-" +line.strip())
            elif line in leftRemoved:
                print("+" +line.strip())

        for line in rightTextList:
            countRightNew += 1
            countRightOld += 1
            if line in leftAdded:
                print("-" + line.strip())
                containerRight.tag_add("rightColor", '3.0', '3.99')
                containerRight.tag_config("rightColor", background='red')

            elif line in leftRemoved:
                print("+" +line.strip())
                containerRight.tag_add("rightColor", str(countRightNew)+'.0', str(countRightNew)+'.999')
                containerRight.tag_config("rightColor", background='red')
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


#Settings gor frames and containers
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

