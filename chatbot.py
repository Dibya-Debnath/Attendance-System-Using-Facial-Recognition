from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chatbot")
        self.root.geometry("800x600+100+100")
        self.root.bind("<Return>", self.on_enter)
        self.root.wm_iconbitmap("front.ico")

        # Main frame for chat display
        main_frame = Frame(self.root, bd=4, bg="powder blue")
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Header with image and title
        img = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\devlop.jpg")
        img = img.resize((50, 50), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        header = Label(main_frame, image=self.photo, text=' Chatbot', compound=LEFT,
                       font=("Arial", 20, "bold"), bg="white", fg="black", bd=2, relief=RAISED)
        header.pack(fill=X)

        # Chat history area with scrollbar
        text_frame = Frame(main_frame)
        text_frame.pack(fill=BOTH, expand=True)
        self.scrollbar = Scrollbar(text_frame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.chat_text = Text(text_frame, wrap=WORD, yscrollcommand=self.scrollbar.set,
                              font=("Arial", 12), bd=2, relief=RAISED)
        self.chat_text.pack(fill=BOTH, expand=True)
        self.scrollbar.config(command=self.chat_text.yview)

        # Bottom frame for user input
        bottom_frame = Frame(self.root, bd=4, bg="powder blue")
        bottom_frame.pack(fill=X, padx=10, pady=10)
        Label(bottom_frame, text="Type your message:", font=("Arial", 14), bg="powder blue").grid(row=0, column=0)

        self.user_var = StringVar()
        self.user_entry = ttk.Entry(bottom_frame, textvariable=self.user_var,
                                     font=("Arial", 12), width=40)
        self.user_entry.grid(row=0, column=1, padx=5)
        self.user_entry.focus()

        send_btn = Button(bottom_frame, text="Send", command=self.send_message,
                          font=("Arial", 12, "bold"), bg="green", fg="white")
        send_btn.grid(row=0, column=2, padx=5)
        clear_btn = Button(bottom_frame, text="Clear", command=self.clear_chat,
                           font=("Arial", 12), bg="red", fg="white")
        clear_btn.grid(row=0, column=3, padx=5)

        # Status label
        self.status_label = Label(bottom_frame, text="", font=("Arial", 12), bg="powder blue", fg="red")
        self.status_label.grid(row=1, column=0, columnspan=4, pady=5)

    def on_enter(self, event=None):
        self.send_message()

    def clear_chat(self):
        self.chat_text.delete(1.0, END)
        self.user_entry.delete(0, END)
        self.status_label.config(text="")

    def send_message(self):
        user_msg = self.user_var.get().strip()
        if not user_msg:
            self.status_label.config(text="Please enter a message!")
            return
        self.status_label.config(text="")
        # Display user's message
        self.chat_text.insert(END, f"You: {user_msg}\n")
        self.chat_text.see(END)
        self.user_entry.delete(0, END)

        # Bot responses
        msg_lower = user_msg.lower()

        if msg_lower in ("hello", "hi", "hey"):
            response = "Hello! How can I help you today?"
        elif "how are you" in msg_lower:
            response = "I'm doing great! How can I assist you?"
        elif "your name" in msg_lower:
            response = "I'm your helpful assistant, a chatbot created by Dibbo."
        elif "your age" in msg_lower:
            response = "I'm a chatbot, so I don't age like humans do."
        elif "your purpose" in msg_lower:
            response = "I'm here to help you with your questions and problems."
        elif "thank you" in msg_lower:
            response = "You're welcome! If you need anything else, just ask."
        elif "bye" in msg_lower:
            response = "Goodbye! Have a wonderful day!"
        elif "need help" in msg_lower or "i need help" in msg_lower:
            response = "Sure! Please tell me what you need help with — like technical issues, homework, or general questions."
        elif "forgot my password" in msg_lower:
            response = "You can usually reset your password by clicking 'Forgot Password' on the login page. Need more help with that?"
        elif "can't open my file" in msg_lower:
            response = "Make sure the file type is supported by your software. You can also try opening it with a different program."
        elif "how to code" in msg_lower:
            response = "Start with a beginner-friendly language like Python. Websites like W3Schools, Codecademy, or freeCodeCamp can help you get started."
        elif "how to install python" in msg_lower:
            response = "Visit https://python.org, download the latest version, and run the installer. Let me know if you face issues."
        elif "how to use tkinter" in msg_lower:
            response = "Tkinter is Python's standard GUI library. You can start by importing it and creating a simple window. Want an example?"
        elif "how to create a database" in msg_lower:
            response = "You can create a database using tools like MySQL, SQLite, or PostgreSQL. For beginners, SQLite is simple and built-in with Python."
        elif "what is ai" in msg_lower:
            response = "AI stands for Artificial Intelligence. It's the simulation of human intelligence in machines that can learn and solve problems."
        elif "what is machine learning" in msg_lower:
            response = "Machine Learning is a subset of AI that enables systems to learn from data and improve without being explicitly programmed."
        elif "difference between ai and ml" in msg_lower:
            response = "AI is the broader concept of machines being able to carry out tasks smartly. ML is a subset of AI that involves learning from data."
        elif "how to make a website" in msg_lower:
            response = "You can build websites using HTML, CSS, and JavaScript. Frameworks like Django or Flask can help you do it with Python."
        elif "how to mark attendance" in msg_lower:
            response = "To mark attendance, go to the Face Recognition section, click 'FACE RECOGNITION,' and the system will automatically detect and log attendance using the webcam."
        elif "where is my attendance record" in msg_lower:
            response = "Your attendance record is in the 'Attendance Management System' section. Check the table on the right side for your details, or export the data as a CSV file."
        elif "system not detecting my face" in msg_lower:
            response = "Ensure your face is well-lit and centered in the webcam. Check if 'haarcascade_frontalface_default.xml' and 'classifier.xml' are in the correct directory. You may need to retrain the classifier with your images."
        elif "how to add a new student" in msg_lower:
            response = "To add a new student, you’ll need to update the MySQL database with their details and retrain the face recognition model. Add their info to the 'student' table and run the training script again."
        elif "error connecting to database" in msg_lower:
            response = "Check if your MySQL server is running and the credentials (host='localhost', user='root', password='246800', database='face_recognizer') are correct. Ensure the database 'face_recognizer' exists."
        elif "how to export attendance" in msg_lower:
            response = "Go to the 'Attendance Management System' section, click the 'Export CSV' button, and choose a location to save the attendance records as a CSV file."
        elif "how to reset the system" in msg_lower:
            response = "To reset the attendance data, go to the 'Attendance Management System' section and click the 'Reset' button. This will clear the input fields. Note: This won’t delete the saved CSV file."
        elif "why is confidence low" in msg_lower:
            response = "Low confidence in face recognition can be due to poor lighting, a partially visible face, or an untrained model. Ensure good lighting and retrain the classifier with more images if needed."
        elif "how to view student details" in msg_lower:
            response = "Student details are stored in the MySQL database. You can view them by accessing the 'student' table in the 'face_recognizer' database using a tool like phpMyAdmin or a SQL query."
        elif "system is slow" in msg_lower:
            response = "The system might be slow due to high webcam resolution or large database queries. Try lowering the webcam resolution in the code or optimizing the database by indexing the 'student' table."
        elif "how to train the model" in msg_lower:
            response = "To train the face recognition model, collect multiple images of each student, label them with their IDs, and use a script to train the LBPHFaceRecognizer. Save the trained model as 'classifier.xml'."
        elif "webcam not working" in msg_lower:
            response = "Ensure your webcam is connected and not in use by another app. Check the code to confirm it’s using the correct camera index (e.g., 'cv2.VideoCapture(0)'). Try using index 1 if 0 doesn’t work."
        elif "how to update attendance" in msg_lower:
            response = "In the 'Attendance Management System' section, select a record from the table, edit the details in the fields on the left, and click 'Update' to save the changes."
        elif "delete a student record" in msg_lower:
            response = "To delete a student, remove their entry from the 'student' table in the MySQL database and retrain the face recognition model to update the classifier."
        elif "how to import attendance" in msg_lower:
            response = "Go to the 'Attendance Management System' section, click 'Import CSV,' and select a CSV file with attendance data to load it into the table."
        else:
            response = "I'm not sure how to respond to that yet. Can you please ask something else or be more specific?"

        # Display bot's response
        self.chat_text.insert(END, f"Bot: {response}\n")
        self.chat_text.see(END)

if __name__ == "__main__":
    root = Tk()
    app = ChatbotApp(root)
    root.mainloop()