from tkinter import *


root = Tk()
root.title("Dong coding")
root.geometry("640x480")

listbox = Listbox(root, selectmode='extended',height=3)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()


def btncmd():
  print(listbox)

btn = Button(root, text="클릭",  command=btncmd)
btn.pack()


root.mainloop()