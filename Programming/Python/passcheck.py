# List of commonly used (weak) passwords
weak_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567",
    "qwerty", "abc123", "111111", "123123", "admin", "abcd", "letmein", "welcome"
]

# Function to check for weak passwords
def check_weak_passwords(user_passwords, weak_passwords):
    for password in user_passwords:
        if password in weak_passwords:
            print(f"Warning: The password '{password}' is weak and should be changed!")
        else:
            print(f"The password '{password}' is strong enough.")

# Get user input
user_passwords = input("Enter passwords to check, separated by commas: ").split(',')

# Trim any extra spaces around the passwords
user_passwords = [password.strip() for password in user_passwords]

# Run the check
check_weak_passwords(user_passwords, weak_passwords)