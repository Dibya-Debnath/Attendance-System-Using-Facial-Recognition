from tkinter import *
from tkinter import ttk
from unittest import result
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2
import os
from time import strftime
from datetime import datetime, time

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("front.ico")
        
        
        #==========================varibles=========================================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        
        
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
        img3 = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\back.jpg")
        img3 = img3.resize((1525, 730), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1525, height=730)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="BLACK", fg="WHITE")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=700)
        
        # Left label frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)
        
        img_left = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\fa.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=720, height=130)
        
     # Current course information
        current_course_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="CURRENT COURSE INFORMATION", font=("times new roman", 12, "bold"))
        current_course_frame.place(x=5, y=135, width=720, height=150)

        # Department
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 13, "bold"), state="readonly", width=20)
        dep_combo["values"] = ("Select Department", "CSE", "IT", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Course
        course_label = Label(current_course_frame, text="Course", font=("times new roman", 13, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 13, "bold"), state="readonly", width=20)
        course_combo["values"] = ("Select Course", "B.tech", "M.tech", "Bsc", "Bba")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Year
        year_label = Label(current_course_frame, text="Year", font=("times new roman", 13, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, sticky=W)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, font=("times new roman", 13, "bold"), state="readonly", width=20)
        year_combo["values"] = ("Select Year", "2021-2022", "2022-2023", "2023-2024", "2024-2025", "2025-2026")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # Semester
        semester_label = Label(current_course_frame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=10, sticky=W)

        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,  font=("times new roman", 13, "bold"), state="readonly", width=20)
        semester_combo["values"] = ("Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6", "Semester-7", "Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information
        class_student_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="CLASS STUDENT INFORMATION", font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=250, width=720, height=300)

        # Student ID
        studentId_label = Label(class_student_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame,textvariable=self.va_std_id, width=20,  font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        studentName_label = Label(class_student_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx=10, sticky=W)
        
        studentName_entry = ttk.Entry(class_student_frame,textvariable=self.var_std_name, width=20, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, sticky=W)
        
        # Class division
        class_div_label = Label(class_student_frame, text="Class Division:", font=("times new roman", 13, "bold"), bg="white")
        class_div_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div, font=("times new roman", 13, "bold"), state="readonly", width=18)
        div_combo["values"] = ("","A", "B", "C","D","E")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Roll number
        roll_no_label = Label(class_student_frame, text="Roll No:", font=("times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        
        roll_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_roll, width=20,  font=("times new roman", 13, "bold"))
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,  font=("times new roman", 13, "bold"), state="readonly", width=18)
        gender_combo["values"] = ("Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date of birth
        dob_label = Label(class_student_frame, text="DOB:", font=("times new roman", 13, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob, width=20,  font=("times new roman", 13, "bold"))
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email, width=20,  font=("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone number
        phone_label = Label(class_student_frame, text="Phone No:", font=("times new roman", 13, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        
        phone_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone, width=20,  font=("times new roman", 13, "bold"))
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address:", font=("times new roman", 13, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_address, width=20,  font=("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher name
        teacher_label = Label(class_student_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = ttk.Entry(class_student_frame,textvariable=self.var_teacher, width=20,  font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio buttons for photo sample status
        self.var_radio1 = StringVar()
        radionbtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6, column=0)
        
        radionbtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radionbtn2.grid(row=6, column=1)

        # Buttons Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=715, height=35)

        #save
        save_btn = Button(btn_frame, text="Save", width=17,command=self.add_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        #update
        update_btn = Button(btn_frame, text="Update", width=17,command=self.update_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)
         
        #delete
        delete_btn = Button(btn_frame, text="Delete", width=17,command=self.delete_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=2)

        #reset
        reset_btn = Button(btn_frame, text="Reset",  width=17,command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=3)
        
        btn_frame1 = Frame(class_student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=235, width=715, height=35)
        
        #take photo
        take_photo_btn=Button(btn_frame1,text="Take Photo",  width=35,command=self.generate_dataset,font=("time new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)
        
        #update photo
        update_photo_btn=Button(btn_frame1,text="update_photo",command=self.update_image,width=35,font=("time new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)
        
        
         

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=580)
        
        img_right = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\fa.jpg")
        img_right = img_right.resize((720, 130), Image.LANCZOS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl = Label(Right_frame, image=self.photoimg_right)
        f_lbl.place(x=5, y=0, width=710, height=130)
        
        
        #=======searching System=========
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("time new roman",12,"bold"))
        Search_frame.place(x=5,y=135,width=710,height=70)
        
        search_label=Label(Search_frame,text="Search By:",font=("time new roman",13,"bold"),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        Search_combo=ttk.Combobox(Search_frame,font=("time new roman",13,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll_No","Phone_No")
        Search_combo.current(0)
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(Search_frame,width=15,font=("time new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        Search_btn=Button(Search_frame,text="Search",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
        Search_btn.grid(row=0,column=3,padx=4)
        
        showAll_btn=Button(Search_frame,text="ShowAll",width=12,font=("time new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        
        #=============table frame=============
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student ID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    #================================function decration===============================
    
    def add_data(self): 
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="246800",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                                    self.var_dep.get(),
                                                                                                                    self.var_course.get(),
                                                                                                                    self.var_year.get(),
                                                                                                                    self.var_semester.get(),
                                                                                                                    self.va_std_id.get(),
                                                                                                                    self.var_std_name.get(),
                                                                                                                    self.var_div.get(),
                                                                                                                    self.var_roll.get(),
                                                                                                                    self.var_gender.get(),
                                                                                                                    self.var_dob.get(),
                                                                                                                    self.var_email.get(),
                                                                                                                    self.var_phone.get(),
                                                                                                                    self.var_address.get(),
                                                                                                                    self.var_teacher.get(),
                                                                                                                    self.var_radio1.get()
                                                                                                               ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details has been added Successfully", parent=self.root) 
            except Exception as es: 
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root) 
                
                   
        #=========================fetch data========================
    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="246800", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()
            
            if len(data) !=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()    
            conn.close()
        
            
            
    #=====================get cursor========================             
    def get_cursor(self, event=""): 
     cursor_focus = self.student_table.focus()
     content = self.student_table.item(cursor_focus)
     data = content.get("values", [])

     if not data or len(data) < 15:
         messagebox.showwarning("Selection Error", "Please select a valid row with complete student data.", parent=self.root)
         return

     self.var_dep.set(data[0])
     self.var_course.set(data[1])
     self.var_year.set(data[2])
     self.var_semester.set(data[3])
     self.va_std_id.set(data[4]) 
     self.var_std_name.set(data[5])
     self.var_div.set(data[6])
     self.var_roll.set(data[7])
     self.var_gender.set(data[8])
     self.var_dob.set(data[9])
     self.var_email.set(data[10])
     self.var_phone.set(data[11])
     self.var_address.set(data[12])
     self.var_teacher.set(data[13])
     self.var_radio1.set(data[14])


# ======================update function====================================
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate = messagebox.askyesno("Update", "Do you want to update this Student's details", parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="246800",database="face_recognizer")
                    my_cursor=conn.cursor()
                
                   # Corrected SQL Query
                    my_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s",(
                    
                                                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                                                self.var_course.get(),
                                                                                                                                                                                                self.var_year.get(),
                                                                                                                                                                                                self.var_semester.get(),
                                                                                                                                                                                                self.var_std_name.get(),
                                                                                                                                                                                                self.var_div.get(),
                                                                                                                                                                                                self.var_roll.get(),
                                                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                                                self.var_teacher.get(),
                                                                                                                                                                                                self.var_radio1.get(),
                                                                                                                                                                                                self.va_std_id.get()  # Corrected variable name
                                                                                                                                                                                             ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()     
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

#======delete Function===============
    def delete_data(self):
        if self.va_std_id.get()=="":
           messagebox.showinfo("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',username="root",password="246800",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close() 
                messagebox.showinfo("Delete","Successfully delete student detials",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)
 
 
 #===========Reset================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.va_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Male")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")
        
#=======================Generate Data Set or Take Photo Samples===================

    def generate_dataset(self):
      # 1) Validate required fields
      if (self.var_dep.get() == "Select Department" 
          or not self.var_std_name.get() 
          or not self.va_std_id.get()):
          messagebox.showerror("Error", "All fields are required", parent=self.root)
          return

      try:
          # 2) Connect to database
          conn = mysql.connector.connect(
              host="localhost",
              username="root",
              password="246800",
              database="face_recognizer"
          )
          cursor = conn.cursor()

          # 3) Insert or update student record
          cursor.execute("""
              INSERT INTO student (
                  Student_id, Dep, Course, Year, Semester, Name, Division,
                  Roll, Gender, Dob, Email, Phone, Address, Teacher, PhotoSample
              ) VALUES (
                  %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s
              )
              ON DUPLICATE KEY UPDATE
                  Dep=VALUES(Dep), Course=VALUES(Course), Year=VALUES(Year),
                  Semester=VALUES(Semester), Name=VALUES(Name), Division=VALUES(Division),
                  Roll=VALUES(Roll), Gender=VALUES(Gender), Dob=VALUES(Dob),
                  Email=VALUES(Email), Phone=VALUES(Phone), Address=VALUES(Address),
                  Teacher=VALUES(Teacher), PhotoSample=VALUES(PhotoSample)
          """, (
              self.va_std_id.get(),
              self.var_dep.get(),
              self.var_course.get(),
              self.var_year.get(),
              self.var_semester.get(),
              self.var_std_name.get(),
              self.var_div.get(),
              self.var_roll.get(),
              self.var_gender.get(),
              self.var_dob.get(),
              self.var_email.get(),
              self.var_phone.get(),
              self.var_address.get(),
              self.var_teacher.get(),
              self.var_radio1.get()
          ))

          conn.commit()
          self.fetch_data()
          self.reset_data()

          # 4) Prepare face detection
          face_cascade = cv2.CascadeClassifier(
              cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
          )

          def crop_face(frame):
              gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
              faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
              for (x, y, w, h) in faces:
                  return frame[y:y+h, x:x+w]
              return None

          # 5) Ensure data directory exists
          if not os.path.exists("data"):
              os.makedirs("data")

          # 6) Capture and save 100 face samples
          cap = cv2.VideoCapture(0)
          img_id = 0
          sid = self.va_std_id.get().strip()
          while img_id < 100:
              ret, frame = cap.read()
              if not ret:
                  break
              face = crop_face(frame)
              if face is not None:
                  img_id += 1
                  face_resized = cv2.resize(face, (450, 450))
                  gray_face = cv2.cvtColor(face_resized, cv2.COLOR_BGR2GRAY)
                  filename = f"data/user.{sid}.{img_id}.jpg"
                  cv2.imwrite(filename, gray_face)
                  cv2.putText(
                      gray_face, str(img_id), (50, 50),
                      cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2
                  )
                  cv2.imshow("Cropped Face", gray_face)

              if cv2.waitKey(1) == 13:  # Enter key to break early
                  break

          cap.release()
          cv2.destroyAllWindows()

          messagebox.showinfo(
              "Result",
              f"Generated {img_id} face samples for Student ID {sid}.",
              parent=self.root
          )

      except Exception as e:
          messagebox.showerror("Error", f"An unexpected error occurred:\n{e}", parent=self.root)
      finally:
          if conn.is_connected():
              conn.close()



#=======================update take photo========================================
    def update_image(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.va_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                # Connect to the database
                conn = mysql.connector.connect(host="localhost", username="root", password="246800", database="face_recognizer")
                my_cursor = conn.cursor()

                # Check if the student exists
                my_cursor.execute("SELECT * FROM Student WHERE Student_id=%s", (self.va_std_id.get(),))
                student = my_cursor.fetchone()

                if student is None:
                    messagebox.showerror("Error", "Student not found.", parent=self.root)
                    conn.close()
                    return

                # Update student record (if needed)
                my_cursor.execute("UPDATE Student SET Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.va_std_id.get()
                ))
                conn.commit()
                conn.close()

                # Initialize face classifier
                face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    for (x, y, w, h) in faces:
                        face_cropped = img[y:y + h, x:x + w]
                        return face_cropped
                    return None

                # Start video capture
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if not ret:
                        messagebox.showerror("Error", "Failed to capture image from camera.", parent=self.root)
                        break

                    cropped_face = face_cropped(my_frame)
                    if cropped_face is not None:
                        img_id += 1
                        face = cv2.resize(cropped_face, (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = f"data/user.{self.va_std_id.get()}.{img_id}.jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or img_id == 100:  # Press 'Enter' to exit or after 100 images
                        break

                cap.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Result", "Image dataset updated successfully!", parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


             
        
        
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
  