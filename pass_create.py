import tkinter as tk
import random
import string

root = tk.Tk()
root.geometry('400x280')
root.title('Password Generator')

title = tk.StringVar()
label = tk.Label(root, textvariable=title)
label.pack()
title.set('The strength of the password')

def selection():
    pass

choice = tk.IntVar()
R1 = tk.Radiobutton(root, text='Poor', variable=choice, value=1, command=selection)
R1.pack(anchor='center')
R2 = tk.Radiobutton(root, text='Average', variable=choice, value=2, command=selection)
R2.pack(anchor='center')
R3 = tk.Radiobutton(root, text='Advanced', variable=choice, value=3, command=selection)
R3.pack(anchor='center')

lenlabel = tk.StringVar()
lenlabel.set('Password length')
lentitle = tk.Label(root, textvariable=lenlabel)
lentitle.pack()

val = tk.IntVar()
spinlength = tk.Spinbox(root, from_=8, to_=24, textvariable=val, width=13)
spinlength.pack()

def passgen():
    poor = string.ascii_uppercase + string.ascii_lowercase + string.digits
    symbols = string.punctuation
    advance = poor + symbols

    if choice.get() == 1:
        return "".join(random.sample(poor, val.get()))
    elif choice.get() == 2:
        return "".join(random.sample(poor + string.ascii_lowercase, val.get()))
    elif choice.get() == 3:
        return "".join(random.sample(advance, val.get()))
    else:
        return "Select a strength"

def callback():
    password = passgen()
    sum.config(text=password)

passgenButton = tk.Button(root, text='Generate Password', bd=5, height=2, command=callback, pady=3)
passgenButton.pack()

sum = tk.Label(root, text="")
sum.pack(side='bottom')

root.mainloop()
