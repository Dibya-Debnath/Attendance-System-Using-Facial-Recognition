from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector
import cv2
import os
from datetime import datetime

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="white")
        self.root.wm_iconbitmap("front.ico")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Top image
        img_top = Image.open(os.path.join("photos", "face2.jpg"))
        img_top = img_top.resize((650, 700), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=0, y=55, width=650, height=700)

        # Bottom image
        img_bottom = Image.open(os.path.join("photos", "face.jpg"))
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Face recognition button
        btn_recognize = Button(f_lbl2, text="FACE RECOGNITION", cursor="hand2", command=self.face_recog,
                               font=("times new roman", 18, "bold"), bg="darkblue", fg="white")
        btn_recognize.place(x=200, y=590, width=500, height=70)

    def mark_attendance(self, student_id, name, roll, dep):
        attendance_report = "Attend.csv"
        if not os.path.exists(attendance_report):
            with open(attendance_report, "w", newline="") as f:
                f.write("ID,Name,Roll,Department,Time,Date,Status\n")

        with open(attendance_report, "a+", newline="") as f:
            now = datetime.now()
            time_str = now.strftime('%H:%M:%S')
            date_str = now.strftime('%d/%m/%Y')
            f.write(f"{student_id},{name},{roll},{dep},{time_str},{date_str},Present\n")
            print(f"✅ Attendance marked for {name} ({student_id})")

    def face_recog(self):
        # Load classifier and recognizer
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("classifier.xml")

        # Load today's recorded IDs
        today_str = datetime.now().strftime('%d/%m/%Y')
        recorded_today = set()
        if os.path.exists("Attend.csv"):
            with open("Attend.csv", "r") as f:
                for line in f.readlines()[1:]:
                    parts = line.strip().split(",")
                    if len(parts) >= 6 and parts[5] == today_str:
                        recorded_today.add(parts[0])

        # Start video capture
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                id_, confidence = recognizer.predict(roi_gray)
                conf_pct = int(100 * (1 - confidence/300))

                # Get student info from DB
                conn = mysql.connector.connect(host="localhost", user="root", password="246800", database="face_recognizer")
                cursor = conn.cursor()
                cursor.execute("SELECT Student_id, Name, Roll, Dep FROM student WHERE Student_id = %s", (id_,))
                result = cursor.fetchone()
                conn.close()

                if result and conf_pct > 77:
                    student_id, name, roll, dep = result
                    label = f"ID: {student_id} | Name: {name} | Dept: {dep}"
                    if str(student_id) not in recorded_today:
                        self.mark_attendance(student_id, name, roll, dep)
                        recorded_today.add(str(student_id))
                    color = (255, 0, 0)
                else:
                    label = "Unknown"
                    color = (0, 0, 255)

                # Draw rectangle and label
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
                cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

            cv2.imshow("Face Recognition", frame)

            if cv2.waitKey(1) & 0xFF == 13:  # Enter key
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()
