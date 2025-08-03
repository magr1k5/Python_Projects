from tkinter import *
root = Tk()
root.title("Регистратор символов клавиатур")
text=Text(root,height=5 , width=20 , highlightthickness=2)
text.pack(expand=1 , fill="both")
def reportEvent(event):
    print('keysym=%s , keysym_num=%s'%(event.keysym, event.keysym_num))
text.bind("<KeyPress>" , reportEvent)
text.focus_set()
root.mainloop()    
