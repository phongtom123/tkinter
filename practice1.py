import tkinter as tk
import ttkbootstrap as ttk

def printt():
    print("print")

# Tạo window
window = ttk.Window()
window.title("practice1")
window.geometry("440x520")

# widgets
text = tk.Text(master = window)
text.pack()

# ttk
label = ttk.Label(master = window, text = "test")
label.pack()

#Entry
entry = ttk.Entry(master = window)
entry.pack()

#Button
button = ttk.Button(master = window, text = "Button", command = printt)
button.pack()

def entryy():
    print("Hello")

frame = ttk.Frame(window)
frame.pack()

entry = ttk.Entry(master = window)
entry.pack(in_ = frame, side = "left")

label = ttk.Label(master = window, text ="my label")
label.pack(in_ = frame, side = "left")

# button = ttk.Button(master = window, command = entryy, text = "Button")
button = ttk.Button(master = window, command = lambda: print("hello"), text = "Button")
button.pack(in_ = frame, side = "left")

window.mainloop()

print("practicing")