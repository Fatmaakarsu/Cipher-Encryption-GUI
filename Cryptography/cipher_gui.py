import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = ord(char.lower()) - ord('a')
            encrypted_char = chr((char_index + shift) % 26 + ord('a')).upper() if is_upper else chr((char_index + shift) % 26 + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def affine_cipher(message, a, b):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = ord(char.lower()) - ord('a')
            encrypted_char = chr((a * char_index + b) % 26 + ord('a')).upper() if is_upper else chr((a * char_index + b) % 26 + ord('a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def substitution_cipher(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = ord(char.lower()) - ord('a')
            encrypted_char = key[char_index].upper() if is_upper else key[char_index]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def update_widgets():
    current_cipher = cipher_choice.get()
    if current_cipher == "Caesar":
        label_caesar_shift.pack()
        entry_caesar_shift.pack()
        label_affine_a.pack_forget()
        entry_affine_a.pack_forget()
        label_affine_b.pack_forget()
        entry_affine_b.pack_forget()
        label_substitution_key.pack_forget()
        entry_substitution_key.pack_forget()
    elif current_cipher == "Affine":
        label_caesar_shift.pack_forget()
        entry_caesar_shift.pack_forget()
        label_affine_a.pack()
        entry_affine_a.pack()
        label_affine_b.pack()
        entry_affine_b.pack()
        label_substitution_key.pack_forget()
        entry_substitution_key.pack_forget()
    elif current_cipher == "Substitution":
        label_caesar_shift.pack_forget()
        entry_caesar_shift.pack_forget()
        label_affine_a.pack_forget()
        entry_affine_a.pack_forget()
        label_affine_b.pack_forget()
        entry_affine_b.pack_forget()
        label_substitution_key.pack()
        entry_substitution_key.pack()
    else:
        messagebox.showerror("Error", "Invalid cipher choice.")

def encrypt():
    entered_message = entry_message.get()

    if not entered_message:
        messagebox.showerror("Error", "Please enter a message.")
        return

    current_cipher = cipher_choice.get()

    if current_cipher == "Caesar":
        shift_value = int(entry_caesar_shift.get())
        encrypted_message = caesar_cipher(entered_message, shift_value)
    elif current_cipher == "Affine":
        a_value = int(entry_affine_a.get())
        b_value = int(entry_affine_b.get())
        encrypted_message = affine_cipher(entered_message, a_value, b_value)
    elif current_cipher == "Substitution":
        substitution_key = entry_substitution_key.get()
        encrypted_message = substitution_cipher(entered_message, substitution_key)
    else:
        messagebox.showerror("Error", "Invalid cipher choice.")
        return

    result_label.config(text="Encrypted Message: " + encrypted_message)  

# Create the main window
root = tk.Tk()
root.title("Cipher Encryption Interface")
root.geometry("500x440")  # Set window size

# Add background image
image_path = "background_image.png"  # Change the file name of the image
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Message input box
label_message = tk.Label(root, text="Enter your message:", bg="white")  
label_message.pack(pady=5)

entry_message = tk.Entry(root)
entry_message.pack(pady=5)

# Choose encryption method
label_cipher_choice = tk.Label(root, text="Choose encryption method:", bg="lightblue")  
label_cipher_choice.pack(pady=5)

cipher_choice = tk.StringVar()
cipher_choice.set("Caesar")

radiobutton_caesar = tk.Radiobutton(root, text="Caesar Cipher", variable=cipher_choice, value="Caesar", command=update_widgets, bg="white")  
radiobutton_caesar.pack(pady=5)

radiobutton_affine = tk.Radiobutton(root, text="Affine Cipher", variable=cipher_choice, value="Affine", command=update_widgets, bg="white")  
radiobutton_affine.pack(pady=5)

radiobutton_substitution = tk.Radiobutton(root, text="Substitution Cipher", variable=cipher_choice, value="Substitution", command=update_widgets, bg="white")  
radiobutton_substitution.pack(pady=5)

# Additional input boxes
label_caesar_shift = tk.Label(root, text="Enter the shift value (for Caesar Cipher):", bg="lightblue")  
entry_caesar_shift = tk.Entry(root)

label_affine_a = tk.Label(root, text="Enter the 'a' value (for Affine Cipher):", bg="lightblue")  
entry_affine_a = tk.Entry(root)

label_affine_b = tk.Label(root, text="Enter the 'b' value (for Affine Cipher):", bg="lightblue")  
entry_affine_b = tk.Entry(root)

label_substitution_key = tk.Label(root, text="Enter the substitution key (for Substitution Cipher):", bg="lightblue")  
entry_substitution_key = tk.Entry(root)

frame_entries = tk.Frame(root, bg="lightblue")
frame_entries.pack(pady=5)

# Encryption button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt, bg="red")  
encrypt_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", bg="yellow")  
result_label.pack(pady=5)

# Start the Tkinter application
root.mainloop()
