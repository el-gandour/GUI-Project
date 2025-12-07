from tkinter import *

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(END, task)
        task_entry.delete(0, END)
    else:
        error_label.config(text="Please enter a task!")

# Function to delete selected task
def delete_task():
    try:
        selected_task = task_listbox.curselection()
        task_listbox.delete(selected_task)
        error_label.config(text="")
    except:
        error_label.config(text="Please select a task to delete!")

# Function to clear all tasks
def clear_all():
    task_listbox.delete(0, END)
    error_label.config(text="")

root = Tk()
root.title("To Do List")
root.geometry("500x500")

title_label = Label(root,text="To-Do List",font="Helvatica 10 bold",bg="white",fg="black")
title_label.pack(pady=20)

task_entry = Entry(root,width=30,font="Helvatica 10 bold")
task_entry.pack(pady=10)

add_button = Button(root,text="Add Task",font="Helvatica 10 bold",bg="green",fg="white",padx=20,pady=5,command=add_task)
add_button.pack(pady=5)

error_label = Label(root,text="",font="Helvatica 10 bold",bg="white",fg="red")
error_label.pack()

task_listbox = Listbox(root,width=40,height=10,font="Helvatica 10 bold",selectmode=SINGLE,bg="white",fg="black")
task_listbox.pack(pady=20)

delete_button = Button(root,text="Delete Task",font="Helvatica 10 bold",bg="red",fg="white",padx=15,pady=5,command=delete_task)
delete_button.pack(pady=5)

clear_button = Button(root,text="Clear All",font="Arial 11 bold",bg="gray",fg="white",padx=15,pady=5,command=clear_all)
clear_button.pack(pady=5)

root.mainloop()