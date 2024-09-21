import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    
    return result

def encrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        encrypted_text = caesar_cipher(text, shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted_text)
    except ValueError:
        messagebox.showerror("Input Error", "Shift must be an integer.")

def decrypt():
    try:
        text = input_text.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        decrypted_text = caesar_cipher(text, -shift)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted_text)
    except ValueError:
        messagebox.showerror("Input Error", "Shift must be an integer.")
        
window = tk.Tk()
window.title("Caesar Cipher")

input_label = tk.Label(window, text="Enter Text:")
input_label.pack()

input_text = tk.Text(window, height=5, width=40)
input_text.pack()

shift_label = tk.Label(window, text="Enter Shift Value:")
shift_label.pack()

shift_entry = tk.Entry(window)
shift_entry.pack()

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt)
encrypt_button.pack()

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.pack()

output_label = tk.Label(window, text="Output Text:")
output_label.pack()

output_text = tk.Text(window, height=5, width=40)
output_text.pack()

window.mainloop()
