import face_recognition  # Library for face recognition
import cv2  # Library for computer vision tasks
import numpy as np  # Library for numerical operations
import csv  # Library for handling CSV files
from datetime import datetime  # Library for working with date and time
import tkinter as tk  # Library for creating GUI applications
from tkinter import messagebox  # Module for messagebox in Tkinter
from PIL import Image, ImageTk  # Libraries for handling images

# List to store known face encodings and their corresponding names
known_face_encodings = []
known_face_names = []

# Load and preprocess person1 image
person1_image = face_recognition.load_image_file("/home/User/Desktop/1.jpg")
person1_encoding = face_recognition.face_encodings(person1_image)[0]
known_face_encodings.append(person1_encoding)
known_face_names.append("Person 1")

# Load and preprocess person2 image
person2_image = face_recognition.load_image_file("/home/User/Desktop/2.jpg")
person2_encoding = face_recognition.face_encodings(person2_image)[0]
known_face_encodings.append(person2_encoding)
known_face_names.append("Person 2")

# Load and preprocess person3 image
person3_image = face_recognition.load_image_file("/home/User/Desktop/3.jpg")
person3_encoding = face_recognition.face_encodings(person3_image)[0]
known_face_encodings.append(person3_encoding)
known_face_names.append("Person 3")

# Load and preprocess person4 image
person4_image = face_recognition.load_image_file("/home/User/Desktop/4.jpg")
person4_encoding = face_recognition.face_encodings(person4_image)[0]
known_face_encodings.append(person4_encoding)
known_face_names.append("Person 4")

# Load and preprocess person5 image
person5_image = face_recognition.load_image_file("/home/User/Desktop/5.jpg")
person5_encoding = face_recognition.face_encodings(person5_image)[0]
known_face_encodings.append(person5_encoding)
known_face_names.append("Person 5")

# Load and preprocess person6 image
person6_image = face_recognition.load_image_file("/home/User/Desktop/6.jpg")
person6_encoding = face_recognition.face_encodings(person6_image)[0]
known_face_encodings.append(person6_encoding)
known_face_names.append("Person 6")

# Load and preprocess person7 image
person7_image = face_recognition.load_image_file("/home/User/Desktop/7.jpg")
person7_encoding = face_recognition.face_encodings(person7_image)[0]
known_face_encodings.append(person7_encoding)
known_face_names.append("Person 7")

# Load and preprocess person8 image
person8_image = face_recognition.load_image_file("/home/User/Desktop/8.jpg")
person8_encoding = face_recognition.face_encodings(person8_image)[0]
known_face_encodings.append(person8_encoding)
known_face_names.append("Person 8")

# Initialize the Tkinter window
root = tk.Tk()
root.title("Face Recognition Attendance System")

# Create a label to display the captured frame in the Tkinter window
label = tk.Label(root)
label.pack()

# Create an exit button to close the application
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack()

# Function to update the attendance record in a CSV file
def update_attendance(name):
    current_time = datetime.now().strftime("%H-%M-%S")  # Get the current time
    # Open a CSV file with the current date as the filename
    with open(datetime.now().strftime("%Y-%m-%d") + '.csv', 'a', newline='') as f:
        lnwriter = csv.writer(f)
        lnwriter.writerow([name, current_time])  # Write the name and current time to the file
    # Show a message box indicating that attendance has been recorded
    messagebox.showinfo("Attendance Recorded", f"{name}'s attendance recorded successfully!")

# Function to handle the face recognition process
def recognize_faces():
    ret, frame = video_capture.read()  # Capture a frame from the video source
    if not ret:  # Check if the frame was captured successfully
        print("Error: Failed to capture frame")
        return

    # Convert the frame from BGR to RGB (required by face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect face locations in the frame
    face_locations = face_recognition.face_locations(rgb_frame)

    # Encode faces found in the frame
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Iterate over each face found in the frame
    for face_encoding, face_location in zip(face_encodings, face_locations):
        # Compare face encoding with known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        
        name = "Unknown"  # Default name for unknown faces
        
        # If a match is found, update the name with the corresponding known face
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            # If the recognized face is in the list of students, update attendance
            if name in student:
                student.remove(name)  # Remove the student from the list to avoid duplicate entries
                update_attendance(name)  # Update attendance

        # Draw a rectangle around the face in the frame
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        # Draw the name of the recognized face below the rectangle
        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Convert the frame to RGB format for display
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert the frame to PIL Image format for Tkinter
    img = Image.fromarray(frame_rgb)
    imgtk = ImageTk.PhotoImage(image=img)

    # Update the label widget with the new image
    label.imgtk = imgtk
    label.configure(image=imgtk)

    # Set up the next recognition call after 100 milliseconds
    root.after(100, recognize_faces)

# Start video capture from the default camera (index 0)
video_capture = cv2.VideoCapture(0)

# Create a copy of known_face_names to keep track of students who haven't been marked
student = known_face_names.copy()

# Set up Tkinter main loop and start face recognition after 10 milliseconds
root.after(10, recognize_faces)
root.mainloop()
