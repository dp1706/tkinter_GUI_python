from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

CheckVar1 = IntVar()
CheckVar2 = IntVar()

C1 = Checkbutton(root, text = "Music", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C2 = Checkbutton(root, text = "Video", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=5, \
                 width = 20)
C1.pack()
C2.pack()

root.mainloop()
