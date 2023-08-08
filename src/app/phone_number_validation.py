import re

"""
4. Застосуйте свої знання регулярних виразів для валідації номера телефону.
"""


def validate_phone_number(phone_number, *args, **kwargs):
    pattern = r"\+380\d{9}\b"
    return re.match(pattern, phone_number) is not None


if __name__ == "__main__":
    phone_numbers = [
        "+3800123456789",
        "+380987654321",
        "+38012345",
        "+3801234567890",
        "+380123456789",
        "+38012345678901",
        "+380123456789a",
    ]

    valid_numbers = []

    for number in phone_numbers:
        if validate_phone_number(number):
            valid_numbers.append(number)
        else:
            print(f"{number} is not valid")

    print(f"Valid numbers: {valid_numbers}")
