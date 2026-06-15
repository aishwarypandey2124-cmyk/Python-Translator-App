import tkinter as tk
import math

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Aishu_Calculator")
root.geometry("400x550")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=15)

buttons = [
    ['C', '√', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '**', '=']
]

frame = tk.Frame(root)
frame.pack()

for r, row in enumerate(buttons):
    for c, btn in enumerate(row):

        if btn == "=":
            command = equal
        elif btn == "C":
            command = clear
        elif btn == "√":
            command = sqrt
        else:
            command = lambda x=btn: press(x)

        tk.Button(
            frame,
            text=btn,
            font=("Arial", 18),
            width=5,
            height=2,
            command=command
        ).grid(row=r, column=c, padx=5, pady=5)

root.mainloop()