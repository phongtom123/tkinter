import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Sidebar + Header Demo")
root.geometry("700x400")
root.configure(bg="#f0f0f0")

# ===== Header =====
header = tk.Frame(root, bg="#333", height=50)
header.pack(side="top", fill="x")

title_label = tk.Label(header, text="My Application", font=("Arial", 14, "bold"), bg="#333", fg="white")
title_label.pack(side="left", padx=10)

# ====== Sidebar ======
sidebar = tk.Frame(root, bg="#1db954", width=200)

def show_message(msg):
    messagebox.showinfo("Menu", f"Bạn chọn: {msg}")

buttons = [
    ("🏠 Home", lambda: show_message("Home")),
    ("📚 Courses", lambda: show_message("Courses")),
    ("⭐ Streak", lambda: show_message("Streak")),
    ("⚙️ Settings", lambda: show_message("Settings")),
    ("🚪 Logout", root.quit)
]

for text, cmd in buttons:
    btn = tk.Button(
        sidebar, text=text, command=cmd,
        font=("Arial", 12), fg="white", bg="#1db954",
        bd=0, activebackground="#17a74a", anchor="w", padx=20
    )
    btn.pack(fill="x", pady=10)

# ====== Main Frame ======
main_frame = tk.Frame(root, bg="white")
main_frame.pack(side="right", fill="both", expand=True)

label = tk.Label(main_frame, text="Demo Sidebar + Header", font=("Arial", 16), bg="white")
label.pack(expand=True)

# ====== Toggle Sidebar ======
is_open = True

def toggle_sidebar():
    global is_open
    if is_open:
        sidebar.pack_forget()   # ẩn sidebar
    else:
        sidebar.pack(side="left", fill="y")
    is_open = not is_open

# ====== Nút Toggle nằm trong header ======
toggle_btn = tk.Button(header, text="☰", font=("Arial", 14), command=toggle_sidebar, bg="#333", fg="white", bd=0)
toggle_btn.pack(side="right", padx=10)

# Hiện sidebar ban đầu
sidebar.pack(side="left", fill="y")

root.mainloop()
