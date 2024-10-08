import os
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showinfo("Error", "You can't leave any fields empty!\nPlease enter your website and password.")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: {email} \nPassword: {password}\n"
                                                  f"Is it ok to save?")

    if is_ok:
        with open("passwords.txt", "a") as file:
            file.write(website + " | " + email + " | " + password + "\n")

            os.startfile("passwords.txt")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Helvetica", 10))
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:", font=("Helvetica", 10))
username_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Helvetica", 10))
password_label.grid(row=3, column=0)

website_entry = Entry(width=52)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ivangoranov14@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text='Generate Password', command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text='Add', width=44, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()