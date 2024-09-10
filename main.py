from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

RED = '#F1EF99'
BACKGROUND_COLOR = '#FFE8C5'
BUTTON_COLOR = '#FFA27F'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    pass_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list += [choice(letters) for x in range(randint(8, 10))]
    password_list += [choice(symbols) for x in range(randint(2, 4))]
    password_list += [choice(numbers) for x in range(randint(2, 4))]
    shuffle(password_list)

    password = ''.join(password_list)
    pyperclip.copy(password)

    pass_input.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = web_input.get()
    user = user_input.get()
    password = pass_input.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Error', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are de data entered: \nEmail: {user} \nPassword: {password}')
        
        if is_ok:
            with open('passwords.txt', mode='a') as file:
                file.writelines(f'{website} | {user} | {password}\n')
            
            web_input.delete(0,'end')
            pass_input.delete(0,'end') 
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk(screenName='Password Manager')
window.title('Password manager')
window.config(bg=BACKGROUND_COLOR, padx=60, pady=50)

canvas = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

#Labels and inputs
web_label = Label(text='Website:', bg=BACKGROUND_COLOR)
web_label.grid(column=0, row=1)
web_input = Entry(width=40, bg=RED)
web_input.grid(column=1, row=1, columnspan=2)

web_input.focus()
#----
user_label = Label(text='Email/Username:', bg=BACKGROUND_COLOR)
user_label.grid(column=0, row=2)
user_input = Entry(width=40, bg=RED)
user_input.grid(column=1, row=2, columnspan=2)

user_input.insert(0, "elsantydetodos1@gmail.com")
#----
pass_label = Label(text='Password:', bg=BACKGROUND_COLOR)
pass_label.grid(column=0, row=3)
pass_input = Entry(width=21, bg=RED,)
pass_input.grid(column=1, row=3)
pass_generate_bt = Button(text='Generate Password', bg=BUTTON_COLOR, command=generate_password)
pass_generate_bt.grid(column=2, row=3)

add_bt = Button(text='Add', bg=BUTTON_COLOR, width=33, command=save_password)
add_bt.grid(column=1, row=4, columnspan=2)



window.mainloop()