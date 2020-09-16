from tkinter import *

root=Tk()
root.title('Welcome to LikeGeeks app')
root.geometry('350x200')
'''
def callback():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

b=tkinter.Button(text="Hello",command=callback)
b.pack()

'''
#adding menu in menu bar
menu=Menu(root)
item=Menu(menu)
item.add_command(label='New') 
menu.add_cascade(label='File', menu=item) 
root.config(menu=menu) 


#adding a label
a=Label(root,text="First name")
a1=Label(root,text="last name")
a.grid(row=0)
a1.grid(row=1)

#for userinput
text=Entry(root,width=10)
text.grid(column=1,row=0)
text=Entry(root,width=10)
text.grid(column=1,row=1)


#adding a button
'''def clicked():
    store="you wrote:"+text.get()
    a.configure(text=store)

btn=Button(root,text="hii button",fg="red",bg="black",command=clicked)

btn.grid()'''

btn1=Button(root,text="Stop",width=25,command=root.destroy)
btn1.grid()



#implementing canvas
can=Canvas(root,bg="blue",width=40,height=60)
can.grid()
canvas_height=20
canvas_width=200
y = int(canvas_height / 2) 
can.create_line(0, y, canvas_width, y ) 

#check buttons



root.mainloop()
