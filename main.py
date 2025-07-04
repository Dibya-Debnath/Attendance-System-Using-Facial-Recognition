from sqlite3 import Time
from tkinter import*
from tkinter import ttk
import tkinter
from tkinter import messagebox
import tkinter.messagebox  
from PIL import Image, ImageTk
from student import Student 
import os 
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from developer import Developer
from help import HelpDeskApp
from time import strftime
from datetime import datetime, time
from chatbot import ChatbotApp

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("front.ico")

        # 1st img
        img = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\front.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # 2nd img
        img1 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\aoo.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=500, height=130)
        

        # 3rd img
        img2 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\fa.jpg")
        img2 = img2.resize((600, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=550, height=130)
        
        
        # background img
        img3 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\backgrd.jpg")
        img3 = img3.resize((1525, 730), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1525, height=730)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="WHITE", fg="BLACK")
        title_lbl.place(x=0, y=0, width=1530, height=45)

       # Display time
        self.display_time()
    
     
           
        
        # student button
        img4 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\student.jpg")
        img4 = img4.resize((220, 200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="STUDENT DETAILS", command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\rec.jpg")
        img5 = img5.resize((220, 200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="FACE DETECTOR", cursor="hand2", command=self.face_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance face button
        img6 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\att.jpg")
        img6 = img6.resize((220, 200), Image.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2",command=self.attenendance_data)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="ATTENDANCE", cursor="hand2",command=self.attenendance_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help desk button
        img7 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\helpp.jpg")
        img7 = img7.resize((220, 200), Image.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2",command=self.chat_data)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="CHAT BOT", cursor="hand2",command=self.chat_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train face button
        img8 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\teain.jpg")
        img8 = img8.resize((220, 200), Image.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="TRAIN DATA", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        # Photos face button
        img9 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\studentpho.jpg")
        img9 = img9.resize((220, 200), Image.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2",command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="PHOTOS", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        # Development face button
        img10 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\devlop.jpg")
        img10 = img10.resize((220, 200), Image.LANCZOS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2",command=self.developer_data)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="DEVELOPER", cursor="hand2",command=self.developer_data,font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        # Exit face button
        img11 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\exitj.jpg")
        img11 = img11.resize((220, 200), Image.LANCZOS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2",command=self.iExit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="EXIT DESK", cursor="hand2",command=self.iExit, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)


    def display_time(self):
        def update_time():
            current_time = strftime('%H:%M:%S %p')
            lbl_time.config(text=current_time)
            lbl_time.after(1000, update_time)
        lbl_time = Label(self.root, font=('times new roman', 14, 'bold'), bg='black', fg='white')
        lbl_time.place(x=1300, y=5, width=200, height=40)
        update_time()
        
    def open_img(self):
        os.startfile("data") 

    def iExit(self):
        # Ask for confirmation before exiting
        self.iExit = messagebox.askyesno("Face Recognition", "Are you sure you want to exit this project?", parent=self.root)
        
        # If the user chooses 'Yes'
        if self.iExit:
            self.root.destroy()  # Properly close the window
        else:
            return  # Do nothing if 'No' is chosen            
        
        

     #=====================Function buttons==============================
     
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window) 

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=FaceRecognition(self.new_window)

    def attenendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window) 


    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    #def help_data(self):
    #    self.new_window=Toplevel(self.root)
    #    self.app=HelpDeskApp(self.new_window)
    
    def chat_data(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatbotApp(self.new_window)    

                         
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()