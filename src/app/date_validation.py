import re

"""
2. Напишіть регулярний вираз, який валідує формат дати MM/DD/YYYY.
"""


def regex_date(text):
    regex_pattern = r"^(0[1-9]|1[0-2])\/([0-2][0-9]|3[0-1])\/([0-9]{4})$"
    answer = re.findall(regex_pattern, text)

    return answer


if __name__ == "__main__":
    regex_date(text="12/07/2004")
