import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Sidebar Menu Demo")
root.geometry("700x400")
root.configure(bg="#f0f0f0")


sidebar = tk.Frame(root, bg="#1db954", width=250)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)


def show_message(msg):
    messagebox.showinfo("Menu", f"Bạn chọn: {msg}")


buttons = [
    ("🏠  Home", lambda: show_message("Home")),
    ("📚  Courses", lambda: show_message("Courses")),
    ("⭐  Streak", lambda: show_message("Streak")),
    ("⚙️  Settings", lambda: show_message("Settings")),
    ("🚪  Logout", root.quit)
]

for text, cmd in buttons:
    btn = tk.Button(
        sidebar, text=text, command=cmd,
        font=("Arial", 12), fg="white", bg="#1db954",
        bd=0, activebackground="#17a74a", anchor="w", padx=20
    )
    btn.pack(fill="x", pady=15)
    btn.pack(fill="y", padx=15)
    #btn.pack(expand = True, anchor = "center") Nghiên cứu thêm

# ======== Khu vực nội dung chính ========
main_frame = tk.Frame(root, bg="white")
main_frame.pack(side="right", fill="both", expand=True)

label = tk.Label(
    main_frame,
    text="",
    font=("Arial", 16), bg="white"
)
label.pack(expand=True)

root.mainloop()
