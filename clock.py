from datetime import datetime
from tkinter import *

def update_time():
    dt = datetime.now()
    timeframe = dt.strftime('%H:%M:%S %p')
    my_label.config(text=timeframe)
    root.after(1000, update_time)

root = Tk()
root.title('Clock App')
root.configure(bg='black')

my_label = Label(root, fg='red', bg='black', font=('arial', 100, 'bold'))
my_label.pack()

update_time()

root.mainloop()
