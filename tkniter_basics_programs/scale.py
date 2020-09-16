from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

scale=Scale(root,from_=0,to=44)
scale.pack()
scale1=Scale(root,from_=0,to=44,orient=HORIZONTAL)
scale1.pack()

root.mainloop()
