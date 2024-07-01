import tkinter as tk
import mysql.connector  
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

window = Tk()
window.geometry("850x600")
window.title("Manager Control Unit")

label1 = tk.Label(window, text="Manager Control Unit")
label1.config(font=("Times New Roman", 15, "bold"))
label1.pack()

table = ttk.Treeview(window, columns=('UserName', 'Position', 'Status'), show='headings')
table.heading('UserName', text='UserName')
table.heading('Position', text='Position')
table.heading('Status', text='Status')

table.pack()
table.config(height=15)


def db():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="project")
        cursor = mydb.cursor()
        quary = "SELECT user_name,position,Status FROM login"
        cursor.execute(quary)
        results = cursor.fetchall()
        for row in results:
            table.insert('', tk.END, text='', values=row)
        mydb.close()
    except:
        messagebox.showinfo("Message", "Database is not connected")


db()


def row_selected(event):
    # Get the selected row
    selected_row = table.focus()

    # Get the values of the selected row
    values = table.item(selected_row)['values']

    # Display the name in the label
    name_label.config(text=values[0], font=("Times New Roman", 40, "bold"), foreground="red", justify="center")  

    print(values)

    def state():
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="project")
            cursor = mydb.cursor()
            query = "UPDATE `login` SET `Status`=%s WHERE `user_name`=%s AND `position`=%s"
            new_status = 1 - int(values[2])  # Toggle the status value between 0 and 1
            cursor.execute(query, (new_status, values[0], values[1]))
            mydb.commit()
            mydb.close()
            if new_status==0:
             messagebox.showinfo("Message", values[0]+" can't log now")
            elif new_status==1:
                messagebox.showinfo("Message", values[0]+" can log now")
            db()
        except:
            messagebox.showinfo("Message", "Database is not connected")

        # Clear the existing data in the treeview
        table.delete(*table.get_children())
        
        # Fetch the updated data from the database
        db()

    button.config(text="Status", font=("Times New Roman", 15, "bold"), foreground="white", background="gray", justify="center", command=state)


# Create a label to display the selected name
name_label = tk.Label(window, text='')
name_label.pack()

button = tk.Button(window, text="Select A Row")
button.config(font=("Times New Roman", 15, "bold"), foreground="white", background="gray", justify="center")
button.pack()

table.bind('<<TreeviewSelect>>', row_selected)

window.mainloop()
