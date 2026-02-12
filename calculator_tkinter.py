import tkinter as tk

def add():
    result.set(float(num1.get()) + float(num2.get()))

def subtract():
    result.set(float(num1.get()) - float(num2.get()))

def multiply():
    result.set(float(num1.get()) * float(num2.get()))

def divide():
    try:
        result.set(float(num1.get()) / float(num2.get()))
    except ZeroDivisionError:
        result.set("Cannot divide by 0")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")

# Variables
num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

# Input Fields
tk.Label(root, text="Number 1").pack()
tk.Entry(root, textvariable=num1).pack()

tk.Label(root, text="Number 2").pack()
tk.Entry(root, textvariable=num2).pack()

# Buttons
tk.Button(root, text="+", command=add).pack(pady=5)
tk.Button(root, text="-", command=subtract).pack(pady=5)
tk.Button(root, text="*", command=multiply).pack(pady=5)
tk.Button(root, text="/", command=divide).pack(pady=5)

# Result
tk.Label(root, text="Result:").pack()
tk.Label(root, textvariable=result, font="Arial 14 bold").pack()

root.mainloop()
