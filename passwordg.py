import random
import string

def generate_password(length):
    if length < 1:
        return "Error: Password length must be at least 1."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Error: Password length must be at least 1.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        another = input("Do you want to generate another password? (yes/no): ").lower()
        if another != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
