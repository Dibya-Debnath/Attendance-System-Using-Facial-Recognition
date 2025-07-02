from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        self.root.wm_iconbitmap("front.ico")

        # Title Label
        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="BLACK", fg="RED")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top Background Image
        img_top = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\ai-robot.jpg")
        img_top = img_top.resize((1530, 720), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        bg_lbl = Label(self.root, image=self.photoimg_top)
        bg_lbl.place(x=0, y=55, width=1530, height=720)

        # Main Content Frame
        main_frame = Frame(bg_lbl, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=1000, y=50, width=500, height=620)

        # Profile Image
        img_profile = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\help.jpg")
        img_profile = img_profile.resize((180, 180), Image.LANCZOS)
        self.photoimg_profile = ImageTk.PhotoImage(img_profile)

        profile_lbl = Label(main_frame, image=self.photoimg_profile, bg="white")
        profile_lbl.place(x=160, y=10, width=180, height=180)

        # Developer Info
        dev_name = Label(main_frame, text="Hello, I'm Dibya", font=("times new roman", 15, "bold"), bg="white", fg="black")
        dev_name.place(x=20, y=210)

        dev_role = Label(main_frame, text="Full Stack Developer", font=("times new roman", 13), bg="white", fg="gray")
        dev_role.place(x=20, y=240)

        dev_desc = Label(
            main_frame,
            text="Experienced in building robust web and desktop\n"
                 "applications using Python, JavaScript, MySQL,\n"
                 "OpenCV, and modern frameworks.",
            font=("times new roman", 12),
            bg="white",
            justify=LEFT
        )
        dev_desc.place(x=20, y=280)

        # Contact Title
        contact_title = Label(main_frame, text="Connect with me:", font=("times new roman", 13, "bold"), bg="white", fg="blue")
        contact_title.place(x=20, y=370)

        # Clickable Link Function
        def open_link(url):
            webbrowser.open_new(url)

        # Social Links
        links = {
            "GitHub": "https://github.com/Dibyarex",
            "LinkedIn": "https://www.linkedin.com/in/dibya-debnath-6b27b6200/",
            "Portfolio": "https://dibya.dev",  # example
            "Email": "https://mail.google.com/mail/u/0/#inbox?compose=CllgCJNsLlDpVtjBkPNjNLvzkNdFtqjXglgzjjXlNLCSRlQbqStPrQJKzmBKZqvDSBlnPXcJCLV"
        }

        y_position = 400
        for platform, url in links.items():
            link_lbl = Label(main_frame, text=platform, font=("times new roman", 12, "underline"), fg="blue", bg="white", cursor="hand2")
            link_lbl.place(x=40, y=y_position)
            link_lbl.bind("<Button-1>", lambda e, link=url: open_link(link))
            y_position += 30

        

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
