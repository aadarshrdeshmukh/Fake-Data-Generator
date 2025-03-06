import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
from faker import Faker
import pyperclip

# Initialize Faker
fake = Faker()

# Function to generate fake data
def generate_data():
    name = fake.name()
    email = fake.email()
    name_data.set(f"Name: {name}")
    email_data.set(f"Email: {email}")

def copy_to_clipboard():
    combined_data = f"{name_data.get()}; {email_data.get()}"
    pyperclip.copy(combined_data)
    messagebox.showinfo("Copied", "Data copied to clipboard!")

def surprise_me():
    name_data.set(f"Surprise Name: {fake.first_name()}")

def export_json():
    file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
    if file_path:
        with open(file_path, "w") as file:
            json.dump({"name": name_data.get(), "email": email_data.get()}, file)
        messagebox.showinfo("Exported", "Data saved as JSON!")

# Function to switch themes
def switch_theme(theme):
    if theme == "Tech Blue":
        root.configure(bg="#0a192f")
        label.config(bg="#0a192f", fg="white")
        name_label.config(bg="#0a192f", fg="white")
        email_label.config(bg="#0a192f", fg="white")
        name_box.config(bg="#112240", fg="white", relief="ridge", highlightthickness=2, highlightbackground="#64ffda")
        email_box.config(bg="#112240", fg="white", relief="ridge", highlightthickness=2, highlightbackground="#64ffda")
        style.configure("TButton", background="#64ffda", foreground="#0a192f")
    elif theme == "Paper Theme":
        root.configure(bg="#f5f5dc")
        label.config(bg="#f5f5dc", fg="#5a3e36")
        name_label.config(bg="#f5f5dc", fg="white")
        email_label.config(bg="#f5f5dc", fg="white")
        name_box.config(bg="#fffaf0", fg="white", relief="ridge", highlightthickness=2, highlightbackground="#5a3e36")
        email_box.config(bg="#fffaf0", fg="white", relief="ridge", highlightthickness=2, highlightbackground="#5a3e36")
        style.configure("TButton", background="#5a3e36", foreground="#fffaf0")

# Create main window
root = tk.Tk()
root.title("Fake Data Generator")
root.geometry("500x500")
root.configure(bg="#2b2b2b")

name_data = tk.StringVar()
email_data = tk.StringVar()

# UI Elements
style = ttk.Style()
label = tk.Label(root, text="Fake Data Generator", font=("Arial", 18, "bold"), bg="#2b2b2b", fg="#64ffda")
label.pack(pady=10)

frame = tk.Frame(root, bg="#2b2b2b")
frame.pack(pady=10)

name_label = tk.Label(frame, text="Name:", bg="#2b2b2b", fg="black", font=("Arial", 12))
name_label.grid(row=0, column=0, padx=5)
name_box = tk.Entry(frame, textvariable=name_data, width=40, state="readonly", bg="#333", fg="white", relief="ridge", highlightthickness=2, highlightbackground="#64ffda")
name_box.grid(row=0, column=1, padx=5, pady=5)

email_label = tk.Label(frame, text="Email:", bg="#2b2b2b", fg="white", font=("Arial", 12))
email_label.grid(row=1, column=0, padx=5)
email_box = tk.Entry(frame, textvariable=email_data, width=40, state="readonly", bg="#333", fg="white", relief="ridge", highlightthickness=2, highlightbackground="#64ffda")
email_box.grid(row=1, column=1, padx=5, pady=5)

# Buttons
generate_button = ttk.Button(root, text="Generate Data", command=generate_data)
generate_button.pack(pady=2)

copy_button = ttk.Button(root, text="Copy", command=copy_to_clipboard)
copy_button.pack(pady=2)

surprise_button = ttk.Button(root, text="Surprise Me!", command=surprise_me)
surprise_button.pack(pady=2)

export_button = ttk.Button(root, text="Export as JSON", command=export_json)
export_button.pack(pady=2)

# Theme switcher
theme_var = tk.StringVar(value="Tech Blue")
theme_menu = ttk.Combobox(root, textvariable=theme_var, values=["Tech Blue", "Paper Theme"], state="readonly")
theme_menu.pack(pady=5)
theme_menu.bind("<<ComboboxSelected>>", lambda event: switch_theme(theme_var.get()))

switch_theme("Tech Blue")  # Set default theme

# Run main loop
root.mainloop()