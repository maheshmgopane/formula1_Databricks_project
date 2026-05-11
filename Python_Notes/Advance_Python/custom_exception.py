class InvalidAgeError(Exception):
    pass


def check_age(age):
    if age < 19:
        raise InvalidAgeError("Age must be 19 or above")
    print("Access Granted")


try:
    check_age(int(input("Please enter your age:")))
except InvalidAgeError as e:
    print("custom exception:", e)