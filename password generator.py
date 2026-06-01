import secrets
import string

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than 0.")
        exit()

    while True:
        print("\nSelect Password Complexity")
        print("1. Letters Only")
        print("2. Letters + Numbers")
        print("3. Letters + Numbers + Special Characters")

        choice = input("Enter your choice (1-3): ")

        match choice:
            case "1":
                characters = string.ascii_letters
                break

            case "2":
                characters = string.ascii_letters + string.digits
                break

            case "3":
                characters = (
                    string.ascii_letters
                    + string.digits
                    + string.punctuation
                )
                break

            case _:
                print("Invalid choice! Please enter 1, 2, or 3.")

    password = ''.join(
        secrets.choice(characters)
        for _ in range(length)
    )

    print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid number for password length.")