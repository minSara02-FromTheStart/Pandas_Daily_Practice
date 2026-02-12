import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import os


contacts = pd.DataFrame(columns=["ID", "Name", "Number", "Email"])
file_name = "contact.csv"


def load_contact():
    global contacts
    if os.path.exists(file_name):
        contacts = pd.read_csv(file_name)
        messagebox.showinfo("Info", "Contacts loaded successfully!")
    else:
        messagebox.showwarning("Warning", "No contact file found. Starting fresh.")

def save_contact():
    global contacts
    contacts.to_csv(file_name, index=False)
    messagebox.showinfo("Info", "Contacts saved successfully!")

def add_contact_gui():
    global contacts
    try:
        new_contact = {
            "ID": int(id_entry.get()),
            "Name": name_entry.get(),
            "Number": number_entry.get(),
            "Email": email_entry.get()
        }
    except ValueError:
        messagebox.showerror("Error", "ID must be an integer")
        return

    # Check for duplicate ID
    if new_contact["ID"] in contacts["ID"].values:
        messagebox.showerror("Error", "ID already exists")
        return

    contacts.loc[len(contacts)] = new_contact
    save_contact()
    clear_entries()
    messagebox.showinfo("Success", "Contact added!")

def view_contact_gui():
    for row in tree.get_children():
        tree.delete(row)
    for _, row in contacts.iterrows():
        tree.insert("", tk.END, values=list(row))

def delete_contact_gui():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Warning", "Select a contact to delete")
        return
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete?")
    if confirm:
        index = tree.index(selected_item)
        contacts.drop(index, inplace=True)
        contacts.reset_index(drop=True, inplace=True)
        save_contact()
        view_contact_gui()

def clear_entries():
    id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Contact Book")
root.geometry("600x500")


tk.Label(root, text="ID").grid(row=0, column=0, padx=5, pady=5, sticky="w")
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Name").grid(row=1, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Number").grid(row=2, column=0, padx=5, pady=5, sticky="w")
number_entry = tk.Entry(root)
number_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Email").grid(row=3, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1, padx=5, pady=5)


tk.Button(root, text="Add Contact", command=add_contact_gui).grid(row=4, column=0, padx=5, pady=5)
tk.Button(root, text="View Contacts", command=view_contact_gui).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact_gui).grid(row=4, column=2, padx=5, pady=5)
tk.Button(root, text="Load Contacts", command=load_contact).grid(row=0, column=2, padx=5, pady=5)
tk.Button(root, text="Clear Entries", command=clear_entries).grid(row=4, column=3, padx=5, pady=5)


columns = ("ID", "Name", "Number", "Email")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)
tree.grid(row=5, column=0, columnspan=4, padx=5, pady=10)


root.mainloop()
