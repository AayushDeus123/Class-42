from tkinter import *

def calculate():
    p = float(p_entry.get())
    r = float(r_entry.get())
    t = float(t_entry.get())

    si = (p * r * t) / 100
    ci = p * ((1 + r / 100) ** t) - p

    result.config(text=f"SI: {si:.2f}, CI: {ci:.2f}")

root = Tk()
root.geometry("400x400")
root.title("Age Calculator App")

Label(root, text="Principal").pack()
p_entry = Entry(root)
p_entry.pack()

Label(root, text="Rate (%)").pack()
r_entry = Entry(root)
r_entry.pack()

Label(root, text="Time (years)").pack()
t_entry = Entry(root)
t_entry.pack()

Button(root, text="Calculate", command=calculate).pack(pady=10)
result = Label(root, text="")
result.pack()

root.mainloop()