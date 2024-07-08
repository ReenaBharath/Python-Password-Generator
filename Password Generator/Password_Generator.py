import random

def generate_password(length=8):
    # Define character sets
    uppercase_letters = [chr(random.randint(65, 90)) for _ in range(length // 4)]
    lowercase_letters = [chr(random.randint(97, 122)) for _ in range(length // 4)]
    numbers = [chr(random.randint(48, 57)) for _ in range(length // 4)]
    symbols = [chr(random.randint(33, 47)) for _ in range(length - len(uppercase_letters) - len(lowercase_letters) - len(numbers))]

    # Combine all character sets
    all_chars = uppercase_letters + lowercase_letters + numbers + symbols

    # Shuffle and join to form password
    random.shuffle(all_chars)
    password = ''.join(all_chars)

    return password

# Main program starts here
if __name__ == "__main__":
    try:
        while True:
            # Prompt user for password length
            password_length = int(input("Enter password length (default is 8): ") or 8)
            
            # Validate password length
            if password_length < 8:
                raise ValueError("Password length should be at least 8 characters.")
            
            # Generate password
            password = generate_password(length=password_length)
            print(f"Generated Password: {password}")
            
            # Ask user if they want to generate another password
            repeat = input("Generate another password? (yes/no): ").strip().lower()
            if repeat != "yes":
                break
    
    except ValueError as ve:
        print(f"Error: {ve}")