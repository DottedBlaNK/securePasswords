#!/usr/bin/env python3

import os
import hashlib
import requests

passwords_dir = "your password directory"

def get_hash_prefix(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1_hash[:5], sha1_hash[5:]

def check_pwned_password(password):
    prefix, suffix = get_hash_prefix(password)
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
        
        hashes = response.text.splitlines()
        for hash_entry in hashes:
            hash_suffix, count = hash_entry.split(":")
            if hash_suffix == suffix:
                return True, count
        return False, None  
    else:
        print("Error fetching data from Have I Been Pwned.")
        return False, None

def check_passwords_in_file(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    for i in range(0, len(lines), 3):
        password_line = lines[i].strip().split(":")[1].strip()
        description_line = lines[i+1].strip().split(":")[1].strip()
        
        print(f"Checking password for {description_line} in file {file_path}...")
        is_pwned, count = check_pwned_password(password_line)
        
        if is_pwned:
            print(f"Warning: The password for {description_line} has been pwned {count} times!")
        else:
            print(f"Password for {description_line} is safe.")

def check_all_password_files():
    for filename in os.listdir(passwords_dir):
        if filename.startswith("password") and filename.endswith(".txt"):
            file_path = os.path.join(passwords_dir, filename)
            print(f"\nChecking passwords in file: {file_path}")
            check_passwords_in_file(file_path)

check_all_password_files()
