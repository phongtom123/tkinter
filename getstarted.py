import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    value = entryInt.get() * 1.61
    output_string.set(value)

#window = tk.Tk()
window = ttk.Window(themename = "journal")
window.title("Helo")
window.geometry("244x244")

title_label = ttk.Label(master = window, text = "Miles to kilometers", font = "Calibri 12 bold")
title_label.pack()
 

input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = "Chơi đê", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack()

output_string = tk.StringVar()
output_label = ttk.Label(master = window, font ="Calibri 12 bold", text = "Output", textvariable = output_string)
output_label.pack(pady =15)

tk.mainloop()