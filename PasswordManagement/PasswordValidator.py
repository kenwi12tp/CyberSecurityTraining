import hashlib
import os
import sqlite3
conn = sqlite3.connect("passwordManagementDatabase.db")
cursor = conn.cursor()


def whats_missing(has_upper,has_lower,has_digit,has_special, length, different_chars, password, temp_password):
    if has_upper == False:
        print("your missing an uppercase letter")
    if has_lower == False:
        print("your missing an lowercase letter")
    if has_digit == False:
        print("your missing an digit")
    if has_special == False:
        print("your missing an special character")
    if length == False:
        print(f"your password isnt 12 letters its {len(password)} long")
    if different_chars == False:
        print(f"you only have {len(temp_password)} characters you need 6")

def user_creator(conn, cursor, whats_missing):
    special = ["!", "@", "#", "?", "-", "_"]
    user = input("Enter your username: ")
    while True:
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        length = False
        different_chars = False
        points = 0
        temp_password =[]
        print("Welcome to Password Management\nyour new password should contain 12 letters, 6 different characters, lowercase letter, uppercase letter, a digit and a special character")
        password = input("Enter your password: ")
        if len(password) >= 12:
            length = True
            points = points + 1

        for char in password:
            if char.isupper():
                if has_upper == False:
                    points = points + 1
                has_upper = True

            elif char.islower():
                if has_lower == False:
                    points = points + 1
                has_lower = True

            elif char.isdigit():
                if has_digit == False:
                    points = points + 1
                has_digit = True

            elif char in special:
                if has_special == False:
                    points = points + 1
                has_special = True
            if char not in temp_password:
                temp_password.append(char)

        if len(temp_password) >= 6:
            different_chars = True

        print(points)
        if points == 1:
            print("Password is very weak")
            whats_missing(has_upper, has_lower, has_digit, has_special, length, different_chars, password, temp_password)
        elif points == 2:
            print("Password is weak")
            whats_missing(has_upper,has_lower,has_digit,has_special,length, different_chars, password, temp_password)
        elif points <= 4:
            print("Password is medium")
            whats_missing(has_upper, has_lower, has_digit, has_special, length, different_chars, password, temp_password)
        elif points <= 6:
            print("Password is strong")
        quit = input("Do you want to remake your password (y/n)")
        if quit == "n":
            print(f"Password is set")
            salt = os.urandom(16)
            password_hash=hashlib.pbkdf2_hmac("sha256",password.encode(),salt,600_000)
            password_hash=password_hash.hex()
            salt = salt.hex()
            print(password_hash)
            print(salt)
            cursor.execute("""INSERT INTO users (username, Password_hash, salt) VALUES(?,?,?)""",(user,password_hash,salt))
            conn.commit()
            break
def login(cursor):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    data = cursor.execute("""SELECT Password_hash, salt FROM users WHERE username = ?""", (username,))
    userdata = data.fetchone()
    if userdata is None:
        print("Invalid username or password")
    else:
        print("User found!")
        salt = bytes.fromhex(userdata[1])
        password_hash = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000).hex()
        if userdata[0] == password_hash:
            print("login successful")
        else:
            print("invalid username or password")

while True:
    function_chooser = input("login press 1\ncreate user press 2\nquit press 3")
    if function_chooser == "1":
        login(cursor)
    elif function_chooser == "2":
        user_creator(conn, cursor, whats_missing)
    elif function_chooser == "3":
        break
    else:
        print("invalid input only press one or 2")