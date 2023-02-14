import tkinter
from tkinter import ttk
from tkinter import messagebox


def enter_data():
    accepted = correct_var.get()
    if accepted == "Accepted":
        # User info
        SerialNumber = Serial_Number_entry.get()
        DefaltPassword = Serial_Number_entry.get()
        RecoveryPassword = Recovery_Password_entry.get()
        VoltNumber = Volt_Number_label_entry.get()

        if SerialNumber and DefaltPassword:
            VoltNumber = Volt_Number_label_entry.get()
            print("Serial Number: ", SerialNumber,)
            print("DefaltPassword: ", DefaltPassword)
            print("Recovery Password: ", RecoveryPassword,)
            print("Volt Number: ", VoltNumber)
        else:
            tkinter.messagebox.showwarning(
                title="Error", message="Serial Number and Defalt Password are required.")
    else:
        tkinter.messagebox.showwarning(
            title="Error", message="Have You check the Data ")

## for scannig QR code
# taking three inputs at a time


var_1, var_2, var_3 = input(
    "Enter three values: ").split()
print("serial Num: ", var_1)
print("Defalult Pass : ", var_2)
print("Recovery Code : ", var_3)
print()


window = tkinter.Tk()
window.title("Charging Station Data Entry Form")

frame = tkinter.Frame(window, width=250, height=150, background="#34A2FE")
frame.grid(rowspan=20, columnspan=5, padx=20, pady=10)
frame.pack()

filename_label = tkinter.Label(frame, text="Data received form scanner")
filename_label.grid(sticky='news', padx=20, pady=10)


# Text Fram for retrieving Tex from scanner in form of variable
scann_output_file_text = tkinter.Text(frame)
scann_output_file_text.grid(sticky='news', padx=20, pady=10)
# txt field name space
# scann_output_file_text_Entry1 = tkinter.Entry(frame)
# scann_output_file_text_Entry2 = tkinter.Entry(frame)
# scann_output_file_text_Entry3 = tkinter.Entry(frame)
# #-------
# var_1 = scann_output_file_text_Entry1 = tkinter.Entry(frame)
# var_2 = scann_output_file_text_Entry2 = tkinter.Entry(frame)
# var_3 = scann_output_file_text_Entry3 = tkinter.Entry(frame)


def func_1():
    global var_1
    var_1 = scann_output_file_text_Entry1.get()


def func_2():
    global var_2
    var_2 = scann_output_file_text_Entry2.get()


def func_3():
    global var_3
    var_3 = scann_output_file_text_Entry3.get()


def store_all():
    func_1()
    func_2()
    func_3()
    print(var_1)
    print(var_2)
    print(var_3)


#b = tkinter.Button(frame, text="get", width=10, )



#-----
# Button for into charging station inforamtion
open_scannfile_button = tkinter.Button(
    frame, text="send scann data", command = store_all)  # , command=openFile)
open_scannfile_button.grid()

# Saving User Info
user_info_frame = tkinter.LabelFrame(
    frame, text="Charging station Information")        # hier can this box will brough below with --row=2
user_info_frame.grid(row=0, rowspan=2, column=2,  padx=20, pady=10)

# for serial number
Serial_Number_label = tkinter.Label(user_info_frame, text="Serial Number")
Serial_Number_label.grid(row=0, column=0)
var_1 = Serial_Number_entry = tkinter.Entry(user_info_frame, width=25)
Serial_Number_entry.grid(row=1, column=0)


Defalt_Password_label = tkinter.Label(user_info_frame, text="Default Password")
Defalt_Password_label.grid(row=2, column=0)
var_2 = Defalt_Password_entry = tkinter.Entry(user_info_frame, width=25)
Defalt_Password_entry.grid(row=3, column=0)


Recovery_Password_label = tkinter.Label(user_info_frame, text="Recovery Password")
Recovery_Password_label.grid(row=4, column=0)
var_3 = Recovery_Password_entry = tkinter.Entry(user_info_frame, width=25)
Recovery_Password_entry.grid(row=5, column=0)

Volt_Number_label = tkinter.Label(user_info_frame, text="Enter Volt Number")
Volt_Number_label.grid(row=6, column=0)
Volt_Number_label_entry = tkinter.Entry(user_info_frame)
Volt_Number_label_entry.grid(row=7, column=0, padx=20, pady=10)

# Check wether the Data is correct or not
check_frame = tkinter.LabelFrame(frame, text="confirmation")
check_frame.grid(sticky='news', row=7, column=0, padx=20, pady=15)

correct_var = tkinter.StringVar(value="Find correct")
check_data = tkinter.Checkbutton(check_frame, text="I read and check the data is correcct.",
                                 variable=correct_var, onvalue="Accepted", offvalue="Not Accepted")
check_data.grid(row=0, column=0)

# correct_var = tkinter.StringVar(value="Find correct")

# Button
button = tkinter.Button(frame, text="Enter data", command=enter_data)
button.grid()
window.mainloop()
