import tkinter as tk
import ttkbootstrap as ttk 
from tkinter import messagebox
from numpy import random
uppercase_alphabets = [chr(i) for i in range(65,91)]
lowercase_alphabets = [chr(i) for i in range(97,123)]
num = [str(i) for i in range(10)]
special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
    '{', '}', '[', ']', '|',':', ';', '"', '<', '>', ',', 
    '.', '?', '/', '~'
]


def Generate():
    try:
        password = ''
        length_value = length.get()
        l = int(length_value)
        if not char_var.get():
            for i in range(l):
                password = password + random.choice(num)
        elif char_var.get() :
            if upper_var.get():
                lowercase_alphabets.extend(uppercase_alphabets)
            if special_var.get():
                lowercase_alphabets.extend(special_characters)  
            lowercase_alphabets.extend(num)
            for i in range(l):
                password += random.choice(lowercase_alphabets)
        return password_var.set(password)
    except:
        messagebox.showerror('Invalid input', 'Your need to enter a number!')
        




#intializing window
window = ttk.Window(themename='superhero')
window.title('Password Generator')
window.geometry('600x400')

#declaring variables
length = ttk.StringVar()
char_var = ttk.BooleanVar()
upper_var = ttk.BooleanVar()
special_var = ttk.BooleanVar()
password_var = ttk.StringVar()

#widgets
input_frame = ttk.Frame(master=window,padding=50)
button_frame = ttk.Frame(master=window)
label = ttk.Label(master=input_frame,text='Enter your password length')
length_entry = ttk.Entry(master=input_frame,justify='center',textvariable=length)
charbtn = ttk.Checkbutton(master=button_frame,text='Characters?',variable=char_var,padding=5)
upperbtn = ttk.Checkbutton(master=button_frame,text='Uppercase?',variable=upper_var,padding=5)
specialbtn = ttk.Checkbutton(master=button_frame,variable=special_var,text='Special Characters?',padding=5)
gen_button = ttk.Button(master=window,text="Generate",command=Generate,padding=10)
output_label = ttk.Label(master=window,text='Your Passcode',padding=10)
pass_label = ttk.Label(master=window,textvariable=password_var,padding=10)

#packing widgets
input_frame.pack()
label.pack()
length_entry.pack(side='left')
length_entry.focus()
charbtn.pack(side='left')
upperbtn.pack(side='left')
specialbtn.pack(side='left')
button_frame.pack()
gen_button.pack(pady=10)
output_label.pack()
pass_label.pack()

window.mainloop()