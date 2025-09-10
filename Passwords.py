import secrets
import string


def passwords(length=12):
    # default length is 12 for the password.

    # choices is the string containing all characters that are acceptable for use in the password generation.
    choices = string.ascii_letters + string.digits + string.punctuation

    # returns a string of characters at random from the string of possible characters
    return "".join((secrets.choice(choices)) for i in range(length))


if __name__ == "__main__":
    print(passwords())
