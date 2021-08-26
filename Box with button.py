from tkinter import *

root = Tk()

#function
def myclick():
    mylabel = Label(root, text= 'poop', bg='#5982b5', fg='white')
    mylabel.pack()

#The actualy button
mybutton = Button(root, text = 'Poop?', padx= 100, pady= 10, command=myclick)
mybutton.pack()

# box color name and size
root.title("Poop?")
root.configure(bg='#5982b5')

root.mainloop()
