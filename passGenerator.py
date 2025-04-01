#!/usr/bin/env python3

import secrets
import string
import os
# from datetime import datetime


def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))
def save_password(password, reason):

    if not os.path.exists('/home/blank/passwords'):
        os.makedirs('/home/blank/passwords')


    # timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    password_file = os.path.join('/home/blank/passwords', f"password_{reason}.txt")

    with open(password_file, 'w') as f:
        f.write(f'Password: {password}\nDescription: {reason}\n\n')
    
    return password_file

password = generate_password()

reason = input(f"what is this passoword for?\nInput: ")

password_file = save_password(password, reason)

save_password(password, reason)

print(f'Here is your cryptographicaslly secure password for {reason}:\n{password}\n\nYour password and information has been written to {password_file}')


