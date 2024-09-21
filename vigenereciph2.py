import tkinter as tk
from tkinter import font as tkfont

# Vigenère Cipher Functions
def generate_key(text, key):
    key = list(key)
    key_expanded = []
    key_index = 0

    for char in text:
        if char.isalpha():  
            key_expanded.append(key[key_index % len(key)])
            key_index += 1
        else:
            key_expanded.append(char)

    return "".join(key_expanded)

def vigenere_encrypt(pln_txt, key):
    ciph_txt = []
    key = generate_key(pln_txt, key)

    for i in range(len(pln_txt)):
        if pln_txt[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            if pln_txt[i].isupper():
                cipher_char = chr((ord(pln_txt[i]) - ord('A') + shift) % 26 + ord('A'))
            else:
                cipher_char = chr((ord(pln_txt[i]) - ord('a') + shift) % 26 + ord('a'))
            ciph_txt.append(cipher_char)
        else:
            ciph_txt.append(pln_txt[i])

    return "".join(ciph_txt)

def vigenere_decrypt(ciph_txt, key):
    pln_txt = []
    key = generate_key(ciph_txt, key)

    for i in range(len(ciph_txt)):
        if ciph_txt[i].isalpha():
            shift = ord(key[i].upper()) - ord('A')
            if ciph_txt[i].isupper():
                plain_char = chr((ord(ciph_txt[i]) - ord('A') - shift + 26) % 26 + ord('A'))
            else:
                plain_char = chr((ord(ciph_txt[i]) - ord('a') - shift + 26) % 26 + ord('a'))
            pln_txt.append(plain_char)
        else:
            pln_txt.append(ciph_txt[i])

    return "".join(pln_txt)

# Function for the Encrypt Button
def encrypt_text():
    pln_txt = entry_plaintext.get()
    key = entry_key.get()

    if not pln_txt or not key:
        messagebox.showwarning("Input Error", "Please enter both text and key.")
        return

    encrypted = vigenere_encrypt(pln_txt, key)
    label_result.config(text="Encrypted: " + encrypted)

# Function for the Decrypt Button
def decrypt_text():
    ciph_txt = entry_plaintext.get()
    key = entry_key.get()

    if not ciph_txt or not key:
        messagebox.showwarning("Input Error", "Please enter both text and key.")
        return

    decrypted = vigenere_decrypt(ciph_txt, key)
    label_result.config(text="Decrypted: " + decrypted)


root = tk.Tk()
root.title("Vigenère Cipher with Spaces and Punctuation")


window_width = 1200
window_height = 600
root.geometry(f"{window_width}x{window_height}")


# Define Larger Fonts
label_font = tkfont.Font(family="Times New Romb B", size=20, weight="bold")
entry_font = tkfont.Font(family="Times New Romb B", size=20)
button_font = tkfont.Font(family="Times New Romb B", size=18, weight="bold")
result_font = tkfont.Font(family="Comic Sans MS", size=22, weight="bold")
padx = 30
pady = 30
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)
label_plaintext = tk.Label(root, text="Enter Text:", font=label_font, bg="white")
label_plaintext.grid(row=0, column=0, padx=padx, pady=pady, sticky='e')

entry_plaintext = tk.Entry(root, font=entry_font, width=30, bd=3, relief='groove')
entry_plaintext.grid(row=0, column=1, padx=padx, pady=20, sticky='w')

# Key Entry
label_key = tk.Label(root, text="Enter Key:", font=label_font, bg="white")
label_key.grid(row=1, column=0, padx=padx, pady=pady, sticky='e')

entry_key = tk.Entry(root, font=entry_font, width=30, bd=3, relief='groove')
entry_key.grid(row=1, column=1, padx=padx, pady=pady, sticky='w')
button_frame = tk.Frame(root, bg="#8a5d3d")
button_frame.grid(row=2, column=0, columnspan=2, pady=20)

# Encrypt Button
button_encrypt = tk.Button(
    button_frame,
    text="Encrypt",
    command=encrypt_text,
    font=button_font,
    width=13,
    height=2
)
button_encrypt.pack(side='left', padx=30, pady=20)

# Decrypt Button
button_decrypt = tk.Button(
    button_frame,
    text="Decrypt",
    command=decrypt_text,
    font=button_font,
    width=13,
    height=2
)
button_decrypt.pack(side='left', padx=30, pady=20)

# Result Label
label_result = tk.Label(
    root,
    text="Result:",
    font=result_font,
    wraplength=1100,
    justify="left",
    anchor="w",
    padx=20,
    pady=7,
    height=1
)
label_result.grid(row=3, column=0, columnspan=2, padx=padx, pady=pady, sticky='w')
root.configure(bg="#bfa88a")
root.mainloop()