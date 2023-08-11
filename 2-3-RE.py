import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        print(email, "is a valid email address.")
    else:
        print(email, "is not a valid email address.")

def main():
    email = input("Enter an email address: ")
    validate_email(email)

if __name__ == '__main__':
    main()