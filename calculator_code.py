from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("CalIt")

#first input number
text_data1=Label(root,text="Enter the first number",width=70).grid(row=0,column=0,columnspan=5)
input_data1=Entry(root,width=70).grid(row=1,column=0,columnspan=5)

#second input number
text_data2=Label(root,text="Enter the second number",width=70).grid(row=2,column=0,columnspan=5)
input_data2=Entry(root,width=70).grid(row=3,column=0,columnspan=5)


#Here will be the output message
#row=4
#numpad
num1=Button(root,text="1",width=12).grid(row=5,column=0)
num2=Button(root,text="2",width=12).grid(row=5,column=1)
num3=Button(root,text="3",width=12).grid(row=5,column=2)
num4=Button(root,text="4",width=12).grid(row=6,column=0)
num5=Button(root,text="5",width=12).grid(row=6,column=1)
num6=Button(root,text="6",width=12).grid(row=6,column=2)
num7=Button(root,text="7",width=12).grid(row=7,column=0)
num8=Button(root,text="8",width=12).grid(row=7,column=1)
num9=Button(root,text="9",width=12).grid(row=7,column=2)
num0=Button(root,text="0",width=26).grid(row=8,column=0,columnspan=2)

op_add=Button(root,text="+",width=12,command=sum).grid(row=6,column=3)
op_minus=Button(root,text="-",width=12).grid(row=5,column=3)
op_div=Button(root,text="/",width=12).grid(row=7,column=3)
op_mul=Button(root,text="X",width=12).grid(row=8,column=3)
op_equals=Button(root,text="=",width=12,height=7).grid(row=5,column=4,rowspan=4)
op_dot=Button(root,text=".",width=12).grid(row=8,column=2)


root.mainloop()
