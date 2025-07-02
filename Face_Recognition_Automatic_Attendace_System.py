import os
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
from main import Face_Recognition_System  # your existing face-recognition module

class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")
        self.root.wm_iconbitmap("front.ico")

        # Background image
        bg_image = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\student.jpg")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Login frame
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Profile image
        profile_img = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\user.jpg")
        profile_img = profile_img.resize((100, 100), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(profile_img)
        Label(frame, image=self.photo, bg="black").place(x=120, y=0, width=100, height=100)

        # Title
        Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black").place(x=60, y=100)

        # Username field
        Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black").place(x=40, y=150)
        self.username_entry = ttk.Entry(frame, font=("times new roman", 15))
        self.username_entry.place(x=40, y=180, width=270)

        # Password field
        Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black").place(x=40, y=220)
        self.password_entry = ttk.Entry(frame, font=("times new roman", 15), show="*")
        self.password_entry.place(x=40, y=250, width=270)

        # Buttons
        Button(frame, text="Login", command=self.login, font=("times new roman", 15, "bold"), bg="blue", fg="white")\
            .place(x=110, y=300, width=120, height=35)
        Button(frame, text="Forgot Password?", command=self.forgot_password, font=("times new roman", 12, "bold"),
               fg="white", bg="black", cursor="hand2").place(x=40, y=350)
        Button(frame, text="New User? Register", command=self.register_window, font=("times new roman", 12, "bold"),
               fg="white", bg="black", cursor="hand2").place(x=40, y=380)

    def clear(self):
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

    def login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "All fields are required")
            return
        if username == "admin" and password == "password":
            messagebox.showinfo("Success", "Welcome to the system!")
            self.clear()
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="246800", database="mydata")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (username, password))
            row = cursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Error", "Invalid Username or Password")
            else:
                proceed = messagebox.askyesno("Confirm", "Access only for admin. Continue?")
                if proceed:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_Recognition_System(self.new_window)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"{e}")
        finally:
            self.clear()

    def forgot_password(self):
        email = self.username_entry.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter your email address")
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="246800", database="mydata")
            cursor = conn.cursor()
            cursor.execute("SELECT securityQ, securityA FROM register WHERE email=%s", (email,))
            row = cursor.fetchone()
            conn.close()
            if row is None:
                messagebox.showerror("Error", "Please enter a valid email address")
            else:
                question, stored_answer = row
                self.open_reset_window(email, question, stored_answer)
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"{e}")

    def open_reset_window(self, email, question, stored_answer):
        self.reset_win = Toplevel(self.root)
        self.reset_win.title("Reset Password")
        self.reset_win.geometry("400x400+600+200")
        self.reset_win.config(bg="white")

        self.reset_email = email
        self.stored_answer = stored_answer

        Label(self.reset_win, text="Reset Password", font=("times new roman", 20, "bold"), bg="white").pack(pady=20)
        Label(self.reset_win, text="Security Question:", font=("times new roman", 12, "bold"), bg="white").pack(pady=(10,0))
        Label(self.reset_win, text=question, font=("times new roman", 12), bg="white").pack(pady=(0,15))

        Label(self.reset_win, text="Answer", font=("times new roman", 12, "bold"), bg="white").pack()
        self.answer_entry = ttk.Entry(self.reset_win, font=("times new roman", 12))
        self.answer_entry.pack(pady=(0,10))

        Label(self.reset_win, text="New Password", font=("times new roman", 12, "bold"), bg="white").pack()
        self.new_pass_entry = ttk.Entry(self.reset_win, font=("times new roman", 12), show="*")
        self.new_pass_entry.pack(pady=(0,10))

        Label(self.reset_win, text="Confirm Password", font=("times new roman", 12, "bold"), bg="white").pack()
        self.confirm_pass_entry = ttk.Entry(self.reset_win, font=("times new roman", 12), show="*")
        self.confirm_pass_entry.pack(pady=(0,15))

        Button(self.reset_win, text="Reset Password", command=self.reset_password,
               font=("times new roman", 12, "bold"), bg="green", fg="white").pack(pady=10)

    def reset_password(self):
        ans = self.answer_entry.get().strip()
        pwd = self.new_pass_entry.get().strip()
        cpwd = self.confirm_pass_entry.get().strip()

        if not ans or not pwd or not cpwd:
            messagebox.showerror("Error", "All fields are required", parent=self.reset_win)
            return
        if ans.lower() != self.stored_answer.lower():
            messagebox.showerror("Error", "Security answer is incorrect", parent=self.reset_win)
            return
        if pwd != cpwd:
            messagebox.showerror("Error", "Passwords do not match", parent=self.reset_win)
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="246800", database="mydata")
            cursor = conn.cursor()
            cursor.execute("UPDATE register SET password=%s WHERE email=%s", (pwd, self.reset_email))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Password reset successfully", parent=self.reset_win)
            self.reset_win.destroy()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"{e}", parent=self.reset_win)

    def register_window(self):
        self.root.destroy()
        root = Tk()
        RegisterWindow(root)
        root.mainloop()


class RegisterWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1530x790+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()

        # Background
        bg_image = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\student.jpg")
        bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.LANCZOS)
        self.bg = ImageTk.PhotoImage(bg_image)
        Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        # Side image
        side_img = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\front.jpg")
        side_img = side_img.resize((470, 550), Image.LANCZOS)
        self.bg1 = ImageTk.PhotoImage(side_img)
        Label(self.root, image=self.bg1).place(x=50, y=100, width=470, height=550)

        # Registration frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=900, height=550)
        Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white").place(x=20, y=20)

        # Form fields...
        Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=100)
        ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15)).place(x=50, y=130, width=250)
        Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=100)
        ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15)).place(x=370, y=130, width=250)

        Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=170)
        ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15)).place(x=50, y=200, width=250)
        Label(frame, text="Email ID", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=170)
        ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15)).place(x=370, y=200, width=250)

        Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=240)
        combo = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 13), state="readonly")
        combo['values'] = ("Select", "Your Birth Place", "Your Pet Name", "Your Childhood Bestfriend")
        combo.current(0); combo.place(x=50, y=270, width=250)

        Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=240)
        ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15)).place(x=370, y=270, width=250)

        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white").place(x=50, y=310)
        ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15), show="*")\
            .place(x=50, y=340, width=250)

        Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white").place(x=370, y=310)
        ttk.Entry(frame, textvariable=self.var_confirm_password, font=("times new roman", 15), show="*")\
            .place(x=370, y=340, width=250)

        Checkbutton(frame, text="I Agree To Terms & Conditions", variable=self.var_confirm_password,
                    font=("times new roman", 12), onvalue=1, offvalue=0, bg="white").place(x=50, y=380)

        Button(frame, text="Register", command=self.register_data,
               font=("times new roman", 15, "bold"), bg="green", fg="white").place(x=50, y=430, width=150)

        # **Updated** Back to Login button:
        Button(frame, text="Back to Login", command=self.back_to_login,
               font=("times new roman", 15, "bold"), bg="blue", fg="white").place(x=400, y=430, width=150)

    def register_data(self):
        if (not self.var_fname.get() or not self.var_email.get() or
            self.var_securityQ.get() == "Select"):
            messagebox.showerror("Error", "All fields are required!")
            return
        if self.var_password.get() != self.var_confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match!")
            return
        try:
            conn = mysql.connector.connect(host="localhost", username="root",
                                           password="246800", database="mydata")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM register WHERE email=%s", (self.var_email.get(),))
            if cursor.fetchone():
                messagebox.showerror("Error", "User already exists!")
            else:
                cursor.execute(
                    "INSERT INTO register (fname, lname, contact, email, security_q, security_a, password) "
                    "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_fname.get(),
                        self.var_lname.get(),
                        self.var_contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_password.get()
                    )
                )
                conn.commit()
                messagebox.showinfo("Success", "Registered Successfully")
            conn.close()
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"{e}")

    def back_to_login(self):
        """Destroy this window and re-launch the login page on a fresh root."""
        self.root.destroy()
        root = Tk()
        LoginWindow(root)
        root.mainloop()


def main():
    root = Tk()
    LoginWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
