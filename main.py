from tkinter import *
from tkinter import messagebox
from pyperclip import copy
import json

from password_generator import RandomPassword

WHITE = "#FFFFFF"
BLACK = "#000000"

window = Tk()
window.minsize(200, 200)
window.title("Rephy's Password Keeper - by Raphael Manayon")
window.config(padx=20, pady=20, bg=WHITE)

website = StringVar()
user = StringVar()
password = StringVar()

def add_password():
        if (website.get().strip() != "") and (user.get().strip() != "") and (password.get().strip() != ""):
                confirmed = messagebox.askokcancel(title="Password Confirmation", message=f"These are your password details:\nWebsite: {website.get().strip()}\nUsername: {user.get().strip()}\nPassword: {password.get().strip()}\n\nProceed to save password?")
                if confirmed:
                        try:
                                file = open("passwords.json", "r")
                        except FileNotFoundError:
                                file = open("passwords.json", "w")
                                blank_json = {

                                }
                                json.dump(blank_json, file, indent=4)

                        with open("passwords.json", "r") as file:
                                new_data = {
                                        website.get(): {
                                                "user/email": user.get(),
                                                "password": password.get()
                                        }
                                }

                                data = json.load(file)
                                data.update(new_data)

                        with open("passwords.json", "w") as file:
                                json.dump(data, file, indent=4)

                        website.set("")
                        user.set("")
                        password.set("")
        else:
                messagebox.showerror(title="Invalid Fields", message="You cannot leave any entry fields blank!")

def generate_password():
        random_password = RandomPassword().password
        password.set(random_password)

        copy_pw = messagebox.askyesno(title="Copy Generated Password", message=f"Your password is {random_password}.\n\nWould you like to copy the result to your clipboard?")
        if copy_pw:
                copy(random_password)

def search_password():
        try:
                file = open("passwords.json", "r")
        except FileNotFoundError:
                file = open("passwords.json", "w")
                blank_json = {

                }
                json.dump(blank_json, file, indent=4)
                messagebox.showinfo(title="No Passwords Saved", message="There are no passwords saved in your data file!")
        else:
                websites = [web for (web, val) in json.load(file).items()]

                if website.get().strip() == "":
                        messagebox.showinfo(title="Websites Saved", message=f"Websites: {websites}")

                        return
                try:
                        data = json.load(file)

                        info = f"Your information for {website.get()}:\n\nUser/Email: {data[website.get()]['user/email']}\nPassword: {data[website.get()]['password']}"

                        messagebox.showinfo(title=f"{website.get()} Info".title(), message=info)
                except KeyError:
                        messagebox.showinfo(title="No Password Saved", message=f"You do not have any passwords for {website.get()}!")

canvas = Canvas(width=200, height=200, highlightthickness=0, bg=WHITE)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0, pady=3)

website_label = Label(text="Website", bg=WHITE, fg=BLACK)
website_label.grid(column=0, row=1, pady=3)

website_entry = Entry(textvariable=website, width=21, bg=WHITE, fg=BLACK, highlightthickness=0)
website_entry.grid(column=1, row=1, pady=3)

search_button = Button(width=10, text="Search", bg=WHITE, fg=BLACK, highlightbackground=WHITE, command=search_password)
search_button.grid(column=2, row=1, pady=3)

user_label = Label(text="Username/Email", bg=WHITE, fg=BLACK)
user_label.grid(column=0, row=2, pady=3)

user_entry = Entry(textvariable=user, width=35, bg=WHITE, fg=BLACK, highlightthickness=0)
user_entry.grid(column=1, row=2, columnspan=2, pady=3)

password_label = Label(text="Password", bg=WHITE, fg=BLACK)
password_label.grid(column=0, row=3, pady=3)

password_entry = Entry(textvariable=password, width=21, bg=WHITE, fg=BLACK, highlightthickness=0)
password_entry.grid(column=1, row=3, pady=3)

generate_password_button = Button(width=10, text="Generate Password", bg=WHITE, fg=BLACK, highlightbackground=WHITE, command=generate_password)
generate_password_button.grid(column=2, row=3, pady=3)

add_password_button = Button(width=33, text="Add", bg=WHITE, fg=BLACK, highlightbackground=WHITE, command=add_password)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()