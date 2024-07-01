import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime
import pymysql
import mysql.connector 
import cv2
from cv2 import VideoCapture
from PIL import Image, ImageTk
import subprocess
########################################
import pickle
import keyboard
import os

save_directory = "C:/Users/LENOVO/Desktop/automatic-number-plate-recognition-python-master/data/"

# Load the array from the file
with open('array_data.pickle', 'rb') as file:
    my_array = pickle.load(file)


#######################################
window=Tk()
window.geometry("1530x830")

# Set the window title
window.title("dash board")

frame1=Frame(window,width=400, height=330,borderwidth=2, relief="solid")
frame1.pack()
frame1.place(x=1120,y=100)
frame1.pack_propagate(False)

label = tkinter.Label(frame1)
label.pack()


frame2=Frame(window,width=400, height=80,borderwidth=2, relief="solid")
frame2.pack()
frame2.place(x=1120,y=10)
frame2.pack_propagate(False)

title_label = tkinter.Label(window, text="Currunt Time")
title_label.pack()
title_label.place(x=1290,y=0)

title_label2 = tkinter.Label(window, text="camera 1")
title_label2.pack()
title_label2.place(x=1300,y=90)

###################################################################
cap = cv2.VideoCapture(0) #changing the camera 0 or 1

def show_frame():
    # Read the next video frame
    ret, frame = cap.read()

    if ret:
        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create a PIL Image from the video frame
        img = Image.fromarray(frame_rgb)

        # Create a PhotoImage object from the PIL Image
        photo = ImageTk.PhotoImage(img)

        # Update the image on the label
        label.config(image=photo)
        label.image = photo  # Store a reference to prevent garbage collection

        # Check if the Enter key is pressed
        if keyboard.is_pressed("enter"):
            # Construct the full file path for saving the image in the specified directory
            file_path = os.path.join(save_directory, "captured_image.png")

            # Save the captured frame as an image
            img.save(file_path)
            print(f"Image captured and saved as {file_path}")

            subprocess.call(["python", "C:/Users/LENOVO/Desktop/automatic-number-plate-recognition-python-master/yolov3-from-opencv-object-detection/main.py"])

    window.after(33, show_frame)

show_frame()

###################################################################

frame3=Frame(window,width=400, height=330,borderwidth=2, relief="solid")
frame3.pack()
frame3.place(x=1120,y=445)

title_label2 = tkinter.Label(window, text="camera 2")
title_label2.pack()
title_label2.place(x=1300,y=435)

frame4=Frame(window,width=1100, height=765,borderwidth=2, relief="solid")
frame4.pack()
frame4.place(x=10,y=10)
frame4.pack_propagate(False)


def update_time():
    current_time = datetime.now().strftime("%H:%M:%S")  # Get the current time
    time_label.config(text=current_time)  # Update the label text
    frame4.after(1000, update_time)  # Schedule the next update after 1 second

# Create a label for displaying the time
time_label = tkinter.Label(frame2, font=("Helvetica", 24))
time_label.pack(pady=20)

# Start updating the time
update_time()

table=ttk.Treeview(frame4,columns=('number_plate','date','in_time','out_time'),show='headings')
table.heading('number_plate',text='Number_Plate')
table.heading('date',text='Date')
table.heading('in_time',text='In_Time')
table.heading('out_time',text='Out_Time')
table.config(height=35)
table.pack()

try:
 mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project")
 cursor = mydb.cursor()
 quary="SELECT * FROM in_out"
 cursor.execute(quary)
 results = cursor.fetchall()
 for row in results:
    table.insert('', tkinter.END, text='', values=row)
 mydb.close()
except:
   messagebox.showinfo("Message", "database is not connected")

##############################################################
def manager_control():
   subprocess.call(["python", "C:\\Users\\LENOVO\\Desktop\\phython codes\\manager.py"])
################################################
try:
 mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project")
 cursor = mydb.cursor()
 quary="SELECT position FROM login WHERE user_name=%s AND password=%s"
 cursor.execute(quary,(my_array[0],my_array[1]))
 results = cursor.fetchall()
 for row in results:
    position=row[0]
    if (row[0]=='manager'):
      button = tkinter.Button(frame4, text="Manager Control unit",command=manager_control)
      button.config(font=("Times New Roman", 15, "bold"),foreground ="white",background="gray",justify="center")
      button.pack()
    else :
      print("not compleat")
 mydb.close()
except:
   messagebox.showinfo("Message", "database is not connected ++")
################################################################

  
window.mainloop()

cap.release()