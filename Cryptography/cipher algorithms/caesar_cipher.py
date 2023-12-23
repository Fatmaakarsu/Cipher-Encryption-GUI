import tkinter as tk

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for character in message:
        if character.isalpha():
            uppercase_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz'
            if character.isupper():
                encrypted_message += uppercase_alphabet[(uppercase_alphabet.index(character) + shift) % 26]
            else:
                encrypted_message += lowercase_alphabet[(lowercase_alphabet.index(character) + shift) % 26]
        else:
            encrypted_message += character
    return encrypted_message

def encrypt():
    entered_message = entry_message.get()
    shift_value = int(entry_shift.get())
    encrypted_message = caesar_encrypt(entered_message, shift_value)
    label_result.config(text="Encrypted Message: " + encrypted_message)

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher Interface")
root.geometry("400x200")  # Set the window size

# Message entry widget
label_message = tk.Label(root, text="Enter your message:")
label_message.pack()

entry_message = tk.Entry(root)
entry_message.pack()

# Shift value entry widget
label_shift = tk.Label(root, text="Shift Value:")
label_shift.pack()

entry_shift = tk.Entry(root)
entry_shift.pack()

# Encrypt button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

# Result label
label_result = tk.Label(root, text="")
label_result.pack()

# Start the Tkinter application
root.mainloop()
