from tkinter import *

#  settings
root = Tk()
# root.mainloop()
root.geometry("400x200")
root.title("calculator")
root.resizable(width=False, height=False)
color = "gray"
root.configure(bg=color)

#  frames
top_first = Frame(root, width=400, height=50, bg='red')
top_first.pack(side=TOP)

top_second = Frame(root, width=400, height=50, bg='green')
top_second.pack(side=TOP)

top_third = Frame(root, width=400, height=50, bg='blue')
top_third.pack(side=TOP)

top_forth = Frame(root, width=400, height=50, bg='yellow')
top_forth.pack(side=TOP)

root.mainloop()
