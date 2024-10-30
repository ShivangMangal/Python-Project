def level_one_password():
    """
    Function to set and verify Level 1 password.
    """
    print("Setting Level 1 password...")
    level_one_pass = input("Enter Level 1 password: ")
    print("Level 1 password set successfully!\n")

    print("Verifying Level 1 password...")
    while True:
        user_input = input("Enter Level 1 password to proceed: ")
        if user_input == level_one_pass:
            print("Level 1 password verified!")
            break
        else:
            print("Incorrect password. Try again.")

def level_two_password():
    """
    Function to set and verify Level 2 password.
    """
    print("Setting Level 2 password...")
    level_two_pass = input("Enter Level 2 password: ")
    print("Level 2 password set successfully!\n")

    print("Verifying Level 2 password...")
    while True:
        user_input = input("Enter Level 2 password to proceed: ")
        if user_input == level_two_pass:
            print("Level 2 password verified!")
            break
        else:
            print("Incorrect password. Try again.")

def level_three_password():
    """
    Function to set and verify Level 3 password.
    """
    print("Setting Level 3 password...")
    level_three_pass = input("Enter Level 3 password: ")
    print("Level 3 password set successfully!\n")

    print("Verifying Level 3 password...")
    while True:
        user_input = input("Enter Level 3 password to proceed: ")
        if user_input == level_three_pass:
            print("Level 3 password verified!")
            break
        else:
            print("Incorrect password. Try again.")

def main():
    print("Welcome to the three-level password system!\n")
    level_one_password()
    level_two_password()
    level_three_password()
    print("\nAll password levels verified. Access granted!")

if __name__ == "__main__":
    main()
