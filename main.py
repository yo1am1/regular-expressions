from src.app import (
    date_validation,
    email_finder,
    text_on_centance,
    phone_number_validation,
    email_domain_and_name_scrapping,
)

import threading
from src.tests import tests


def output(func):
    def wrapper():
        print("-" * 100)
        print(f"Task {func.__name__[-1]}")
        answer = func()
        print("-" * 100)
        return print(answer)

    return wrapper


@output
def task_1():
    return email_finder.regex_email(
        "_Lor@em.ip.sum ipsum bigdie_bam1@gmail.com.ua dolor sit yegortrep-ipt27@lll.kpi.ua amet, consectetur "
        "ad_ipiscin@g.i elit@.com git_hub@gmail.com sed do eiusmod tempor incididunt ut labore et dolore magna "
        "aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
        "commodo consequat. bigdiebam@gmail.com Duis aute irure dolor in reprehenderit in voluptate velit esse"
    )


@output
def task_2():
    return date_validation.regex_date(text="12/07/2004")


@output
def task_3():
    return email_domain_and_name_scrapping.regex_email_domain_and_name(
        """_Lorem.ip.sum ipsum dolor sit amet, consectetur elit@.com sed do eiusmod tempor incididunt ut labore 
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex 
        ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse bigdiebam@gmail.com 
        yegortrep-ipt27@lll.kpi.ua bit_fie@example.com.ua"""
    )


@output
def task_4():
    phone_numbers = [
        "+3800123456789",
        "+380987654321",
        "+38012345",
        "+3801234567890",
        "+380123456789",
        "+38012345678901",
        "+380123456789a",
    ]

    answer = []

    for phone_number in phone_numbers:
        if phone_number_validation.validate_phone_number(phone_number):
            answer.append(f"{phone_number} is valid phone number")
        else:
            answer.append(f"{phone_number} is not valid phone number")

    return answer


@output
def task_5():
    return text_on_centance.regex_split_text(
        text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et "
        "dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
        "commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat "
        "nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit "
        "anim id est laborum."
    )


if __name__ == "__main__":
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
