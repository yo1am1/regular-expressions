import re

"""
4. Застосуйте свої знання регулярних виразів для валідації номера телефону.
"""


def validate_phone_number(phone_number, *args, **kwargs):
    pattern = r"^\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}$"
    return re.match(pattern, phone_number) is not None


if __name__ == "__main__":
    phone_numbers = [
        "+380(01)23456789",
        "+380987654321",
        "+380(12)345",
        "+380(12)34567890",
        "+380123456789",
        "+38012345678901",
        "+380123456789a",
        "+380(67)123-45-67",
        "+380(67)123-45-67",
        "+380(67)1234567",
        "+380(67)123-4567",
        "+380(67)1234567",
        "+380(67)123-45-67",
    ]

    valid_numbers = []

    for number in phone_numbers:
        if validate_phone_number(number):
            valid_numbers.append(number)
        else:
            print(f"{number} is not valid")

    print(f"Valid numbers: {valid_numbers}")
