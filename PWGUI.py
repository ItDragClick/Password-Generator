import tkinter as tk
import random
import string
import tkinter.messagebox as messagebox
from warnings import warn
import webbrowser

def open_github():
    webbrowser.open("https://github.com/ItDragClick")

def open_twitter():
    webbrowser.open("https://twitter.com/ItDragClick")

def open_youtube():
    webbrowser.open("https://www.youtube.com/@itdragclick")

def increment_length():
    current_length = int(length_entry.get())
    if current_length < 1024:
        length_entry.delete(0, tk.END)
        length_entry.insert(tk.END, current_length + 1)

def decrement_length():
    current_length = int(length_entry.get())
    if current_length > 6:
        length_entry.delete(0, tk.END)
        length_entry.insert(tk.END, current_length - 1)

def validate_length_entry(value):
    if value.isdigit() or value == "":
        return True
    else:
        return False
    
def generate_random_password():
    password_min_length = 6
    password_max_length = 1024
    if length_entry.get() == "":
        length_entry.delete(0, tk.END)
        length_entry.insert(tk.END, "16")
    password_length = int(length_entry.get())

    if password_length < password_min_length or password_length > password_max_length:
        print('\nInvalid Password Length.')
        messagebox.showerror("Invalid Password Length", "Password Length should be between 6 and 1024")
        return

    password_characters = ""
    if uppercase_var.get():
        password_characters += string.ascii_uppercase
    if lowercase_var.get():
        password_characters += string.ascii_lowercase
    if numbers_var.get():
        password_characters += string.digits
    if symbols_var.get():
        password_characters += string.punctuation

    if password_characters == "":
        print('\nInvalid Password Options.')
        messagebox.showerror("Invalid Password Options", "Password Options need to be checked!")
        return
    
    print('\nPassword Generating...')
    random_password = ''.join(random.choice(password_characters) for _ in range(password_length))
    password_text.config(state=tk.NORMAL)
    password_text.delete("1.0", tk.END)
    password_text.insert(tk.END, random_password)
    password_text.config(state=tk.DISABLED)
    print('\nPassword Generated.')

def copy_password_to_clipboard():
    generated_password = password_text.get("1.0", tk.END).strip()
    window.clipboard_clear()
    window.clipboard_append(generated_password)
    print('\nPassword Copied.')
    messagebox.showinfo("Password Copied", "The generated password has been copied to the clipboard.")

# Create the main window
window = tk.Tk()
window.resizable(False, False)
window.title("Password Generator")

# Create the password length label, entry, and buttons
length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)

length_frame = tk.Frame(window)
length_frame.grid(row=0, column=1, padx=10, pady=10)

validate_cmd = window.register(validate_length_entry)
length_entry = tk.Entry(length_frame, width=10, validate="key", validatecommand=(validate_cmd, "%P"))
length_entry.insert(tk.END, "16")  # Set default length to 16
length_entry.pack(side=tk.LEFT)

increment_button = tk.Button(length_frame, text="+", command=increment_length)
increment_button.pack(side=tk.LEFT, padx=5)

decrement_button = tk.Button(length_frame, text="-", command=decrement_length)
decrement_button.pack(side=tk.LEFT)

# Create the password options check buttons
options_label = tk.Label(window, text="Password Options:")
options_label.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

options_frame = tk.Frame(window)
options_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(options_frame, text="Uppercase", variable=uppercase_var)
uppercase_check.pack(anchor=tk.W)

lowercase_var = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(options_frame, text="Lowercase", variable=lowercase_var)
lowercase_check.pack(anchor=tk.W)

numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(options_frame, text="Numbers", variable=numbers_var)
numbers_check.pack(anchor=tk.W)

symbols_var = tk.BooleanVar(value=True)
symbols_check = tk.Checkbutton(options_frame, text="Symbols", variable=symbols_var)
symbols_check.pack(anchor=tk.W)

# Create the "Generate Password" button
generate_password_button = tk.Button(window, text="Generate Password", command=generate_random_password)
generate_password_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create the password text box
password_text = tk.Text(window, height=5, width=30)
password_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
password_text.config(state=tk.DISABLED)

# Create the scroll bar
scrollbar = tk.Scrollbar(window)
scrollbar.grid(row=4, column=2, padx=0, pady=10, sticky=tk.N+tk.S)

# Connect the scroll bar to the password text box
password_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=password_text.yview)

# Create the "Copy Password" button
copy_password_button = tk.Button(window, text="Copy Password", command=copy_password_to_clipboard)
copy_password_button.grid(row=5, column=0, columnspan=2, padx=10, pady=20)

# Create the "Credits" text/button
credits_Label = tk.Label(window, text="Credits")
credits_Label.grid(row=6, column=0, columnspan=2, padx=10, pady=2)
twitter_button = tk.Button(window, text="Twitter", command=open_twitter)
twitter_button.grid(row=7, column=1, columnspan=1, padx=10, pady=2)
github_button = tk.Button(window, text="GitHub", command=open_github)
github_button.grid(row=7, column=0, columnspan=1, padx=10, pady=10)

# Run the main event loop
window.mainloop()
