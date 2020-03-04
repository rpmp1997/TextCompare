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

def show_diff(text, n_text):
   seqm = difflib.SequenceMatcher(None, text, n_text)
   output = []
   for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
      if opcode == 'equal':
         output.append(seqm.a[a0:a1])
      elif opcode == 'insert':
         output.append("<font color=red>^" + seqm.b[b0:b1] + "</font>")
      elif opcode == 'delete':
         output.append("<font color=blue>^" + seqm.a[a0:a1] + "</font>")
      elif opcode == 'replace':
         output.append("<font color=green>^" + seqm.b[b0:b1] + "</font>")
      else:
         continue
   return ''.join(output)

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
                for k in range(len(tempRight)):
                    if(tempLeft[k] != tempRight[k]):
                        containerRight.tag_add("rightColor", str(i+1)+"."+str(k))
                        containerRight.tag_config("rightColor", foreground='red')
                        containerLeft.tag_add("leftColor", str(i+1)+"."+str(k))
                        containerLeft.tag_config("leftColor", foreground='green')

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

