import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Sidebar cố định + Toggle Courses + Sidebar phải + Account")
root.geometry("1024x768")
root.configure(bg="#f0f0f0")

# ===== Sidebar Trái =====
sidebar_left = tk.Frame(root, bg="#1db954", width=180)
sidebar_left.pack(side="left", fill="y")
sidebar_left.pack_propagate(False)

# ===== Logo =====
logo_frame = tk.Frame(sidebar_left, bg="#1db954", height=100)
logo_frame.pack(fill="x")
logo_frame.pack_propagate(False)

try:
    logo_img = Image.open("./photos/2.png")
    logo_img = logo_img.resize((150, 130))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(logo_frame, image=logo_photo, bg="#1db954")
    logo_label.image = logo_photo
    logo_label.pack(pady=20)
except:
    logo_label = tk.Label(logo_frame, text="My Logo", font=("Arial", 16, "bold"), fg="white", bg="#1db954")
    logo_label.pack(pady=20)

# ===== Main Frame =====
main_frame = tk.Frame(root, bg="white")
main_frame.pack(side="left", fill="both", expand=True, padx=(0, 0))

def show_message(msg):
    messagebox.showinfo("Menu", f"Bạn chọn: {msg}")

def show_in_main(title, options):
    for widget in main_frame.winfo_children():
        widget.destroy()
    lbl = tk.Label(main_frame, text=title, font=("Arial", 16, "bold"), bg="white")
    lbl.pack(pady=10)
    colors = ["#3498db", "#2ecc71", "#f1c40f"]
    for i, opt in enumerate(options):
        btn = tk.Button(
            main_frame,
            text=opt,
            font=("Arial", 14, "bold"),
            command=lambda x=opt: show_message(f"{title} - {x}"),
            bg=colors[i % len(colors)],
            fg="white" if colors[i] != "#f1c40f" else "black",
            width=30,
            height=2,
            relief="raised",
            bd=4,
            highlightthickness=0,
            activebackground="#666"
        )
        btn.pack(pady=15)

# ===== Nút chính Sidebar trái =====
btn_home = tk.Button(sidebar_left, text="🏠 Home", command=lambda: show_in_main("Home", ["Welcome to Home"]),
                     font=("Arial", 12), fg="white", bg="#1db954", bd=0, activebackground="#17a74a",
                     anchor="w", padx=20)
btn_home.pack(fill="x", pady=5)

# ===== Toggle Courses =====
courses_open = False
btn_courses = tk.Button(sidebar_left, text="📚 Courses", font=("Arial", 12), fg="white", bg="#1db954",
                        bd=0, activebackground="#17a74a", anchor="w", padx=20)
btn_courses.pack(fill="x", pady=5)

# Các mục con Courses
btn_reading = tk.Button(sidebar_left, text="📖 Reading", command=lambda: show_in_main("Reading", ["Unit 1", "Unit 2", "Unit 3"]),
                        font=("Arial", 11), fg="white", bg="#14833b", bd=0, activebackground="#0f5c29", anchor="w", padx=40)
btn_listening = tk.Button(sidebar_left, text="🎧 Listening", command=lambda: show_in_main("Listening", ["Unit 1", "Unit 2", "Unit 3"]),
                          font=("Arial", 11), fg="white", bg="#14833b", bd=0, activebackground="#0f5c29", anchor="w", padx=40)
courses_sub = [btn_reading, btn_listening]

def toggle_courses():
    global courses_open
    if courses_open:
        for btn in courses_sub:
            btn.pack_forget()
        courses_open = False
    else:
        for btn in courses_sub:
            btn.pack(fill="x", pady=2, after=btn_courses)
        courses_open = True

btn_courses.config(command=toggle_courses)

# ===== Nút khác Sidebar trái =====
btn_streak = tk.Button(sidebar_left, text="⭐ Streak", command=lambda: show_in_main("Streak", ["Day 1"]),
                       font=("Arial", 12), fg="white", bg="#1db954", bd=0, activebackground="#17a74a",
                       anchor="w", padx=20)
btn_streak.pack(fill="x", pady=5)

btn_settings = tk.Button(sidebar_left, text="⚙️ Settings", command=lambda: show_in_main("Settings", ["Profile", "Security"]),
                         font=("Arial", 12), fg="white", bg="#1db954", bd=0, activebackground="#17a74a",
                         anchor="w", padx=20)
btn_settings.pack(fill="x", pady=5)

# ===== Toggle Account (thay cho Logout cũ) =====
account_open = False
btn_account = tk.Button(sidebar_left, text="👤 Account", font=("Arial", 12), fg="white", bg="#1db954",
                        bd=0, activebackground="#17a74a", anchor="w", padx=20)
btn_account.pack(fill="x", pady=5)

# Các mục con Account
btn_profile = tk.Button(sidebar_left, text="🧾 Profile", command=lambda: show_in_main("Profile", ["Thông tin cá nhân"]),
                        font=("Arial", 11), fg="white", bg="#14833b", bd=0,
                        activebackground="#0f5c29", anchor="w", padx=40)
btn_logout = tk.Button(sidebar_left, text="🚪 Logout", command=root.quit,
                       font=("Arial", 11), fg="white", bg="#14833b", bd=0,
                       activebackground="#0f5c29", anchor="w", padx=40)
account_sub = [btn_profile, btn_logout]

def toggle_account():
    global account_open
    if account_open:
        for btn in account_sub:
            btn.pack_forget()
        account_open = False
    else:
        for btn in account_sub:
            btn.pack(fill="x", pady=2, after=btn_account)
        account_open = True

btn_account.config(command=toggle_account)

# ===== Sidebar Phải =====
sidebar_right = tk.Frame(root, bg="#f0f0f0", width=200)
sidebar_right.pack(side="right", fill="y", padx=(10, 20), pady=10)
sidebar_right.pack_propagate(False)

# ===== Hàm tạo card bo tròn có viền =====
def create_rounded_card(parent, title, options):
    w, h = 180, 60 + 40*len(options)
    radius = 15

    # Canvas làm nền card
    canvas = tk.Canvas(parent, width=w, height=h, bg="#f0f0f0", bd=0, highlightthickness=0)
    canvas.pack(pady=10, padx=10)

    # Vẽ hình chữ nhật bo góc với viền
    canvas.create_polygon(
        [
            radius, 0, w-radius, 0,
            w, radius, w, h-radius,
            w-radius, h, radius, h,
            0, h-radius, 0, radius
        ],
        smooth=True,
        fill="white",
        outline="#d1d1d1",
        width=2
    )

    # Frame chứa nội dung
    frame = tk.Frame(canvas, bg="white")
    canvas.create_window((0,0), window=frame, anchor='nw', width=w, height=h)

    lbl = tk.Label(frame, text=title, font=("Arial", 12, "bold"), bg="white")
    lbl.pack(pady=(10,5), padx=10)

    for opt in options:
        btn = tk.Button(frame, text=opt, font=("Arial", 11), bg="#3498db", fg="white",
                        activebackground="#2980b9", bd=0)
        btn.pack(fill="x", padx=10, pady=5)

    return canvas

# ===== Tạo các card Sidebar phải =====
create_rounded_card(sidebar_right, "Streak", ["Thông báo 1"])
create_rounded_card(sidebar_right, "Bảng xếp hạng", ["Profile"])

# ===== Mặc định hiển thị Home =====
show_in_main("Home", ["Welcome to Home"])

root.mainloop()
