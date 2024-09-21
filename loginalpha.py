import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import messagebox


def create_connection():
    """ Create a connection to the MySQL database """
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='cipheroo',
            user='root',  
            password='mysql'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None


def verify_login(username, password):
    """ Verify login credentials from the database """
    connection = create_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
            print("Login successful!")
            return True
        else:
            print("Invalid username or password")
            return False
    except Error as e:
        print(f"Error while verifying login: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


def signup_user(username, password):
    """ Insert new user credentials into the database for sign-up """
    connection = create_connection()
    if connection is None:
        return False

    try:
        cursor = connection.cursor()
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        connection.commit()
        print("Sign-up successful!")
        return True
    except Error as e:
        print(f"Error while signing up: {e}")
        messagebox.showerror("Error", f"Username '{username}' already exists.")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed")


def attempt_login():
    """ Attempts to log in when the login button is pressed """
    username = entry_username.get()
    password = entry_password.get()

    if verify_login(username, password):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password")


def attempt_signup():
    """ Attempts to sign up when the sign-up button is pressed """
    username = entry_username.get()
    password = entry_password.get()

    if signup_user(username, password):
        messagebox.showinfo("Success", "Sign-up successful! You can now log in.")
    else:
        messagebox.showerror("Error", "Sign-up failed.")


def show_signup():
    """ Switch to the sign-up page """
    login_button.pack_forget()
    signup_button.config(text="Register", command=attempt_signup)
    signup_button.pack(pady=20)


def show_login():
    """ Switch to the login page """
    signup_button.pack_forget()
    login_button.pack(pady=20)


# Setting up the Tkinter window
root = tk.Tk()
root.title("Login & Sign-Up System")

# label and entry
label_username = tk.Label(root, text="Username")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)


label_password = tk.Label(root, text="Password")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login/sign up button
login_button = tk.Button(root, text="Login", command=attempt_login)
login_button.pack(pady=20)

signup_button = tk.Button(root, text="Sign-Up", command=show_signup)
signup_button.pack(pady=10)


root.mainloop()