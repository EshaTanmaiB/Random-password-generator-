import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    characters = string.ascii_letters  # A-Z, a-z

    if use_digits:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation  # !@#$%^&*()...

    if not characters:
        return "Error: No character sets selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator")
    
    try:
        length = int(input("Enter password length (default 12): ") or 12)
    except ValueError:
        print("Invalid input. Using default length 12.")
        length = 12

    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_digits, use_special)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
