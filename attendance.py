from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import csv
import os

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")  
        self.root.wm_iconbitmap("front.ico")

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # ============ Images ============
        # 1st image
        img = Image.open("photos/front.jpg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=130)

        # 2nd image
        img1 = Image.open("photos/aoo.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)

        # 3rd image
        img2 = Image.open("photos/fa.jpg")
        img2 = img2.resize((550, 130), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=550, height=130)

        # Background image
        img3 = Image.open("photos/back.jpg")
        img3 = img3.resize((1525, 730), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1525, height=730)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 35, "bold"), bg="BLACK", fg="WHITE")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=55, width=1500, height=700)

        # Left frame
        left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"))
        left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("photos/fa.jpg")
        img_left = img_left.resize((720, 130), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(left_frame, image=self.photoimg_left).place(x=5, y=0, width=720, height=130)

        # Inside Left Frame
        left_inside_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        left_inside_frame.place(x=0, y=135, width=725, height=420)

        # Labels and Entries
        Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 13, "bold"), bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, width=20, font=("times new roman", 13, "bold")).grid(row=0, column=1, padx=10, pady=5, sticky=W)

        Label(left_inside_frame, text="Roll:", font=("comicsansns", 11, "bold"), bg="white").grid(row=0, column=2, padx=4, pady=8)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_roll, width=22, font=("comicsansns", 11, "bold")).grid(row=0, column=3, pady=8)

        Label(left_inside_frame, text="Name:", font=("comicsansns", 11, "bold"), bg="white").grid(row=1, column=0)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_name, width=22, font=("comicsansns", 11, "bold")).grid(row=1, column=1, pady=8)

        Label(left_inside_frame, text="Department:", font=("comicsansns", 11, "bold"), bg="white").grid(row=1, column=2)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_dep, width=22, font=("comicsansns", 11, "bold")).grid(row=1, column=3, pady=8)

        Label(left_inside_frame, text="Time:", font=("comicsansns", 11, "bold"), bg="white").grid(row=2, column=0)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_time, width=22, font=("comicsansns", 11, "bold")).grid(row=2, column=1, pady=8)

        Label(left_inside_frame, text="Date:", font=("comicsansns", 11, "bold"), bg="white").grid(row=2, column=2)
        ttk.Entry(left_inside_frame, textvariable=self.var_atten_date, width=22, font=("comicsansns", 11, "bold")).grid(row=2, column=3, pady=8)

        Label(left_inside_frame, text="Attendance Status:", font=("comicsansns", 11, "bold"), bg="white").grid(row=3, column=0)
        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance, font=("comicsansns", 11, "bold"), state="readonly", width=20)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, pady=8)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=300, width=715, height=35)

        Button(btn_frame, text="Import CSV", command=self.importCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=0)
        Button(btn_frame, text="Export CSV", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=1)
        Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white").grid(row=0, column=3)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"))
        right_frame.place(x=750, y=10, width=730, height=580)

        table_frame = Frame(right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=5, width=715, height=550)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.AttendaceReportTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "department", "time", "date", "attendance"),
                                                 xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendaceReportTable.xview)
        scroll_y.config(command=self.AttendaceReportTable.yview)

        self.AttendaceReportTable.heading("id", text="Attendance ID")
        self.AttendaceReportTable.heading("roll", text="Roll")
        self.AttendaceReportTable.heading("name", text="Name")
        self.AttendaceReportTable.heading("department", text="Department")
        self.AttendaceReportTable.heading("time", text="Time")
        self.AttendaceReportTable.heading("date", text="Date")
        self.AttendaceReportTable.heading("attendance", text="Attendance")
        self.AttendaceReportTable["show"] = "headings"

        for col in ("id", "roll", "name", "department", "time", "date", "attendance"):
            self.AttendaceReportTable.column(col, width=100)

        self.AttendaceReportTable.pack(fill=BOTH, expand=1)
        self.AttendaceReportTable.bind("<ButtonRelease>", self.get_curser)

    def fetchData(self, rows):
        self.AttendaceReportTable.delete(*self.AttendaceReportTable.get_children())
        for i in rows:
            self.AttendaceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", defaultextension=".csv",
                                               filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
            messagebox.showinfo("Data Exported", f"Data exported to {os.path.basename(fln)} successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def get_curser(self, event=""):
        cursor_focus = self.AttendaceReportTable.focus()
        content = self.AttendaceReportTable.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_atten_id.set(data[0])
            self.var_atten_roll.set(data[1])
            self.var_atten_name.set(data[2])
            self.var_atten_dep.set(data[3])
            self.var_atten_time.set(data[4])
            self.var_atten_date.set(data[5])
            self.var_atten_attendance.set(data[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

    def update_data(self):
        try:
            selected = self.AttendaceReportTable.focus()
            if not selected:
                messagebox.showerror("Error", "Please select a row to update", parent=self.root)
                return

            updated_row = (
                self.var_atten_id.get(),
                self.var_atten_roll.get(),
                self.var_atten_name.get(),
                self.var_atten_dep.get(),
                self.var_atten_time.get(),
                self.var_atten_date.get(),
                self.var_atten_attendance.get()
            )

            self.AttendaceReportTable.item(selected, values=updated_row)

            for i in range(len(mydata)):
                if mydata[i][0] == updated_row[0]:
                    mydata[i] = updated_row
                    break

            messagebox.showinfo("Success", "Record updated successfully!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Error while updating: {str(e)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
