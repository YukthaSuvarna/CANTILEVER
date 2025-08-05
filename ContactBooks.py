import tkinter as tk
from tkinter import messagebox


def add_contact(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"{name},{phone}\n")


def view_contacts():
    try:
        with open("contacts.txt", "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def delete_contact(name):
    contacts = view_contacts()
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            if not contact.strip().startswith(name + ","):
                file.write(contact)


def edit_contact(name, new_phone):
    contacts = view_contacts()
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            if contact.strip().startswith(name + ","):
                file.write(f"{name},{new_phone}\n")
            else:
                file.write(contact)


def add():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    if name and phone:
        add_contact(name, phone)
        messagebox.showinfo("Success", "Contact Added")
        reset_fields()
        view()
    else:
        messagebox.showwarning("Input Error", "Both fields are required")


def view():
    contact_list.delete(0, tk.END)
    contacts = view_contacts()
    for contact in contacts:
        contact_list.insert(tk.END, contact.strip())


def delete():
    name = name_var.get().strip()
    if name:
        delete_contact(name)
        messagebox.showinfo("Success", "Contact Deleted")
        reset_fields()
        view()
    else:
        messagebox.showwarning("Input Error", "Enter Name to Delete")


def edit():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    if name and phone:
        edit_contact(name, phone)
        messagebox.showinfo("Success", "Contact Updated")
        reset_fields()
        view()
    else:
        messagebox.showwarning("Input Error", "Both fields are required for Edit")


def reset_fields():
    name_var.set("")
    phone_var.set("")


def exit_app():
    root.destroy()


root = tk.Tk()
root.title("Contact Book")
root.geometry("400x400")

name_var = tk.StringVar()
phone_var = tk.StringVar()

tk.Label(root, text="Name").pack(pady=5)
tk.Entry(root, textvariable=name_var).pack(pady=5)

tk.Label(root, text="Contact No.").pack(pady=5)
tk.Entry(root, textvariable=phone_var).pack(pady=5)

tk.Button(root, text="ADD", command=add, width=15, bg="lightblue").pack(pady=5)
tk.Button(root, text="EDIT", command=edit, width=15, bg="lightpink").pack(pady=5)
tk.Button(root, text="DELETE", command=delete, width=15, bg="lavender").pack(pady=5)
tk.Button(root, text="VIEW", command=view, width=15, bg="lightblue").pack(pady=5)
tk.Button(root, text="RESET", command=reset_fields, width=15, bg="lightpink").pack(pady=5)
tk.Button(root, text="EXIT", command=exit_app, width=15, bg="lavender").pack(pady=5)

contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=10)

root.mainloop()
