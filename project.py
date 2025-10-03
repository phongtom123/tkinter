import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Sidebar 2 bên + Header Demo")
root.geometry("900x500")
root.configure(bg="#f0f0f0")

# ===== Header =====
header = tk.Frame(root, bg="#333", height=50)
header.grid(row=0, column=0, columnspan=3, sticky="nsew")

title_label = tk.Label(header, text="My Application", font=("Arial", 14, "bold"), bg="#333", fg="white")
title_label.pack(side="left", padx=10)

# ====== Sidebar Trái ======
sidebar_left = tk.Frame(root, bg="#1db954", width=180)

def show_message(msg):
    messagebox.showinfo("Menu", f"Bạn chọn: {msg}")

buttons_left = [
    ("🏠 Home", lambda: show_message("Home")),
    ("📚 Courses", lambda: show_message("Courses")),
    ("⭐ Streak", lambda: show_message("Streak")),
    ("⚙️ Settings", lambda: show_message("Settings")),
    ("🚪 Logout", root.quit)
]

for text, cmd in buttons_left:
    btn = tk.Button(
        sidebar_left, text=text, command=cmd,
        font=("Arial", 12), fg="white", bg="#1db954",
        bd=0, activebackground="#17a74a", anchor="w", padx=20
    )
    btn.pack(fill="x", pady=10)

# ====== Sidebar Phải ======
sidebar_right = tk.Frame(root, bg="#ff9800", width=200)

label_right = tk.Label(sidebar_right, text="📖 Bài tập đang học", font=("Arial", 12, "bold"), bg="#ff9800", fg="white")
label_right.pack(pady=10)

for i in range(1, 6):
    task = tk.Label(sidebar_right, text=f"• Bài tập {i}", font=("Arial", 11), bg="#ff9800", fg="white", anchor="w")
    task.pack(fill="x", padx=10, pady=2)

# ====== Main Frame ======
main_frame = tk.Frame(root, bg="white")
main_label = tk.Label(main_frame, text="Nội dung chính", font=("Arial", 16), bg="white")
main_label.pack(expand=True)

# ====== Toggle Sidebar ======
is_left_open = True
is_right_open = True

def toggle_left():
    global is_left_open
    if is_left_open:
        sidebar_left.grid_forget()
    else:
        sidebar_left.grid(row=1, column=0, sticky="ns")
    is_left_open = not is_left_open

def toggle_right():
    global is_right_open
    if is_right_open:
        sidebar_right.grid_forget()
    else:
        sidebar_right.grid(row=1, column=2, sticky="ns")
    is_right_open = not is_right_open

# Buttons toggle
btn_left = tk.Button(header, text="☰ Left", font=("Arial", 12), command=toggle_left, bg="#333", fg="white", bd=0)
btn_left.pack(side="right", padx=5)

btn_right = tk.Button(header, text="☰ Right", font=("Arial", 12), command=toggle_right, bg="#333", fg="white", bd=0)
btn_right.pack(side="right", padx=5)

# ====== Layout Grid ======
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

sidebar_left.grid(row=1, column=0, sticky="ns")
main_frame.grid(row=1, column=1, sticky="nsew")
sidebar_right.grid(row=1, column=2, sticky="ns")

root.mainloop()
