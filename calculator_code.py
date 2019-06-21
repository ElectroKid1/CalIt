#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''1] To give spaces between buttons
   2] To give the color to the frame
   3] To give the title to frame
   4] To convert this to the exe file'''

from tkinter import *
from tkinter import messagebox
root=Tk()
root.configure(bg="lightsteelblue")
root.title("MyCal v0.1.1")
#root.geometry("370x300")
#to define the function
def add():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:
        output=int(e1.get())+int(e2.get())
        w=Message(root,text=str(output),width=51).grid(row=4,column=0,columnspan=4)
def sub():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:
        output=int(e1.get())-int(e2.get())
        w=Message(root,text=str(output),width=51).grid(row=4,column=0,columnspan=4)
def mul():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:
        output=int(e1.get())*int(e2.get())
        w=Message(root,text=str(output),width=51).grid(row=4,column=0,columnspan=4)
def div():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:    
        try:
            output=int(e1.get())/int(e2.get())
            w=Message(root,text=str(output),width=51).grid(row=4,column=0,columnspan=4)
        except ZeroDivisionError:
            messagebox.showinfo("ERROR",'You cannot divide a number by 0')
def clear():
    w=Message(root,text="").grid(row=4,column=0,columnspan=4)
    
#to take the input
l1=Label(root,text="Enter the first number:").grid(row=0,column=0,columnspan=4)
e1=Entry(root,bd=10,width=51)
e1.grid(row=1,column=0,columnspan=4)
l2=Label(root,text="Enter the second number:").grid(row=2,column=0,columnspan=4)
e2=Entry(root,bd=10,width=51)
e2.grid(row=3,column=0,columnspan=4)
   
#to take the operation to perform
b_add=Button(root,text="+",width=10,height=3,command=add,bg="lightgrey").grid(row=6,column=3,rowspan=2)
b_sub=Button(root,text="-",width=10,height=3,command=sub,bg="lightgrey").grid(row=8,column=3,rowspan=2)
b_mul=Button(root,text="x",width=22,command=mul,bg="lightgrey").grid(row=5,column=0,columnspan=2)
b_div=Button(root,text="/",width=22,command=div,bg="lightgrey").grid(row=5,column=2,columnspan=2)
b_clr=Button(root,text="CE",command=clear).grid(row=9,column=0,columnspan=4)
#= button does nothing
#b_equal=Button(root,text="=",width=51,bg="lightgrey").grid(row=,column=,columnspan=)
b1=Button(root,text="1",width=10).grid(row=8,column=2)
b2=Button(root,text="2",width=10).grid(row=8,column=1)
b3=Button(root,text="3",width=10).grid(row=8,column=0)

b4=Button(root,text="4",width=10).grid(row=7,column=2)
b5=Button(root,text="5",width=10).grid(row=7,column=1)
b6=Button(root,text="6",width=10).grid(row=7,column=0)

b7=Button(root,text="7",width=10).grid(row=6,column=2)
b8=Button(root,text="8",width=10).grid(row=6,column=1)
b9=Button(root,text="9",width=10).grid(row=6,column=0)
b0=Button(root,text="0",width=33).grid(row=9,column=0,columnspan=3)

root.mainloop()
