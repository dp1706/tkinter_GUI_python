from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')

menu=Menu(root)
item=Menu(menu)
item.add_command(label='New') 
item.add_command(label="Open")
item.add_command(label="Save")
item.add_command(label="Save as...")
item.add_command(label="Close")
item.add_separator()
item.add_command(label="Exit", command=root.quit)

menu.add_cascade(label='File', menu=item) 
root.config(menu=menu) 

root.mainloop()
