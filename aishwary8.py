import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())

    chars = string.ascii_letters + string.digits + string.punctuation

    password = "".join(random.choice(chars) for _ in range(length))

    result.delete(0, tk.END)
    result.insert(0, password)

root = tk.Tk()
root.title("Aishu_Password_Generator")
root.geometry("400x200")

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)

length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

tk.Button(root, text="Generate Password",
          command=generate_password).pack(pady=10)

result = tk.Entry(root, width=35, font=("Arial", 12))
result.pack(pady=10)

root.mainloop()