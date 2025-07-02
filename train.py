from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 
import os
import cv2
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("front.ico")
        
        # Title Label
        title_lbl = Label(self.root,text="TRAIN DATA SET",font=("times new roman", 35, "bold"),bg="BLACK",fg="red",)
        title_lbl.place(x=0, y=0, width=1530, height=45)
        
        # Top Image
        img_top = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\fa.jpg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        
        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=325)
        
        # Button for Training
        b1_1 = Button( self.root,text="TRAIN DATA",cursor="hand2",font=("times new roman", 30, "bold"),bg="darkblue",fg="white",command=self.train_classifier,)
        b1_1.place(x=0, y=380, width=1530, height=60)
        
        # Bottom Image
        img_bottom = Image.open(r"C:\Users\Dibbo\OneDrive\Documents\Desktop\face_recconice_system\photos\fa.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        
        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=0, y=440, width=1530, height=325)
        
        # Progress Bar
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=100, mode="indeterminate")
        self.progress.place(x=0, y=750, width=1530, height=20)

    def train_classifier(self):
        data_dir = "data"
        
        # Check if the directory exists
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", "Data directory not found!")
            return
        
        # List all image paths
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.png', '.jpg', '.jpeg'))]
        
        if len(path) == 0:
            messagebox.showerror("Error", "No images found in the data directory!")
            return
        
        faces = []
        ids = []
        
        # Start the progress bar
        self.progress.start()
        
        for image in path:
            try:
                img = Image.open(image).convert('L')  # Convert to grayscale
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from the filename
                
                faces.append(imageNp)
                ids.append(id)
            except Exception as e:
                print(f"Error processing {image}: {e}")
                continue
        
        # Check if we have valid data
        if len(faces) == 0:
            messagebox.showerror("Error", "No valid images for training!")
            self.progress.stop()
            return
        
        ids = np.array(ids)
        
        # Train the classifier and save it
        try:
            clf = cv2.face.LBPHFaceRecognizer_create()  # Requires opencv-contrib-python
            clf.train(faces, ids)
            clf.write("classifier.xml")
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {e}")
            self.progress.stop()
            return
        
        self.progress.stop()  # Stop the progress bar
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed!")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
