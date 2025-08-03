from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("ТЕСТ")
label1=Label(text="Подтвердите или опровергните утверждение:",font=("Helvetica",14))
label1.grid(row=1,column=0 , sticky=W)
l2=Label(text='Язык Python является объектно-ориентированным?')
l2.grid(row=2,column=0,sticky=W)
l3=Label(root,text='(поставьте галочку, если утверждение верно)')
l3.grid(row=4,column=0,sticky=W)
var=IntVar()
ch_box = Checkbutton(root,text='Да/Нет',variable=var,onvalue=1,offvalue=0)
ch_box.grid(row=3,column=0,sticky=W)
def check():
    if var.get() == 1:
        master=Tk()
        message=Message(master,text="ПОЗДРАВЛЯЮ! Вы ответили правильно!",width=300)
        message.pack()
        master.mainloop()
    elif var.get()== 0:
        master=Tk()
        message=Message(master,text="К сожалению, вы ответили неправильно",width=300)
        message.pack()
        master.mainloop()
button=Button(root,text='Проверить',command=check)
button.grid(row=5,column=0,sticky=W)
root.mainloop()
check()



    
