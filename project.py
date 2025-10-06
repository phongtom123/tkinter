import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk   # dùng Pillow để load ảnh JPG/PNG

root = tk.Tk()
root.title("Sidebar 2 bên + Header Demo")
root.geometry("900x500")
root.configure(bg="#f0f0f0")

# ===== Header =====
header = tk.Frame(root, bg="#333", height=80)
header.grid(row=0, column=0, columnspan=3, sticky="nsew")

title_label = tk.Label(header, text="My Application", font=("Arial", 14, "bold"),
                       bg="#333", fg="white")
title_label.pack(side="left", padx=20, pady=20)

# ===== Avatar (phải) =====
# Load ảnh và resize nhỏ lại cho vừa header
avatar_img = Image.open("./photos/avataaars.png")
avatar_img = avatar_img.resize((50, 50))  # chỉnh kích thước avatar
avatar_photo = ImageTk.PhotoImage(avatar_img)

def avatar_clicked(event):
    messagebox.showinfo("Avatar", "Bạn vừa click vào avatar!")

avatar_label = tk.Label(header, image=avatar_photo, bg="#333", cursor="hand2")
avatar_label.pack(side="right", padx=20, pady=10)
avatar_label.bind("<Button-1>", avatar_clicked)   # click được vào avatar

# ====== Sidebar Trái ======
sidebar_left = tk.Frame(root, bg="#1db954", width=180, height=500)
sidebar_left.grid(row=1, column=0, sticky="ns")
sidebar_left.grid_propagate(False)   # Giữ sidebar cố định

# ====== Main Frame ======
main_frame = tk.Frame(root, bg="white")
main_frame.grid(row=1, column=1, sticky="nsew")

def show_message(msg):
    messagebox.showinfo("Menu", f"Bạn chọn: {msg}")

# Hàm hiển thị nội dung trong main_frame
def show_in_main(title, options):
    for widget in main_frame.winfo_children():
        widget.destroy()

    lbl = tk.Label(main_frame, text=title, font=("Arial", 16, "bold"), bg="white")
    lbl.pack(pady=10)

    # Danh sách màu cho các Unit
    colors = ["blue", "green", "yellow"]

    for i, opt in enumerate(options):
        btn = tk.Button(main_frame, text=opt, font=("Arial", 14, "bold"),
                        command=lambda x=opt: show_message(f"{title} - {x}"),
                        bg=colors[i % len(colors)],
                        fg="white" if colors[i] != "yellow" else "black",
                        width=30, height=2,
                        relief="raised", bd=4, highlightthickness=0,
                        activebackground="#666")
        btn.pack(pady=20)   # cách đều 20px

# ====== Nút chính ======
btn_home = tk.Button(sidebar_left, text="🏠 Home",
                     command=lambda: show_in_main("Home", ["Welcome to Home"]),
                     font=("Arial", 12), fg="white", bg="#1db954",
                     bd=0, activebackground="#17a74a", anchor="w", padx=20)
btn_home.grid(row=0, column=0, sticky="ew", pady=5)

# ====== Toggle Courses ======
courses_open = False
courses_frame = tk.Frame(sidebar_left, bg="#14833b")

btn_reading = tk.Button(courses_frame, text="📖 Reading",
                        command=lambda: show_in_main("Reading", ["Unit 1", "Unit 2", "Unit 3"]),
                        font=("Arial", 11), fg="white", bg="#14833b",
                        bd=0, activebackground="#0f5c29", anchor="w", padx=40)
btn_reading.pack(fill="x", pady=3)

btn_listening = tk.Button(courses_frame, text="🎧 Listening",
                          command=lambda: show_in_main("Listening", ["Unit 1", "Unit 2", "Unit 3"]),
                          font=("Arial", 11), fg="white", bg="#14833b",
                          bd=0, activebackground="#0f5c29", anchor="w", padx=40)
btn_listening.pack(fill="x", pady=3)

def toggle_courses():
    global courses_open
    if courses_open:
        courses_frame.grid_remove()
        courses_open = False
    else:
        courses_frame.grid(row=2, column=0, sticky="ew")
        courses_open = True

btn_courses = tk.Button(sidebar_left, text="📚 Courses", command=toggle_courses,
                        font=("Arial", 12), fg="white", bg="#1db954",
                        bd=0, activebackground="#17a74a", anchor="w", padx=20)
btn_courses.grid(row=1, column=0, sticky="ew", pady=5)

courses_frame.grid_remove()  # ẩn mặc định

# ====== Các nút khác ======
btn_streak = tk.Button(sidebar_left, text="⭐ Streak",
                       command=lambda: show_in_main("Streak", ["Day 1"]),
                       font=("Arial", 12), fg="white", bg="#1db954",
                       bd=0, activebackground="#17a74a", anchor="w", padx=20)
btn_streak.grid(row=3, column=0, sticky="ew", pady=5)

btn_settings = tk.Button(sidebar_left, text="⚙️ Settings",
                         command=lambda: show_in_main("Settings", ["Profile", "Security"]),
                         font=("Arial", 12), fg="white", bg="#1db954",
                         bd=0, activebackground="#17a74a", anchor="w", padx=20)
btn_settings.grid(row=4, column=0, sticky="ew", pady=5)

btn_logout = tk.Button(sidebar_left, text="🚪 Logout", command=root.quit,
                       font=("Arial", 12), fg="white", bg="#1db954",
                       bd=0, activebackground="#17a74a", anchor="w", padx=20)
btn_logout.grid(row=5, column=0, sticky="ew", pady=5)

# ====== Layout Grid ======
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

# Mặc định hiển thị Home
show_in_main("Home", ["Welcome to Home"])

root.mainloop()
