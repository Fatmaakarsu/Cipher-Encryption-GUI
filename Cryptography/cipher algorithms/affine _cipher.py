import tkinter as tk

def affine_encrypt(plain_text, a, b):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char_index = ord(char.lower()) - ord('a')
            encrypted_char = chr((a * char_index + b) % 26 + ord('a')).upper() if is_upper else chr((a * char_index + b) % 26 + ord('a'))
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

def encrypt():
    entered_message = entry_message.get()
    a_value = int(entry_a.get())
    b_value = int(entry_b.get())

    # a'nın ve 26'nın aralarında asal olup olmadığını kontrol et
    if greatest_common_divisor(a_value, 26) != 1:
        result_label.config(text="Invalid values for 'a'! Must be coprime with 26.")
        return

    encrypted_message = affine_encrypt(entered_message, a_value, b_value)
    result_label.config(text="Encrypted Message: " + encrypted_message)

def greatest_common_divisor(a, b):
    while b:
        a, b = b, a % b
    return a

# Ana pencere oluştur
root = tk.Tk()
root.title("Affine Cipher Interface")
root.geometry("400x300")  # Pencere boyutunu ayarla

# Mesaj giriş kutusu
label_message = tk.Label(root, text="Enter your message:")
label_message.pack()

entry_message = tk.Entry(root)
entry_message.pack()

# 'a' değeri giriş kutusu
label_a = tk.Label(root, text="Enter the 'a' value (must be coprime with 26):")
label_a.pack()

entry_a = tk.Entry(root)
entry_a.pack()

# 'b' değeri giriş kutusu
label_b = tk.Label(root, text="Enter the 'b' value:")
label_b.pack()

entry_b = tk.Entry(root)
entry_b.pack()

# Şifreleme düğmesi
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.pack()

# Sonuç etiketi
result_label = tk.Label(root, text="")
result_label.pack()

# Tkinter uygulamasını başlat
root.mainloop()
