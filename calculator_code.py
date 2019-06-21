from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("500x500")

def sum():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:
        output=int(e1.get())+int(e2.get())
        w=Message(f1,text="{}".format(output),width=80)
        w.grid(row=0,column=0)
def sub():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:
        output=int(e1.get())-int(e2.get())
        w=Message(f1,text=str(output),width=51).grid(row=0,column=0)
def mul():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:
        output=int(e1.get())*int(e2.get())
        w=Message(f1,text=str(output),width=51).grid(row=0,column=0)
def div():
    if e1.get()=="" or e2.get()=="":
        messagebox.showinfo("Error","Please enter the numbers.")
    else:    
        try:
            output=int(e1.get())/int(e2.get())
            w=Message(f1,text=str(output),width=51).grid(row=0,column=0)
        except ZeroDivisionError:
            messagebox.showinfo("ERROR",'You cannot divide a number by 0')
def clear():
    w=Message(root,text="").grid(row=0,column=0)
    
l1=Label(root,text="Enter the 1st number:").grid(row=0,column=0,columnspan=4)
e1=Entry(root,bd=5,width=80)
e1.grid(row=1,column=0,columnspan=4)
l2=Label(root,text="Enter the 2nd number:").grid(row=2,column=0,columnspan=4)
e2=Entry(root,bd=5,width=80)
e2.grid(row=3,column=0,columnspan=4)
#use frame and insert message box in it.
f1=Frame(root,height=40,width=480,highlightcolor="red",bg="blue")
f1.grid(row=4,column=0,columnspan=5)


        
#message box at row 4 

b1=Button(root,text="1",width=16).grid(row=5,column=0)
b2=Button(root,text="2",width=16).grid(row=5,column=1)
b3=Button(root,text="3",width=16).grid(row=5,column=2)
b_plus=Button(root,text="+",width=16,command=sum).grid(row=5,column=3)

b4=Button(root,text="4",width=16).grid(row=6,column=0)
b5=Button(root,text="5",width=16).grid(row=6,column=1)
b6=Button(root,text="6",width=16).grid(row=6,column=2)
b_minus=Button(root,text="-",width=16,command=sub).grid(row=6,column=3)

b7=Button(root,text="7",width=16).grid(row=7,column=0)
b8=Button(root,text="8",width=16).grid(row=7,column=1)
b9=Button(root,text="9",width=16).grid(row=7,column=2)
b_mul=Button(root,text="x",width=16,command=mul).grid(row=7,column=3)

b0=Button(root,text="0",width=34).grid(row=8,column=0,columnspan=2)
b_dot=Button(root,text=".",width=16).grid(row=8,column=2)
b_div=Button(root,text="/",width=16,command=div).grid(row=8,column=3)

root.mainloop()
