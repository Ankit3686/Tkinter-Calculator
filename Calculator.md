# Tkinter-Calculator

import tkinter as tk
first_number=second_number=operator=None
root=tk.Tk()
root.title("calculator")
root.geometry("280x380")
root.resizable(0,0)
root.configure(background="black")

def get_digits(digit):  #function print digits number
    current=lable["text"]
    new=current+str(digit)
    lable.configure(text=new)

def clear(): #clear krne ke liya
    lable.configure(text="")
    
def get_operator(op): #operator store krne ki liya
    global first_number,operator
    first_number=int(lable["text"])
    operator=op
    lable.configure(text=" ")

def get_result(): #output print krnbane ki liya 
    global first_number,second_number,operator
    second_number=int(lable["text"])
    if operator=="+":
        lable.configure(text=str(first_number+second_number))
    elif operator=="-":
        lable.configure(text=str(first_number-second_number))
    elif operator=="*":
        lable.configure(text=str(first_number*second_number))
    else:
        if second_number==0:
            lable.configure(text="error")
        else:
            lable.configure(text=str(round(first_number/second_number,2)))       
    
lable=tk.Label(root,text="",bg="black",fg="white",width=8,height=2) #label lyne ki liya
lable.grid(row=0,column=0,columnspan=8,pady=(30,25),sticky="e") #sticky means word display left or right
lable.configure(font=("verdana",20,"bold"))

btn7=tk.Button(root,text="7",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(7))
btn7.grid(row=1,column=0)
btn7.configure(font=("verdana",14))
btn8=tk.Button(root,text="8",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(8))
btn8.grid(row=1,column=1)
btn8.configure(font=("verdana",14))
btn9=tk.Button(root,text="9",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(9))
btn9.grid(row=1,column=2)
btn9.configure(font=("verdana",14))
btn_add=tk.Button(root,text="+",bg="green",fg="yellow",width=5,height=2,command=lambda:get_operator("+"))
btn_add.grid(row=1,column=3)
btn_add.configure(font=("verdana",14))

btn4=tk.Button(root,text="4",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(4))
btn4.grid(row=2,column=0)
btn4.configure(font=("verdana",14))
btn5=tk.Button(root,text="5",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(5))
btn5.grid(row=2,column=1)
btn5.configure(font=("verdana",14))
btn6=tk.Button(root,text="6",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(6))
btn6.grid(row=2,column=2)
btn6.configure(font=("verdana",14))
btn_min=tk.Button(root,text="-",bg="green",fg="yellow",width=5,height=2,command=lambda:get_operator("-"))
btn_min.grid(row=2,column=3)
btn_min.configure(font=("verdana",14))

btn1=tk.Button(root,text="1",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(1))
btn1.grid(row=3,column=0)
btn1.configure(font=("verdana",14))
btn2=tk.Button(root,text="2",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(2))
btn2.grid(row=3,column=1)
btn2.configure(font=("verdana",14))
btn3=tk.Button(root,text="3",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(3))
btn3.grid(row=3,column=2)
btn3.configure(font=("verdana",14))
btn_mul=tk.Button(root,text="*",bg="green",fg="yellow",width=5,height=2,command=lambda:get_operator("*"))
btn_mul.grid(row=3,column=3)
btn_mul.configure(font=("verdana",14))

btn_clear=tk.Button(root,text="C",bg="green",fg="white",width=5,height=2,command=lambda:clear())
btn_clear.grid(row=4,column=0)
btn_clear.configure(font=("verdana",14))
btn0=tk.Button(root,text="0",bg="green",fg="white",width=5,height=2,command=lambda:get_digits(0))
btn0.grid(row=4,column=1)
btn0.configure(font=("verdana",14))
btn_eql=tk.Button(root,text="=",bg="green",fg="white",width=5,height=2,command=lambda:get_result())
btn_eql.grid(row=4,column=2)
btn_eql.configure(font=("verdana",14))
btn_div=tk.Button(root,text="/",bg="green",fg="yellow",width=5,height=2,command=lambda:get_operator("/"))
btn_div.grid(row=4,column=3)
btn_div.configure(font=("verdana",14))

root.mainloop() #program run krne ke liya
