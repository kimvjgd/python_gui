from tkinter import *
root = Tk()
root.title("Dongpakka Coding")

btn1 = Button(root, text="버튼 1")
btn1.pack()     # 팩으로 우리 프로그램에 넣어줘야한다.

btn2 = Button(root, padx=5, pady=30, text="버튼 22222222222222222")
btn2.pack()

btn3 = Button(root, padx=30, pady=5, text="버튼 3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼 444444444444444444444")
btn4.pack()

btn5 = Button(root, fg="red", bg="blue", text='버튼 5')
btn5.pack()

photo = PhotoImage(file="tutorial/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
  print("버튼이 클릭되었습니다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.geometry("600x300")
root.mainloop()

