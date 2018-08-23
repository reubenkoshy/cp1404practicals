"""Reuben Koshy"""


def main():
    password = get_password()

    check_password(password)


def check_password(password):
    while len(password) >= 0:
        if len(password) >= 8:
            print("Valid Password")
            print('*' * len(password))
            break
        else:
            print("Invalid password. Must be at least 8 characters in length")
            password = get_password()


def get_password():
    password = input("Enter a Password: ")
    return password


main()
