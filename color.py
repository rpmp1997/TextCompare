from tkinter import *
import difflib
# def onclick():
#    pass
# root = Tk()
# text = Text(root)
# text.insert(INSERT, "Hello.....")
# text.insert(END, "Bye Bye.....")
# text.pack()
# text.tag_add("here", "1.0", "1.5")
# text.tag_add("start", "1.8", "1.13")
# text.tag_config("here", background="yellow", foreground="blue")
# text.tag_config("start", background="black", foreground="green")
# root.mainloop()


def show_diff(text, n_text):
   seqm = difflib.SequenceMatcher(None, text, n_text)
   output = []
   tempString = []
   for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
      if opcode == 'equal':
         output.append(seqm.a[a0:a1])
      elif opcode == 'insert':
         output.append("<font color=red>^" + seqm.b[b0:b1] + "</font>")
         tempString.append(seqm.b[b0:b1])
      elif opcode == 'delete':
         output.append("<font color=blue>^" + seqm.a[a0:a1] + "</font>")
         tempString.append(seqm.a[a0:a1])
      elif opcode == 'replace':
         output.append("<font color=green>^" + seqm.b[b0:b1] + "</font>")
         tempString.append(seqm.b[b0:b1])
      else:
         continue
   return tempString

def show_diff2(text, n_text):
   seqm = difflib.SequenceMatcher(None, text, n_text)
   output = []
   for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
      if opcode == 'equal':
         output = []
         output.append(seqm.a[a0:a1])
      elif opcode == 'insert':
         output = []
         output.append(seqm.b[b0:b1])
      elif opcode == 'delete':
         output = []
         output.append(seqm.a[a0:a1])
      elif opcode == 'replace':
         output = []
         output.append(seqm.b[b0:b1])
      else:
         continue
   return ''.join(output)

string1 = "aaa er lo1"
string2 = "aa4 er l51"
string3 = "aa er lo1"

print(show_diff(string1, string2))
