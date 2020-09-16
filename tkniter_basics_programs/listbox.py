from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

ls=Listbox(root,selectmode=SINGLE)

ls.insert(1, 'Python') 
ls.insert(2, 'Java') 
ls.insert(3, 'C++') 
ls.insert(4, 'Any other') 
ls.pack() 

root.mainloop()
