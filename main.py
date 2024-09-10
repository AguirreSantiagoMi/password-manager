from tkinter import *
import pandas

RED = '#d4483b'
BACKGROUND_COLOR = '#E78895'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
web_input = Entry(width=40, bg=BACKGROUND_COLOR)
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
pass_input = Entry(width=21, bg=RED)
pass_input.grid(column=1, row=3)
pass_generate_bt = Button(text='Generate Password', bg='white')
pass_generate_bt.grid(column=2, row=3)

add_bt = Button(text='Add', bg='white', width=33)
add_bt.grid(column=1, row=4, columnspan=2)



window.mainloop()