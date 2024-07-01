import tkinter
import mysql.connector  
from tkinter import *
from tkinter import messagebox
import pymysql
import subprocess
######################################################################


# Create the main window
window = tkinter.Tk()

# Get the screen width and height
screen_width =window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size
window_width = 600
window_height = 600

# Calculate the window position
window_x = int((screen_width - window_width) / 2)
window_y = int((screen_height - window_height) / 2)

# Set the window position and size
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")



###################################################################

#window=Tk()

#window.geometry("600x600")
window.title("login page")

def validate_input(text):
    return text == "" or text.isalpha()

validate_alpha = window.register(validate_input)

image1 = PhotoImage(file="C:/Users/LENOVO/Desktop/phython codes/10-bmw-png-image-download.png")

background_label = Label(window, image=image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

##########################################################

def open_frame2():

  #frame.destroy()

  frame2=tkinter.Frame(window,borderwidth=2, relief="solid",height=400,width=300)
  frame2.pack()

  frame2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
  frame2.pack_propagate(False)


  label1 = Label(frame2, text="Registation")
  label1.config(font=("Times New Roman", 40, "bold"),foreground ="red",justify="center")
  label1.pack()

  label2 = Label(frame2, text="User Name")
  label2.config(font=("Times New Roman", 15, "bold"))
  label2.pack()
  label2.place(x=10,y=80)

  

  Username1 = tkinter.Entry(frame2,borderwidth=2, relief="solid",validate="key", validatecommand=(validate_alpha, "%P")) 
  Username1.config(font=("Times New Roman", 15, "bold"),foreground ="blue")
  Username1.pack()
  Username1.place(x=70,y=110)
 

  label3 = Label(frame2, text="Enter A Password")
  label3.config(font=("Times New Roman", 15, "bold"))
  label3.pack()
  label3.place(x=10,y=140)

  Password1 = tkinter.Entry(frame2,borderwidth=2, relief="solid") 
  Password1.config(font=("Times New Roman", 15, "bold"),foreground ="blue",show="*")
  Password1.pack()
  Password1.place(x=70,y=170)
 

  label4 = Label(frame2, text="Re Type The Password")
  label4.config(font=("Times New Roman", 15, "bold"))
  label4.pack()
  label4.place(x=10,y=200)

  Password2 = tkinter.Entry(frame2,borderwidth=2, relief="solid") 
  Password2.config(font=("Times New Roman", 15, "bold"),foreground ="blue",show="*")
  Password2.pack()
  Password2.place(x=70,y=230)

  label5 = Label(frame2, text="Position")
  label5.config(font=("Times New Roman", 15, "bold"))
  label5.pack()
  label5.place(x=10,y=260)

  Position1 = tkinter.Entry(frame2,borderwidth=2, relief="solid",validate="key", validatecommand=(validate_alpha, "%P")) 
  Position1.config(font=("Times New Roman", 15, "bold"),foreground ="blue")
  Position1.pack()
  Position1.place(x=70,y=290)

  def dbconector():
   try:
    mydb = mysql.connector.connect(
     host="localhost",
     user="root",
     password="",
     database="project")

    cursor = mydb.cursor()
    quary="SELECT * FROM login WHERE user_name=%s AND password=%s"
    cursor.execute(quary,(Username1.get(),Password1.get()))
    results = cursor.fetchall()
   
    if results:
     messagebox.showinfo("Message", "alredy exites")
    elif (Password1.get()!=Password2.get()):
      messagebox.showinfo("Message", "passwords are not same")
    else:
     quary="INSERT INTO login(user_name, password, position,Status) VALUES (%s,%s,%s,%s)"
     cursor.execute(quary,(Username1.get(),Password1.get(),Position1.get(),0))
     #mydb.close()
     mydb.commit()
     messagebox.showinfo("Message", "requested")
     open_frame()
    mydb.close()
   except:
    messagebox.showinfo("Message", "database is not connected")
  entry_boxes=[Username1,Password1,Position1]
  for Entry in entry_boxes:
        Entry.delete(0, tkinter.END)
  

  button2 = Button(frame2, text="Register",command=dbconector)
  button2.config(font=("Times New Roman", 15, "bold"),foreground ="white",background="blue",justify="center")
  button2.pack()
  button2.place(x=55, y=350 )


  button2 = Button(frame2, text="Sign In",command=open_frame)
  button2.config(font=("Times New Roman", 15, "bold"),foreground ="white",background="green",justify="center")
  button2.pack()
  button2.place(x=155, y=350 )
  
 ######################################################################################################



 ##############################################################################################
def open_frame():

 frame=tkinter.Frame(window,borderwidth=2, relief="solid",height=400,width=300)
 frame.pack()

 frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

 frame.pack_propagate(False)


 label2 = Label(frame, text="Login")

 label2.config(font=("Times New Roman", 40, "bold"),foreground ="red",justify="center")

 label2.pack()


 label3 = Label(frame, text="User Name",height=3)
 label3.config(font=("Times New Roman", 10, "bold"))
 label3.pack()


 #creating a tex box

 username = tkinter.Entry(frame,validate="key", validatecommand=(validate_alpha, "%P")) 
 username.config(font=("Times New Roman", 10, "bold"))
 username.pack()
 

 label4 = Label(frame, text="Password",height=3)

 label4.config(font=("Times New Roman", 10, "bold"))

 label4.pack()


 #Creating a password box

 password = tkinter.Entry(frame,width=20, show="*")

 password.config(font=("Times New Roman", 10, "bold"))

 password.pack()

 
 def dbconector():
  try:
   mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="project")

   cursor = mydb.cursor()
   quary="SELECT * FROM login WHERE user_name=%s AND password=%s AND Status=1"
   cursor.execute(quary,(username.get(),password.get()))
   results = cursor.fetchall()
   mydb.close()
   if results:
    #print("compleate")
    messagebox.showinfo("Message", "login sucesses")
    ######################################
       # login_page.py

    import pickle

       # Create an array
    my_array = [username.get(),password.get()]

       # Save the array to a file
    with open('array_data.pickle', 'wb') as file:
     pickle.dump(my_array, file)

      ############################################
    subprocess.call(["python", "C:\\Users\\LENOVO\\Desktop\\phython codes\\dashboard.py"])
    window.destroy()
   else:
    messagebox.showinfo("Message", "login is not sucesses")
   
  except:
    messagebox.showinfo("Message", "database is not connected")
  
  

 button1 = Button(frame, text="sign in",command=dbconector)
 button1.config(font=("Times New Roman", 20, "bold"),foreground ="white",background="green",justify="center")
 button1.pack()


 label5 = Label(frame, text="If you don't have an account use sign up",height=3)
 label5.config(font=("Times New Roman", 10, "bold italic"))
 label5.pack()

 button2 = Button(frame, text="sign up",command=open_frame2)
 button2.config(font=("Times New Roman", 15, "bold"),foreground ="white",background="green",justify="center")
 button2.pack()


window.after(1000,open_frame)
window.mainloop()