from tkinter import *
import random
import json
from tkinter import messagebox

window = Tk()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def passwordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    entry3.delete(0, 'end')
    entry3.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def savePassword():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
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
            entry1.delete(0, END)
            entry3.delete(0, END)
            entry1.focus()

# ---------------------------- FIND WEBSITE ------------------------------- #


def find_website():
    website = entry1.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #


window.title("Password manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
label1 = Label(text="Website:")
label2 = Label(text="Email/Username:")
label3 = Label(text="Password:")
button1 = Button(text="Generate Password", command=passwordGenerator)
button2 = Button(text="Add", width=36, command=savePassword)
find_website_button = Button(text="Find", command=find_website)
entry1 = Entry(width=35)
entry1.focus()
entry2 = Entry(width=35)
entry2.insert(0, "ranjananubhav7@gmail.com")
entry3 = Entry(width=21)
label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=3, column=0)
entry1.grid(row=1, column=1)
find_website_button.grid(row=1, column=2)
entry2.grid(row=2, column=1, columnspan=2)
entry3.grid(row=3, column=1)
button1.grid(row=3, column=2)
button2.grid(row=4, column=1, columnspan=2)
canvas.grid(row=0, column=1)

window.mainloop()
