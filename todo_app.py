####################  IMPORTS  #######################
from cgitb import text
from tkinter import *
from tkinter import ttk
from turtle import bgcolor
import customtkinter
from functions import *

##################  GUI CODE  ######################
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()
root.title("NOTE")
# root.config(bg='#0D2570')
root.resizable(width=False, height=False)

# Create the top frame
top_frame = customtkinter.CTkFrame(master=root,
                                width=200,
                                height=200,
                                corner_radius=10)
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")

# Create and set the intro text variable
intro_text = StringVar()
intro_text.set("Welcome! Let's be productive and see your progress.")

# Create and pack the message label
intro_label = customtkinter.CTkLabel(master=top_frame, 
                                textvariable=intro_text, 
                                width=120,
                                height=50,
                                fg_color=("#6B4101", "#EEAC4A"),
                                corner_radius=8)
intro_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Create the PhotoImage and label to hold it
neutral_image = PhotoImage(file="doit.png")

# Create and set the message text variable

image_label = ttk.Label(top_frame, image=neutral_image)
image_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

message_text = StringVar()
message_text.set("Think of things to do!")

# Create and pack the message label
message_label = customtkinter.CTkLabel(master=top_frame, 
                                textvariable=message_text,  
                                width=120,
                                height=25,
                                fg_color=("#6B4101", "#EEAC4A"),
                                corner_radius=8)
message_label.grid(row=2, column=0, columnspan=2, padx=10, pady=18)


# Create the bottom frame
bottom_frame = customtkinter.CTkFrame(master=root,
                                        width=200,
                                        height=100,
                                        corner_radius=10)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")

# note_text = StringVar()
# note_text.set("ADD NOTE: ")

# # Create a label for the task field and pack it into the GUI
# task_label = customtkinter.CTkLabel(master=bottom_frame,
#                                textvariable=note_text,
#                                width=100,
#                                height=25,
#                                fg_color=("#6B4101"),
#                                corner_radius=8)
# task_label.grid(row=5, column=0, padx=10, pady=3)

# Create an entry to type in task
task_entry = customtkinter.CTkEntry(master=bottom_frame,
                               placeholder_text="ADD TASK HERE",
                               width=250,
                               height=40,
                               border_width=2,
                               corner_radius=10)

task_entry.place(relx=0.5, rely=0.3, anchor=CENTER)
# Create a submit button
submit_button = customtkinter.CTkButton(master=bottom_frame,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Submit",
                                 command=lambda: add_action(task_entry, list_box, message_text))

submit_button.place(relx=0.5, rely=0.7, anchor=CENTER)

# Create the right frame
right_frame = customtkinter.CTkFrame(master=root,
                               width=200,
                               corner_radius=10)
right_frame.grid(row=0, column=1, rowspan=50, padx=10, pady=10, sticky="NSEW")

list_box = Listbox(
    right_frame,
    height=10,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#6B4101',
    activestyle="none",
)
list_box.grid(row=0, column=1, padx=10, pady=10, sticky="NSEW")


task_list = []

for item in task_list:
    list_box.insert('end', item)

scroll_bar = Scrollbar(right_frame)
scroll_bar.grid(row=0, column=2, sticky='NS')

list_box.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=list_box.yview)

# Create a remove button
remove_button = customtkinter.CTkButton(master=right_frame,
                                 width=120,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Remove",
                                 command=lambda: remove_action(list_box, message_text))

remove_button.place(relx=0.5, rely=0.92, anchor=CENTER)

# Run the mainloop

root.mainloop()