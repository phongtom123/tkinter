import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Demo HTML/CSS style")

# Thanh header giống navbar
header = tk.Frame(root, bg="#333", height=50)
header.pack(fill="x")
tk.Label(header, text="My App", fg="white", bg="#333",
         font=("Arial", 16, "bold")).pack(padx=20, pady=10, side="left")

# Nội dung chính
content = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
content.pack(fill="both", expand=True)
ttk.Button(content, text="Bấm tôi").grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
