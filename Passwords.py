import secrets
import string


def generate_passwords(length=12):
    # default length is 12 for the password.

    # choices is the string containing all characters that are acceptable for use in the password generation.
    choices = string.ascii_letters + string.digits + string.punctuation

    # returns a string of characters at random from the string of possible characters with a default amount of one lowercase letter, one uppercase letter, one number, at at least one symbol.
    while True: 
        password = "".join(secrets.choice(choices) for i in range(length))
        if (any(ch.islower() for ch in password) and any(ch.isupper() for ch in password) and any(ch.isdigit() for ch in password) and any(ch in string.punctuation for ch in password)):
            break
    return password


if __name__ == "__main__":
    print(generate_passwords())
