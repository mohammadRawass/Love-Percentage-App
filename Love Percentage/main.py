# def add(*args):
#     return sum(args)
#
# print(add(1,2,3,4,5))

# def add(**kwargs):
#     for n in kwargs.items():
#         print(n)
#     print(kwargs.get("n3"))
#
# add(n1 = 5, n2 = 10)

from tkinter import *
from random import Random
usage = 1

rand = Random()
window = Tk()
window.title("Love Percent")
window.minsize(800,600)
my_label = Label(text="Check how much you", font=("Arial",35,"normal"))
my_label["text"] = f"{my_label["text"]}\nLove your wife!"
my_label.pack()
my_label.config(pady=15)

input_name1 = Entry(width = 80)
input_name1.insert(END, string = "Type your name...")
input_name1.pack(pady=20)
input_name2 = Entry(width = 80)
input_name2.insert(END, string = "Type your wife's/girlfriend's name...")
input_name2.pack()

# def setUsage():
#     global usage
#     if usage >= 1:
#         new_label = Label(text=f"\n{input_name1.get()}'s loving percent for {input_name2.get()} is:\n{rand.randint(0,100)}%", font=("Arial",25,"normal"))
#         new_label.pack(pady=20, padx=100)
#         usage -= 1
#     elif usage < 1:
#         pass

def onClicked():
    #setUsage()
    new_label = Label(text=f"\n{input_name1.get()}'s loving percent for {input_name2.get()} is:\n{rand.randint(0, 100)}%", font=("Arial", 25, "normal"))
    new_label.pack(pady=20, padx=100)

button = Button(text = "Click to see how much you love your wife", width = 40, command = onClicked)
button.pack(pady=20)

window.mainloop()