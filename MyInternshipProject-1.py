import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password =" "
    for i in range(length):
        password += random.choice(characters)
    return password

def main():
    print("Random Password Generator")
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        password_length = int(input("Enter the desired password length: "))
        
        if num_passwords <= 0 or password_length <= 0:
            print("Please enter valid numbers for the number of passwords and password length.")
            return
        
        for i in range(num_passwords):
            password = generate_password(password_length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

main()
