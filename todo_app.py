####################  IMPORTS  #######################
from cgitb import text
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from turtle import bgcolor


##############  FUNCTIONS AND SETUP ###############

# Create the adding action function
def add_action():
    task = task_entry.get()
    if task != "":
        list_box.insert('end', task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
    message = random.choice(add_messages)
    message_text.set(message)

# Create the removing action function
def remove_action():
    list_box.delete('anchor')
    message = random.choice(remove_messages)
    message_text.set(message)

# Set up Lists
add_messages = ["Well done!", "You're very energitic!", "Awesome! It will feel great when you reach your goal"]
remove_messages = ["Good job!", "You're doing well", "You're being productive!"]

##################  GUI CODE  ######################
root = Tk()
root.title("NOTE")
root.config(bg='#0D2570')
root.resizable(width=False, height=False)

# Create the top frame
top_frame = LabelFrame(root, text="WHAT TO DO", bg='#fff', border=0)
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the intro text variable
intro_text = StringVar()
intro_text.set("Welcome! Let's be productive and see your progress.")

# Create and pack the message label
intro_label = Label(top_frame, textvariable=intro_text, wraplength=250, justify='center', bg='#fff')
intro_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="~/Desktop/doit.png")

# Create and set the message text variable

image_label = ttk.Label(top_frame, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

message_text = StringVar()
message_text.set("Think of things to do!")

# Create and pack the message label
message_label = ttk.Label(top_frame, textvariable=message_text, wraplength=250, justify='center')
message_label.grid(row=2, column=0, columnspan=2, padx=10, pady=18)


# Create the bottom frame
bottom_frame = LabelFrame(root, bg='#999090')
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# Create a label for the task field and pack it into the GUI
task_label = Label(bottom_frame, text="NOTE:", bg='#999090')
task_label.grid(row=5, column=0, padx=10, pady=3)

# Create a variable to store the task
task = StringVar()
task.set("")

# Create an entry to type in task
task_entry = ttk.Entry(bottom_frame, textvariable=task)
task_entry.grid(row=5, column=1, padx=10, pady=3, sticky="WE")

# Create a submit button
submit_button = Button(bottom_frame, text="Submit", command=add_action, border=0)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=10)

# Create the right frame
right_frame = ttk.LabelFrame(root, text="TASKS")
right_frame.grid(row=0, column=1, rowspan=50, padx=10, pady=10, sticky="NSEW")

list_box = Listbox(
    right_frame,
    height=10,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
)
list_box.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")


task_list = []

for item in task_list:
    list_box.insert('end', item)

scroll_bar = Scrollbar(right_frame)
scroll_bar.grid(row=0, column=2, sticky='NS')

list_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)


# Create a remove button
remove_button = ttk.Button(right_frame, text="Remove", command=remove_action)
remove_button.grid(row=6, column=1, columnspan=2, padx=10, pady=10)

# Run the mainloop

root.mainloop()