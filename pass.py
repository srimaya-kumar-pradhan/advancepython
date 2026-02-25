# Password Strength Checker

def check_password(password):
    if len(password) < 6:
        print("Weak Password  (Too short)")
    elif password.isalpha() or password.isdigit():
        print("Medium Password (Add numbers or letters)")
    else:
        print("Strong Password ")

pwd = input("Enter your password: ")
check_password(pwd)