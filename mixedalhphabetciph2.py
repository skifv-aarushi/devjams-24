import random as r
import tkinter as tk
from tkinter import messagebox


def shuffle_cipher(txt):
    key = {}
    alph = list('abcdefghijklmnopqrstuvwxyz')
    shuff_alph = alph.copy()
    r.shuffle(shuff_alph)
   
   
    for i in range(26):
        key[alph[i]] = shuff_alph[i]

    ciph_txt = ''
   
    for i in txt:
        if i.isalpha():
            if i.islower():
                ciph_txt += key[i]
            else:
                ciph_txt += key[i.lower()].upper()
        else:
            ciph_txt += i
   
    return (key, ciph_txt)

def cipher_text():
    input_txt = entry.get()
    if not input_txt:
        messagebox.showwarning("Input Error", "Please enter text to cipher!")
        return

    key, ciphered = shuffle_cipher(input_txt.lower())
   
    ciphered_text.set(ciphered)
   
    key_str = ', '.join([f'{k.upper()} -> {v.upper()}' for k, v in key.items()])
    key_display.set(key_str)

root = tk.Tk()
root.title("Shuffle Cipher")

root.geometry("600x300")

tk.Label(root, text="Enter Text:", font=("Comis Sans MS", 14)).grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(root, width=50, font=("Comis Sans MS", 14))
entry.grid(row=0, column=1, padx=10, pady=10)

ciphered_text = tk.StringVar()
key_display = tk.StringVar()    


tk.Label(root, text="Ciphered Text:", font=("Comis Sans MS", 14)).grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=ciphered_text, state='readonly', width=50, font=("Comis Sans MS", 14)).grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Cipher Key:", font=("Comis Sans MS", 14)).grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=key_display, state='readonly', width=50, font=("Comis Sans MS", 14)).grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Cipher", command=cipher_text, bg="white", fg="black", font=("Arial", 25)).grid(row=3, column=0, columnspan=2, padx=10, pady=20)

root.configure(bg="#bfa88a")
root.mainloop()