import tkinter as tk
import ttkbootstrap as ttk


# def button_func():
#     print(entry.get())

#     label.config(text = entry.get())
#     button.config(text = entry.get())
#     entry["state"] = "disable"
#     #print(label.configure())

# window = ttk.Window()

# window.geometry("244x244")

# label = ttk.Label(master = window, text = "Label")
# label.pack()

# entry = ttk.Entry(master = window)
# entry.pack()

# button = ttk.Button(master = window, text = "button", command = button_func)
# button.pack()

def button_func():
    label["text"] = entry.get()
    entry["state"] = "disable"

window = ttk.Window()
window.geometry("244x244")

entry = ttk.Entry(master = window)
entry.pack()

label = ttk.Label(master = window, text = "some text")
label.pack()

button = ttk.Button(master = window, command = button_func)
button.pack()


window.mainloop()