from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')
var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value=2)
R2.pack(anchor = W)

root.mainloop()
