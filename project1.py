import tkinter
from tkinter import ttk
from tkinter import messagebox

def submit():
    
    accepted = accept_var.get()
    
    if accepted=="Accepted":
    
    
    
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            place = place_combobox.get()
            regist =reg_status.get()
            num = numspinbox.get()
            numm = numspibox.get()
  
            print("First name: ", firstname, "Last Name:", lastname)
            print("Title: ", title, "Age:", age, "place", place)
            print("Courses: ", num, "Semesters:", numm)
            print("Registration status: ", regist)
            print("---------------------------------------------------------------------------------------------------------------------------------------------")
        else:
             tkinter.messagebox.showwarning(title="Error", message="First Name and Last Name are required", )
    else:
        tkinter.messagebox.showwarning(title="Error", message="you are not accepted the terms", )


window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

user_info_frame =tkinter.LabelFrame(frame, text="user information")
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="first Name")
first_name_label.grid(row=0, column=0)
last_name_label =tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame,text="Gender")
title_combobox = ttk.Combobox(user_info_frame, values=["","Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox =tkinter.Spinbox(user_info_frame, from_=1, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

place = tkinter.Label(user_info_frame, text="Place")
place_combobox = tkinter.Entry(user_info_frame)
place.grid(row=2, column=1)
place_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

coursees_frame = tkinter.LabelFrame(frame)
coursees_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(coursees_frame, text="Registration Status")

registered_label.grid(row=0, column=0)


reg_status = tkinter.StringVar(value= "Not Registered")
registered_check = tkinter.Checkbutton(coursees_frame,text="Currently Registered", variable=reg_status, onvalue="Registered" , offvalue="Not Registered")
registered_check.grid(row=1, column=0)



numlabel = tkinter.Label(coursees_frame,text="Completed Courses")
numspinbox = tkinter.Spinbox(coursees_frame, from_=0, to='infinity')
numlabel.grid(row=0, column=1)
numspinbox.grid(row=1, column=1)


numsem = tkinter.Label(coursees_frame,text=" Semesters")
numspibox = ttk.Combobox(coursees_frame, values=["","1", "2", "3", "4", "5", "6", "7", "8", "9","10"])
numsem.grid(row=0, column=2)
numspibox.grid(row=1, column=2)


for widget in coursees_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
termlabel = tkinter.LabelFrame(frame,text="Term & Conditions")
termlabel.grid(row=2, column=0, sticky="news", padx=20, pady=20)

accept_var= tkinter.StringVar(value="Not Accepeted")
termchack= tkinter.Checkbutton(termlabel, text="I accept the terms and conditions.", variable=accept_var, onvalue="Accepted", offvalue="Not Accpeted")
termchack.grid(row=0, column=0)

button = tkinter.Button(frame, text="Submit", command= submit)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()