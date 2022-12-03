##############  FUNCTIONS AND SETUP ###############
from tkinter import messagebox
import random

# Create the adding action function
def add_action(task_entry, list_box, message_text):
    task = task_entry.get()
    if task != "":
        list_box.insert('end', task)
        task_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
    message = random.choice(add_messages)
    message_text.set(message)

# Create the removing action function
def remove_action(list_box, message_text):
    list_box.delete('anchor')
    message = random.choice(remove_messages)
    message_text.set(message)

# Set up Lists
add_messages = ["Well done!", "You're very energitic!", "Awesome! It will feel great when you reach your goal"]
remove_messages = ["Good job!", "You're doing well", "You're being productive!"]
