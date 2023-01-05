from tkinter import *

root = Tk()
root.title("Dongpakka coding")
root.geometry("640x480")

chkvar = IntVar() # chkvar에 int형으로 값을 저장
chkbox = Checkbutton(root, text="책 1권 일기", variable=chkvar)
# chkbox.select()     # default로 초기 체크되게
# chkbox.deselect()     # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="술 먹지 않기", variable=chkvar2)
chkbox2.pack()


def btncmd():
  print(chkvar.get())
  print(chkvar2.get())
  

btn = Button(root, text='클릭', command=btncmd)
btn.pack()



root. mainloop()