import tkinter as tk
root = tk.Tk()

tk.Label(root, text="Hng 1", bg="red").pack(side = "left")
tk.Label(root, text="Hng 2", bg="green").pack(side = "right")
tk.Label(root, text="Hng 3", bg="blue").pack()

root.mainloop()
