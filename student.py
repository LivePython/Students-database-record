from tkinter import *
import tkinter as tk
from database import insert_data, search_student_by_id, display_all

root = Tk()

# Functions


def search(id):
    try:
        row = search_student_by_id(id)
    except Exception as a:
        print(a)
    else:
        display_search(row)


def display_search(data):
    list_box = Listbox(frame, width=20, height=1)
    list_box.grid(row=8, column=1)
    if data:
        list_box.insert(END, data)
    else:
        # If no data is found, display a message
        list_box.insert(END, "No student found with that ID")


def display_all_students():
    list_box_students = Listbox(frame, width=20, height=10)
    list_box_students.grid(row=11, column=1)
    all_data = display_all()
    if all_data:
        for item in all_data:
            list_box_students.insert(END, item)
    else:
        list_box_students.insert(END, "No students data in database")


# Creating a canvas
canvas = Canvas(root, width=900, height=600)
canvas.pack()

# Creating a frame object
frame = Frame()
frame.place(rely=0.1, relx=0.3, relwidth=0.8, relheight=0.8)


# Adding label object
label = Label(frame, text="Add Data")
label.grid(row=0, column=1)

# Adding label and their input
label_name = Label(frame, text="Name")
label_name.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

label_age = Label(frame, text="Age")
label_age.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

label_address = Label(frame, text="Address")
label_address.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button_add = Button(frame, text="Add Student",
                    command=lambda: insert_data(entry_name.get(),
                                              entry_age.get(),
                                              entry_address.get()))
button_add.grid(row=4, column=1)

label_search = Label(frame, text="Search by ID")
label_search.grid(row=6, column=1)

label_search_id = Label(frame, text="ID: ")
label_search_id.grid(row=7, column=0)

entry_search_id = Entry(frame)
entry_search_id.grid(row=7, column=1)

button_search_id = Button(frame, text="Find Student", command=lambda: search(entry_search_id.get()))

button_search_id.grid(row=7, column=2)

button_all_data = Button(frame, text="All Students", command=lambda: display_all_students())
button_all_data.grid(row=9, column=1)

root.mainloop()