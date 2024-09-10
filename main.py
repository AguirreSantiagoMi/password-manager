from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

RED = '#F1EF99'
BACKGROUND_COLOR = '#FFE8C5'
BUTTON_COLOR = '#FFA27F'

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #
def find_password():
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title='Not Found', message="No Data File Found")
    else:
        website = web_input.get().capitalize()
        try:
            messagebox.showinfo(title=website, message=f'Web: {website}\nEmail: {data[website]['email']}\nPassword: {data[website]['password']}')
            data[website]
            pyperclip.copy(data[website]['password'])
        except KeyError:
            messagebox.showerror(title='Not Found', message="No details for the website exists")

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
    website = web_input.get().capitalize()
    user = user_input.get()
    password = pass_input.get()
    new_data = {
        website:{
            'email': user,
            'password': password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title='Error', message="Please don't leave any fields empty!")
    else:
        try:
            with open('passwords.json', mode='r') as file:
                #Reading old data
                data = json.load(file)  
                #Updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open('passwords.json', mode='w') as file:
                json.dump(new_data, file)      
        else:
            with open('passwords.json', mode='w') as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
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




#Labels
web_label = Label(text='Website:', bg=BACKGROUND_COLOR)
web_label.grid(column=0, row=1)

user_label = Label(text='Email/Username:', bg=BACKGROUND_COLOR)
user_label.grid(column=0, row=2)

pass_label = Label(text='Password:', bg=BACKGROUND_COLOR)
pass_label.grid(column=0, row=3)



#Inputs
web_input = Entry(width=21, bg=RED)
web_input.grid(column=1, row=1)
web_input.focus()

user_input = Entry(width=40, bg=RED)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "elsantydetodos1@gmail.com")

pass_input = Entry(width=21, bg=RED,)
pass_input.grid(column=1, row=3)



#Buttons
pass_generate_bt = Button(text='Generate Password', bg=BUTTON_COLOR, command=generate_password)
pass_generate_bt.grid(column=2, row=3, pady=5)

add_bt = Button(text='Add', bg=BUTTON_COLOR, width=33, command=save_password)
add_bt.grid(column=1, row=4, columnspan=2, pady=5)

search_bt = Button(text='Search', bg=BUTTON_COLOR, width=14, command=find_password)
search_bt.grid(column=2, row=1, pady=5)


window.mainloop()