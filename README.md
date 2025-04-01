Secure Password Generator & Storage System
Overview

This project provides a secure password generator that creates strong, random passwords and an optional password storage system to save passwords with descriptions. Future enhancements include integrating an API to check if a generated password has been leaked.
Features

✅ Generates strong, random passwords using cryptographically secure methods
✅ Supports customizable password length
✅ Stores generated passwords along with descriptions in a secure local directory
✅ Automatically creates the storage directory if it doesn’t exist
✅ API integration to check if passwords have been exposed in data breaches
Installation
Requirements

    Python 3.x

    Internet connection (for API features, if implemented)

Setup

    Clone this repository:

git clone https://github.com/yourusername/password-generator.git
cd password-generator

Run the script:

    python3 password_generator.py

Usage
1. Generate a Password

Run the script, and it will generate a secure password for you:

python3 passGenerator.py

Example Output:

Generated password: h7!2D$xA9m^1@pF

2. Save the Password

The script prompts you to enter a description (e.g., "Gmail Account"). It then saves the password in:

/home/blank/passwords/passwords.txt

Example Entry in passwords.txt:

Password: h7!2D$xA9m^1@pF
Description: Gmail Account

3. Check If a Password Has Been Leaked

With API integration, users will be able to check if their password appears in known breaches using Have I Been Pwned’s API.
Security Considerations

    This tool does not encrypt saved passwords. Consider encrypting them for extra security.

    Do not use weak passwords or reuse them across multiple sites.

Future Enhancements

    API integration with Have I Been Pwned for breach detection

    GUI or CLI menu for easier password management

    Encryption for password storage
