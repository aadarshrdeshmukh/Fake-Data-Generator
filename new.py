import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import json
import random
from faker import Faker

# Initialize Faker with multiple locales for variety
fake = Faker(['en_US', 'en_GB', 'en_IN'])

# Create the main application window
root = tk.Tk()
root.title("✨ Fancy Fake Data Generator")
root.geometry("600x700")

# Theme settings
themes = {
    "Tech Blue": {
        "bg": "#0A192F",
        "fg": "#64FFDA",
        "btn": "#112D4E",
        "btn_hover": "#1A365D",
        "font": ("Arial", 11)
    },
    "Paper Theme": {
        "bg": "#F5E6C8",
        "fg": "#4A3F35",
        "btn": "#D4A373",
        "btn_hover": "#E7B784",
        "font": ("Comic Sans MS", 11)
    }
}
current_theme = "Tech Blue"

# Fun name prefixes and suffixes for "Surprise Me!"
fun_prefixes = ["Super", "Mega", "Ultra", "Quantum", "Cosmic"]
fun_suffixes = ["Master", "Ninja", "Guru", "Wizard", "Champion"]


def apply_theme():
    """Apply the selected theme to all elements properly."""
    theme = themes[current_theme]
    root.config(bg=theme["bg"])

    # Configure ttk styles
    style = ttk.Style()
    style.configure("TButton", font=theme["font"], padding=5)
    style.configure("TLabel", font=theme["font"], background=theme["bg"], foreground=theme["fg"])
    style.configure("TCombobox", fieldbackground=theme["bg"], foreground=theme["fg"])

    for widget in root.winfo_children():
        if isinstance(widget, tk.Frame):
            widget.config(bg=theme["bg"])
        elif isinstance(widget, tk.Label):
            widget.config(bg=theme["bg"], fg=theme["fg"], font=theme["font"])
        elif isinstance(widget, tk.Button):
            widget.config(bg=theme["btn"], fg=theme["fg"],
                          activebackground=theme["btn_hover"], activeforeground=theme["fg"])
            widget.bind("<Enter>", lambda e, btn=widget: btn.config(bg=theme["btn_hover"]))
            widget.bind("<Leave>", lambda e, btn=widget: btn.config(bg=theme["btn"]))

    # Ensure result label follows the theme
    result_label.config(bg=theme["bg"], fg=theme["fg"])

    # Apply the theme to the combobox
    theme_selector.config(style="TCombobox")


def generate_fun_name():
    """Generate a fun fake name."""
    prefix = random.choice(fun_prefixes)
    base_name = fake.name()
    suffix = random.choice(fun_suffixes)
    return f"{prefix} {base_name} the {suffix}"


def generate_fake_data():
    """Generate normal fake data with a matching email."""
    actual_name = fake.name()

    # Generate an email using the real name
    first_name, last_name = actual_name.split()[:2]  # Take only first and last name
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    address = fake.address().replace("\n", ", ")
    phone = fake.phone_number()

    result_var.set(f"👤 Name: {actual_name}\n📧 Email: {email}\n📍 Address: {address}\n📱 Phone: {phone}")



def generate_surprise_data():
    """Generate 'Surprise Me!' fake data with an email based on the actual name."""
    actual_name = fake.name()
    
    # Generate an email using the real name
    first_name, last_name = actual_name.split()[:2]  # Take only first and last name
    email = f"{first_name.lower()}.{last_name.lower()}@example.com"

    fun_name = f"{random.choice(fun_prefixes)} {actual_name} the {random.choice(fun_suffixes)}"
    address = fake.address().replace("\n", ", ")

    result_var.set(f"🌟 Special Name: {fun_name}\n📧 Email: {email}\n📍 Address: {address}\n🔹 Actual Name: {actual_name}")


def copy_to_clipboard(event=None):
    """Copy displayed data to clipboard when clicked."""
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    root.update()
    messagebox.showinfo("✨ Copied!", "Data magically copied to clipboard!")


def export_json():
    """Export 10 fake data records to JSON."""
    data = [{"name": fake.name(), "email": fake.email(),
             "address": fake.address().replace("\n", ", "),
             "phone": fake.phone_number()} for _ in range(10)]

    filepath = filedialog.asksaveasfilename(defaultextension=".json",
                                            filetypes=[("JSON files", "*.json")],
                                            title="Save Your Fake Data")

    if filepath:
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        messagebox.showinfo("🎉 Success!", "Fake data exported successfully!")


def change_theme(choice):
    """Change theme dynamically."""
    global current_theme
    current_theme = choice
    apply_theme()


# UI Components
title_label = tk.Label(root, text="✨ Fancy Fake Data Generator", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 12), wraplength=500,
                        justify=tk.LEFT, relief=tk.SUNKEN, padx=10, pady=10, cursor="hand2")
result_label.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

# "Click to Copy" functionality
result_label.bind("<Button-1>", copy_to_clipboard)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)
button_frame.config(bg=themes[current_theme]["bg"])

generate_btn = tk.Button(button_frame, text="🎲 Generate Normal Data", command=generate_fake_data)
generate_btn.pack(pady=5)

surprise_btn = tk.Button(button_frame, text="🎮 Surprise Me!", command=generate_surprise_data)
surprise_btn.pack(pady=5)

copy_btn = tk.Button(button_frame, text="📋 Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

export_btn = tk.Button(button_frame, text="💾 Export JSON", command=export_json)
export_btn.pack(pady=5)

# Theme Selector
theme_frame = tk.Frame(root)
theme_frame.pack(pady=20)
theme_frame.config(bg=themes[current_theme]["bg"])

theme_label = tk.Label(theme_frame, text="🎨 Select Theme:")
theme_label.pack(side=tk.LEFT, padx=5)

theme_selector = ttk.Combobox(theme_frame, values=list(themes.keys()), state="readonly", style="TCombobox")
theme_selector.set(current_theme)
theme_selector.bind("<<ComboboxSelected>>", lambda event: change_theme(theme_selector.get()))
theme_selector.pack(side=tk.LEFT, padx=5)

# Apply initial theme
apply_theme()

# Start the application
root.mainloop()