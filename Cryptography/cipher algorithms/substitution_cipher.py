import tkinter as tk

# Önceden tanımlanmış substitution key
default_substitution_key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def substitution_encrypt(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = ord(char.lower()) - ord('a')
            encrypted_char = default_substitution_key[char_index].upper() if is_upper else default_substitution_key[char_index]
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def show_default_key():
    result_label.config(text="Default Substitution Key: " + default_substitution_key)

def encrypt():
    entered_message = entry_message.get()
    encrypted_message = substitution_encrypt(entered_message)
    result_label.config(text="Encrypted Message: " + encrypted_message)

# Ana pencere oluştur
root = tk.Tk()
root.title("Substitution Cipher Interface")
root.geometry("400x300")  # Pencere boyutunu ayarla

# Mesaj giriş kutusu
label_message = tk.Label(root, text="Enter your message:")
label_message.pack()

entry_message = tk.Entry(root)
entry_message.pack()

# Varsayılan anahtarı gösteren düğme
show_key_button = tk.Button(root, text="Show Default Key", command=show_default_key)
show_key_button.pack()

# Şifreleme düğmesi
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

# Sonuç etiketi
result_label = tk.Label(root, text="")
result_label.pack()

# Tkinter uygulamasını başlat
root.mainloop()
