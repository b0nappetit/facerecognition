import tkinter as tk
from tkinter import filedialog
import cv2
import numpy as np

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition App")

        self.image_label1 = tk.Label(root, text="Image 1:")
        self.image_label1.pack(pady=10)

        self.image_label2 = tk.Label(root, text="Image 2:")
        self.image_label2.pack(pady=10)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

        self.browse_button1 = tk.Button(root, text="Browse Image 1", command=self.browse_image1)
        self.browse_button1.pack()

        self.browse_button2 = tk.Button(root, text="Browse Image 2", command=self.browse_image2)
        self.browse_button2.pack()

        self.compare_button = tk.Button(root, text="Compare Faces", command=self.compare_faces)
        self.compare_button.pack()

    def browse_image1(self):
        file_path = filedialog.askopenfilename(title="Select Image 1", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.image_label1.config(text=f"Image 1: {file_path}")
        self.image_path1 = file_path

    def browse_image2(self):
        file_path = filedialog.askopenfilename(title="Select Image 2", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.image_label2.config(text=f"Image 2: {file_path}")
        self.image_path2 = file_path

    def compare_faces(self):
        try:
            image1 = cv2.imread(self.image_path1)
            image2 = cv2.imread(self.image_path2)

            # Convert images to grayscale
            gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
            gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

            # Use OpenCV's face detection
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces1 = face_cascade.detectMultiScale(gray_image1, scaleFactor=1.3, minNeighbors=5)
            faces2 = face_cascade.detectMultiScale(gray_image2, scaleFactor=1.3, minNeighbors=5)

            # Check if faces are found in both images
            if len(faces1) > 0 and len(faces2) > 0:
                self.result_label.config(text="Faces found!")

                # You can add additional logic here to compare face features using OpenCV or other methods.

            else:
                self.result_label.config(text="Faces not found.")
        except Exception as e:
            self.result_label.config(text=f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
