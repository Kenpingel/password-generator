import secrets
import string
import argparse


def main():
    args = cli_input()
    return generate_passwords(length=args.length, exclude_digits=args.digits, exclude_symbols=args.symbols)

def generate_passwords(length=12, exclude_digits=False, exclude_symbols=False): 
    """
    Generate a password that includes at least one lowercase, one uppercase, one digit, and one symbol.
    """
    # raising exeptions in case of length parameter issues.
    if not isinstance(length, int):
        raise TypeError("length must be an int")
    if length < 4:
        raise ValueError("length must be at least 4")
    
    # choices is the string containing all characters that are acceptable for use in the password generation.
    if exclude_digits and exclude_symbols:
        choices = string.ascii_letters
    elif exclude_digits:
        choices = string.ascii_letters + string.punctuation
    elif exclude_symbols:
        choices = string.ascii_letters + string.digits
    else:
        choices = string.ascii_letters + string.digits + string.punctuation

    # returns a string of characters at random from the string of possible characters with a default amount of one lowercase letter, one uppercase letter, one number, at at least one symbol.
    while True: 
        password = "".join(secrets.choice(choices) for i in range(length))
        if exclude_digits and exclude_symbols:
            test = any(ch.islower() for ch in password) and any(ch.isupper() for ch in password)
        elif exclude_digits:
            test = any(ch.islower() for ch in password) and any(ch.isupper() for ch in password) and any(ch in string.punctuation for ch in password)
        elif exclude_symbols:
            test = any(ch.islower() for ch in password) and any(ch.isupper() for ch in password) and any(ch.isdigit() for ch in password)
        else:
            test = any(ch.islower() for ch in password) and any(ch.isupper() for ch in password) and any(ch.isdigit() for ch in password) and any(ch in string.punctuation for ch in password)
        if (test):
            break
    return password

def cli_input():
    parser = argparse.ArgumentParser(
        prog="passwordgen",
        description="Generate secure passwords"
    )
    parser.add_argument("-l", "--length", type=int, default=12, help="Length of password")
    parser.add_argument("-d", "--digits", action="store_true", help="Exclude digits in the password")
    parser.add_argument("-s", "--symbols", action="store_true", help="Exclude symbols in the password")
    return parser.parse_args()


if __name__ == "__main__":
    print(main())
