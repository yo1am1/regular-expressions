import re

"""
1. Напишіть регулярний вираз, який знаходить усі входження email у тексті.
"""


def regex_email(text: str) -> list[str]:
    regex_pattern = r"\b(?:[A-Za-z0-9.%+-]*[A-Za-z0-9][A-Za-z0-9.%+_\-]*[A-Za-z0-9])@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}\b"
    answer = re.findall(regex_pattern, text)

    return answer


if __name__ == "__main__":
    regex_email(
        text="_Lor@em.ip.sum ipsum bigdie_bam1@gmail.com.ua dolor sit yegortrep-ipt27@lll.kpi.ua amet, consectetur "
        "ad_ipiscin@g.i elit@.com git_hub@gmail.com sed do eiusmod tempor incididunt ut labore et dolore magna "
        "aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea "
        "commodo consequat. bigdiebam@gmail.com Duis aute irure dolor in reprehenderit in voluptate velit esse "
    )
