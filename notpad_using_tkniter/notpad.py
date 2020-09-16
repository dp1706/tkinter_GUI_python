import tkinter
import os 
import sys
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
        if file =="":
            file = None

        else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()
def saveas():
    global file
    file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                     ("Text Documents", "*.txt")])
    if file =="":
            file = None

    else:
            #Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")

def quitApp():
     res = askquestion('Exit Application','Do you really want to exit')
     if res == 'yes' : 
        root.destroy() 
          
    # else : 
        #showinfo('Return', 'Returning to main application')
        

def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<>"))
def paste():
    TextArea.event_generate(("<>"))

def about():
    showinfo("Notepad", "Notepad by Code With Dwarka")


if __name__ == "__main__":
    root=Tk()
    #root.iconbitmap(r"/home/dwarka/Pictures/tkinter/notepad.png")
    root.title('untitled-Notpad')
    root.geometry("644x788")

    TextArea=Text(root)
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    menu=Menu(root)
    FileMenu=Menu(menu,tearoff=0)

    FileMenu.add_command(label="New", command=newFile)

    #To Open already existing file
    FileMenu.add_command(label="Open", command = openFile)

    # To save the current file

    FileMenu.add_command(label = "Save", command = saveFile)
    FileMenu.add_command(label = "Save as", command = saveas)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitApp)
    menu.add_cascade(label = "File", menu=FileMenu)


    EditMenu = Menu(menu, tearoff=0)
    
    
    EditMenu.add_command(label = "Cut", command=cut)
    EditMenu.add_command(label = "Copy", command=copy)
    EditMenu.add_command(label = "Paste", command=paste)

    menu.add_cascade(label="Edit", menu = EditMenu)

    HelpMenu = Menu(menu, tearoff=0)
    HelpMenu.add_command(label = "About Notepad", command=about)
    menu.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=menu)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

   

    root.mainloop()

