import random

import pytest

from src.app.date_validation import regex_date
from src.app.email_finder import regex_email


def test_email_finder():
    text = """
        Lor@em.ip.sum ipsum bigdie_bam1@gmail.com.ua bigdie_bam1_@gmail.com.ua bigdie_bam1@gmail.com.ua_ dolor sit yegortrep-ipt27@lll.kpi.ua amet, consectetur 
        ad_ipiscin@g.i elit@.com git_hub@gmail.com sed do eiusmod tempor incididunt ut labore et dolore magna 
        aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea 
        commodo consequat. bigdiebam@gmail.com Duis aute irure dolor in reprehenderit in voluptate velit esse 
    """

    expected = [
        "Lor@em.ip.sum",
        "bigdie_bam1@gmail.com.ua",
        "bigdie_bam1@gmail.com",
        "yegortrep-ipt27@lll.kpi.ua",
        "git_hub@gmail.com",
        "bigdiebam@gmail.com",
    ]

    assert regex_email(text) == expected


def test_date_validation():
    dates_list = [
        f"{i}/{j}/{k}"
        for i in range(0, random.randint(1, 13))
        for j in range(0, random.randint(1, 32))
        for k in range(1000, 9999)
    ]

    assert regex_date("12/07/2004") == [("12", "07", "2004")]
    for i in dates_list:
        assert regex_date(i) is not None

    dates_list_fixed = [
        "12/07/2004",
        "12/07/200",
        "01/31/2004",
        "40/07/2008",
        "12/40/2023",
        "12/07/20",
        "30/01/20045",
        "12/07/2004/12",
        "12/07/2004/12/12",
        "12.07.2024",
    ]

    expected = [
        [("12", "07", "2004")],
        [("01", "31", "2004")],
        [],
    ]

    for j in dates_list_fixed:
        assert regex_date(j) in expected


if __name__ == "__main__":
    pytest.main()
