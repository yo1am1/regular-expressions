import re

"""
3. Використовуйте групи в регулярних виразах для витягування імені та домену з email адрес.
"""


def regex_email_domain_and_name(text):
    regex_pattern = (
        r"\b(?P<name>[A-Za-z0-9.%+-]*[A-Za-z0-9][A-Za-z0-9.%+_\-]*[A-Za-z0-9])@(?P<domain>["
        r"A-Za-z0-9.-]+\.[A-Za-z]{2,7})\b"
    )

    answer = re.findall(regex_pattern, text)
    for match in answer:
        print("Name:", match[0])
        print("Domain:", match[1])

    return answer


if __name__ == "__main__":
    regex_email_domain_and_name(
        text="""_Lorem.ip.sum ipsum dolor sit amet, consectetur elit@.com sed do eiusmod tempor incididunt ut labore 
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex 
        ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse bigdiebam@gmail.com 
        yegortrep-ipt27@lll.kpi.ua bit_fie@example.com.ua"""
    )
