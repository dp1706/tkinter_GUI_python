from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

sb=Scrollbar(root)
sb.pack(side=RIGHT,fill=Y)

mylist =Listbox(root,yscrollcommand = sb.set)
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
sb.config( command = mylist.yview )

root.mainloop()
