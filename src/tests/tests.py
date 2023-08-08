import random

import pytest

from src.app.date_validation import regex_date
from src.app.email_domain_and_name_scrapping import regex_email_domain_and_name
from src.app.email_finder import regex_email
from src.app.phone_number_validation import validate_phone_number
from src.app.text_on_centance import regex_split_text


def test_email_finder():
    text = """Lor@em.ip.sum ipsum bigdie_bam1@gmail.com.ua bigdie_bam1_@gmail.com.ua bigdie_bam1@gmail.com.ua_ dolor 
    sit yegortrep-ipt27@lll.kpi.ua amet, consectetur ad_ipiscin@g.i elit@.com git_hub@gmail.com sed do eiusmod tempor 
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat. bigdiebam@gmail.com Duis aute irure dolor in reprehenderit in voluptate 
    velit esse"""

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
    dates_list_tens = [
        f"{month}/{day}/{year}"
        for month in range(10, random.randint(10, 13))
        for day in range(10, random.randint(10, 32))
        for year in range(1000, 9999)
    ]

    dates_list_one_digit = [
        f"0{month}/0{day}/{year}"
        for month in range(1, 9)
        for day in range(1, 9)
        for year in range(1000, 9999)
    ]

    for date in dates_list_tens:
        assert regex_date(date) is not None

    for date_single_digit in dates_list_one_digit:
        assert regex_date(date_single_digit) is not None

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

    for fixed_date in dates_list_fixed:
        assert regex_date(fixed_date) in expected


def test_email_domain_and_name_scrapping():
    text = """
        _Lorem.ip.sum ipsum dolor sit amet, consectetur elit@.com sed do eiusmod tempor incididunt ut labore 
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex 
        ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse bigdiebam@gmail.com 
        yegortrep-ipt27@lll.kpi.ua bit_fie@example.com.ua bit_fie_@example.com.ua """

    expected = [
        ("bigdiebam", "gmail.com"),
        ("yegortrep-ipt27", "lll.kpi.ua"),
        ("bit_fie", "example.com.ua"),
    ]

    assert regex_email_domain_and_name(text) == expected


def test_validate_phone_number():
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

    expected = [
        "+380(01)23456789",
        "+380987654321",
        "+380(12)345",
        "+380(12)34567890",
        "+380123456789",
        "+38012345678901",
        "+380(67)1234567",
        "+380(67)123-4567",
        "+380(67)1234567",
    ]

    for number in phone_numbers:
        if validate_phone_number(number):
            assert number in expected


def test_regex_split_text():
    expected = [
        "Dovahkiin, Dovahkiin, naal ok zin los vahriin, Wah dein vokul mahfaeraak "
        "ahst vaal!",
        " Ahrk fin norokpaal graan fod nust hon zindro zaan, Dovahkiin, fah hin "
        "kogaan mu draal!",
        "Huzrah nu, kul do od, wah aan boklingrah vod, Ahrk fin tey, boziik fun, do "
        "fin gein!",
        " Wo lostfron wah ney dov, ahrk fin reyliik do jul,Voth aan suleyk wah ronit "
        "faal krein!",
        " Ahrk fin zul, rok drey kod, nau tol morokei frod,Rul lot Taazokaanmotaad "
        "voth kein!",
        " Sahrot Thu'um, med aan tuz, vey zeim hokoron pah,Ol fin Dovakiin komeyt ok "
        "rein!",
        " Dovahkiin,Dovahkiin, naal ok zin los vahriin,Wah dein vokul mahfaeraak ahst "
        "vaal!",
        "Ahrk fin norok paal graan fod nust honzindro zaan,Dovahkiin, fah hin kogaan "
        "mu draal!",
        " Ahrk fin Kel lost prodah, do ved viing ko fin krah,Tol fod zeymah win kein "
        "meyz fuundein!",
        "Alduin, feyn do jun, kruziik vokun, staadnav,Voth aan bahlok wah diivonfin "
        "lein!",
        " Nuz aan sul, fent alok, fod fin vul dovah nok,Fen kos nahlot mahfaeraak "
        "ahrk ruz!",
        "Paaz Keizaal fenkos stin nol bein Alduin jot,Dovahkiin kos fin saviik do "
        "muz!",
        " Dovahkiin, Dovahkiin, naal ok zin los vahriin,Wah dein vokul mahfaeraak "
        "ahst vaal!",
        "Ahrk fin norok paal graan fod nust hon zindro zaan,Dovahkiin, fah hin kogaan "
        "mu draa",
    ]

    assert regex_split_text() == expected


def main():
    test_regex_split_text()
    test_date_validation()
    test_validate_phone_number()
    test_email_domain_and_name_scrapping()
    test_email_finder()


if __name__ == "__main__":
    pytest.main()
