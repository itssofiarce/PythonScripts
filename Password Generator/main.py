from tkinter import *
from tkinter import messagebox
import pasgenerator
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def get_strong_password():
    stronger = pasgenerator.generate_pass()
    password_name.insert(0, stronger)
    # pyperclick.copy(password_name) to copy the password directly once it was created
# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_empty():
    if len(website_name.get()) == 0 or len(user_name.get()) == 0 or len(password_name.get()) == 0:
        messagebox.showwarning(title="Empty fields",
                               message="Do not leave empty entries")
    else:
        save_password()


def save_password():
    new_data = {
        website_name.get(): {
            "email": user_name.get(),
            "password": password_name.get()
        }
    }
    is_ok = messagebox.askyesno(
        title=f"{website_name.get()}", message=f"These are the details entered:\n Name:{user_name.get()}\n Password: {password_name.get()} \n Is it ok to save? ")
    if is_ok:
        try:
            with open("data.json", "r") as data:
                data_dict = json.load(data)
                data_dict.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            with open("data.json", "w") as data:
                json.dump(data_dict, data, indent=4)
        finally:
            password_name.delete(0, 'end')
            website_name.delete(0, 'end')

# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search():
    searched_web = website_name.get()
    try:
        with open("data.json", "r") as data:
            data_web = json.load(data)
            print(data_web)
            searched_data = data_web[searched_web]
    except FileNotFoundError:
        messagebox.showerror(
            message="There is no file created", title="File error")
    except KeyError:
        messagebox.showerror(
            message=f"There is no data for {searched_web}", title="Data error")
    else:
        mail = searched_data['email']
        password = searched_data['password']
        messagebox.showinfo(
            message=f"The data for {searched_web} is: \n Email: {mail}\n\n Password: {password}", title="Data found")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()

window.title("Password Manager")
window.config(padx=50, pady=50)

#-Grid layout- Row 0#
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)
#-Grid layout- Row 1#
website = Label(text="Website")
website.grid(column=0, row=1)
website.focus

website_name = Entry(width=26)
website_name.grid(column=1, row=1)

website_search = Button(text="Search", borderwidth=0, padx=0, command=search)
website_search.grid(column=2, row=1)


#-Grid layout- Row 2#
user = Label(text="Username/Email")
user.grid(column=0, row=2)

user_name = Entry(width=35)
user_name.grid(column=1, columnspan=2, row=2)
#-Grid layout- Row 3#
password = Label(text="Password")
password.grid(column=0, row=3)

password_name = Entry(width=26)
password_name.grid(column=1, row=3)

generator = Button(text="Generate", borderwidth=0, padx=0,
                   command=get_strong_password)
generator.grid(column=2, row=3)

#-Grid layout- Row 4#
add = Button(text="Add Password", width=30,
             borderwidth=0, command=check_empty)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()
