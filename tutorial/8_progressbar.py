import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Dongpakka coding")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)   # 10ms마다 움직임
# progressbar.pack()

# def btncmd():
#   progressbar.stop()

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd():
  for i in range(1, 101): # 1~100
    time.sleep(0.01)  # 0.01초 대기
    p_var2.set(i)
    progressbar2.update()
    print(p_var2.get())

btn2 = Button(root, text='시작', command=btncmd)
btn2.pack()
root.mainloop()
