from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import pyperclip
import json


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title=website.capitalize(), message=f"Username: {username}\n\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} website")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K",
               "k",
               "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", 't', "U", "u", "V",
               "v",
               "W", "w", "X", "x", "Y", "y", "Z", "z"]

    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    generated_password = password_letters + password_symbols + password_numbers
    shuffle(generated_password)
    password_str = "".join(generated_password)

    password_entry.insert(0, password_str)
    pyperclip.copy(password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().lower()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered:"
                                                              f"\n\n\nEmail: {username}"
                                                              f"\nPassword: {password}\n\n\nPress ok to save")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=29)
website_entry.focus()
website_entry.grid(row=1, column=1)

search_button = Button(text="Search", width=13, highlightthickness=0, command=search_password)
search_button.grid(row=1, column=2)

username_entry = Entry(width=49)
username_entry.insert(0, "dhruvrakhra2204@gmail.com")
username_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=29)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=40, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
