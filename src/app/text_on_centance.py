import re

"""
5. Використайте регулярні вирази для розбиття тексту на речення.
"""


def regex_split_text(
    text: str = "Dovahkiin, Dovahkiin, naal ok zin los vahriin, Wah dein vokul mahfaeraak ahst vaal! Ahrk fin norok"
    "paal graan fod nust hon zindro zaan, Dovahkiin, fah hin kogaan mu draal!Huzrah nu, kul do od, wah aan bok"
    "lingrah vod, Ahrk fin tey, boziik fun, do fin gein! Wo lostfron wah ney dov, ahrk fin reyliik do jul,"
    "Voth aan suleyk wah ronit faal krein! Ahrk fin zul, rok drey kod, nau tol morokei frod,Rul lot Taazokaan"
    "motaad voth kein! Sahrot Thu'um, med aan tuz, vey zeim hokoron pah,Ol fin Dovakiin komeyt ok rein! Dovahkiin,"
    "Dovahkiin, naal ok zin los vahriin,Wah dein vokul mahfaeraak ahst vaal!Ahrk fin norok paal graan fod nust hon"
    "zindro zaan,Dovahkiin, fah hin kogaan mu draal! Ahrk fin Kel lost prodah, do ved viing ko fin krah,"
    "Tol fod zeymah win kein meyz fuundein!Alduin, feyn do jun, kruziik vokun, staadnav,Voth aan bahlok wah diivon"
    "fin lein! Nuz aan sul, fent alok, fod fin vul dovah nok,Fen kos nahlot mahfaeraak ahrk ruz!Paaz Keizaal fen"
    "kos stin nol bein Alduin jot,Dovahkiin kos fin saviik do muz! Dovahkiin, Dovahkiin, naal ok zin los vahriin,"
    "Wah dein vokul mahfaeraak ahst vaal!Ahrk fin norok paal graan fod nust hon zindro zaan,Dovahkiin, "
    "fah hin kogaan mu draa",
) -> list[str]:
    regex_pattern = r"([^.!?]+[.!?])"

    sentences = re.split(regex_pattern, text)
    sentences = [sentence for sentence in sentences if sentence.strip()]

    for sentence in sentences:
        print(sentence.strip())

    return sentences


if __name__ == "__main__":
    regex_split_text()
