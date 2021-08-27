import os
import tkinter
from tkinter.constants import COMMAND

#opening file explorer and send succses message
def appimport():
    os.system("Explorer")
    mylabel = tkinter.Label(root, text= 'File Exlorer was successfully opened', bg='#5982b5', fg='white')
    mylabel.pack()

root = tkinter.Tk()

#The actualy button
mybutton = tkinter.Button(root, text = 'Would you like to open a Folder?', padx= 100, pady= 10, command=appimport) 
mybutton.pack()

# box color name and size
root.title("Open folder")
root.configure(bg='#5982b5')

root.mainloop()