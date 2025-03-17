from tkinter import *
from tkinter import messagebox

def addtask():
    task= entry1.get()
    if task:
        tasklist.insert(END,task)
        entry1.delete(0,END)
    else :
        messagebox.showwarning("Warning","Task cannot be empty")
def remove1():
    try:
        selcted=tasklist.cursorselection()[0]
        tasklist.delete(0,END)
    except IndexError:
        messagebox.showwarning("Warning","No task selected")
def ca():
    tasklist.delete(0,END)
root=Tk()
root.title("To-Do-List")
root.geometry("300x400")
entry1=Entry(root,width=50)
entry1.pack(pady=10)
a=Button(root,text="Add Task" ,command=addtask)
a.pack()
b=Button(root,text="Remove Task" ,command=remove1)
b.pack()
c=Button(root,text="Clear All" ,command=ca)
c.pack()
tasklist=Listbox(root,width=40,height=15)
tasklist.pack(pady=15)
root.mainloop()



        
    