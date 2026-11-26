
# Password Policy Validation Engine

password = input("Enter your password: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False

for ch in password:

    if ch >= 'A' and ch <= 'Z':
        has_upper = True

    elif ch >= 'a' and ch <= 'z':
        has_lower = True

    elif ch >= '0' and ch <= '9':
        has_digit = True

    else:
        has_special = True

print("\n--- Password Validation ---")

if length >= 8:
    print("Minimum length: Passed")
else:
    print("Minimum length: Failed")

if has_upper:
    print("Uppercase letter: Passed")
else:
    print("Uppercase letter: Failed")

if has_lower:
    print("Lowercase letter: Passed")
else:
    print("Lowercase letter: Failed")

if has_digit:
    print("Number: Passed")
else:
    print("Number: Failed")

if has_special:
    print("Special character: Passed")
else:
    print("Special character: Failed")

if length >= 8 and has_upper and has_lower and has_digit and has_special:
    print("\nPassword is Valid")
else:
    print("\nPassword is Invalid")
