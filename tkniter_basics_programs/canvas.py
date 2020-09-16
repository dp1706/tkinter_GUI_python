from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

w=Canvas(root,bg="blue", height=300, width=400)
w.pack()
coord = 10, 50, 240, 210
arc = w.create_arc(coord, start=0, extent=150, fill="red")

filename = PhotoImage(file = "hs.jpg")
image = w.create_image(50, 50, anchor=NE, image=filename)

root.mainloop()
