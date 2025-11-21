import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(entry.get())
    except:
        result_label.config(text="Enter a valid number!")
        return

    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for i in range(length))
    result_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

label = tk.Label(root, text="Enter password length:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

btn = tk.Button(root, text="Generate", command=generate_password)
btn.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
