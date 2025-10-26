import json
import os
from fingerprint_utils import hash_fingerprint

USER_FILE = "users.json"

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def register_user(username, fingerprint_path):
    users = load_users()
    if username in users:
        print("⚠️ User already exists!")
        return
    hash_val = hash_fingerprint(fingerprint_path)
    users[username] = hash_val
    save_users(users)
    print("✅ User registered successfully!")

def authenticate_user(username, fingerprint_path):
    users = load_users()
    if username not in users:
        print("❌ User not found!")
        return
    new_hash = hash_fingerprint(fingerprint_path)
    if users[username] == new_hash:
        print("✅ Authentication Successful!")
    else:
        print("❌ Authentication Failed!")

if __name__ == "__main__":
    while True:
        print("\n=== Biometric Authentication System ===")
        print("1. Register User")
        print("2. Authenticate User")
        print("3. Exit")
        choice = input("Enter choice: ")
        
        if choice == "1":
            u = input("Enter username: ")
            f = input("Enter fingerprint image path: ")
            register_user(u, f)
        elif choice == "2":
            u = input("Enter username: ")
            f = input("Enter fingerprint image path: ")
            authenticate_user(u, f)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")
