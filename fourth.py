def je_tah_mozny_pesec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    # pokud se jedna o jiny sloupec, vrat False
    if aktualni_pozice[1] != cilova_pozice[1]:
        return False
    # pokud se pesak posune o 1 pole dopredu, vrat True
    if aktualni_pozice[0] + 1 == cilova_pozice[0]:
        return True
    # pokud je pesak na radku 2 a posune se o 2 pole dopredu a neni obsazeno pole po ceste, vrat True
    return aktualni_pozice[0] == 2 \
        and aktualni_pozice[0] + 2 == cilova_pozice[0] \
        and (aktualni_pozice[0] + 1, aktualni_pozice[1]) not in obsazene_pozice # bylo in v orig


def je_tah_mozny_jezdec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    for i in [1, 2]:
        if abs(aktualni_pozice[0] - cilova_pozice[0]) == 1 and abs(aktualni_pozice[1] - cilova_pozice[1]) == 2:
            return True
        if abs(aktualni_pozice[0] - cilova_pozice[0]) == 2 and abs(aktualni_pozice[1] - cilova_pozice[1]) == 1:
            return True
    return False


def je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if abs(aktualni_pozice[0] - cilova_pozice[0]) != abs(aktualni_pozice[1] - cilova_pozice[1]):
        return False
    for i in range(1, abs(aktualni_pozice[0] - cilova_pozice[0])):
        if (aktualni_pozice[0] + i, aktualni_pozice[1] + i) in obsazene_pozice:
            return False
        elif (aktualni_pozice[0] + i, aktualni_pozice[1] - i) in obsazene_pozice:
            return False
        elif (aktualni_pozice[0] - i, aktualni_pozice[1] + i) in obsazene_pozice:
            return False
        elif (aktualni_pozice[0] - i, aktualni_pozice[1] - i) in obsazene_pozice:
            return False
    return True


def je_tah_mozny_vez(cilova_pozice, aktualni_pozice, obsazene_pozice):
    if aktualni_pozice[0] != cilova_pozice[0] and aktualni_pozice[1] != cilova_pozice[1]:
        return False
    if aktualni_pozice[0] >= cilova_pozice[0]:
        position_range = range(cilova_pozice[0], aktualni_pozice[0])
    else:
        position_range = range(aktualni_pozice[0], cilova_pozice[0])
    for i in position_range:
        if (i, aktualni_pozice[1]) in obsazene_pozice:
            return False
    if aktualni_pozice[1] >= cilova_pozice[1]:
        position_range = range(cilova_pozice[1], aktualni_pozice[1])
    else:
        position_range = range(aktualni_pozice[1], cilova_pozice[1])
    for i in position_range:
        if (aktualni_pozice[0], i) in obsazene_pozice:
            return False
    return True


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.
    """
    if cilova_pozice[0] not in range(1, 9) or cilova_pozice[1] not in range(1, 9):
        return False

    if cilova_pozice in obsazene_pozice:
        return False
    
    aktualni_pozice = figurka["pozice"]
    # pro vez
    bez_sebe = []
    for pole in obsazene_pozice:
        if pole != aktualni_pozice:
            bez_sebe.append(pole)

    # pro strelec: jeden smer
    #вправо вверх по диагонали
    akt_to_cil_radek = cilova_pozice[0] - aktualni_pozice[0]
    akt_to_cil_sloupec = cilova_pozice[1] - aktualni_pozice[1]

    obsazene_strelec = []

    if abs(akt_to_cil_radek) == abs(akt_to_cil_sloupec) and akt_to_cil_radek != 0:
        for i in range(1, abs(akt_to_cil_radek)):
            radek = aktualni_pozice[0]
            sloupec = aktualni_pozice[1]

            if akt_to_cil_radek > 0:
                radek = radek + i
            else:
                radek = radek - i

            if akt_to_cil_sloupec > 0:
                sloupec = sloupec + i
            else:
                sloupec = sloupec - i

            pole = (radek, sloupec)

            if pole in obsazene_pozice:
                obsazene_strelec.append(pole)

    if figurka["typ"] == "pěšec":
        return je_tah_mozny_pesec(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "jezdec":
        return je_tah_mozny_jezdec(cilova_pozice, aktualni_pozice, obsazene_pozice)
    elif figurka["typ"] == "věž":
        return je_tah_mozny_vez(cilova_pozice, aktualni_pozice, bez_sebe)
    elif figurka["typ"] == "střelec":
        return je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_strelec)
    elif figurka["typ"] == "dáma":
        if je_tah_mozny_vez(cilova_pozice, aktualni_pozice, bez_sebe) or je_tah_mozny_strelec(cilova_pozice, aktualni_pozice, obsazene_strelec):
            return True
    elif figurka["typ"] == "král":
        if aktualni_pozice != cilova_pozice and abs(aktualni_pozice[0] - cilova_pozice[0]) <= 1 and abs(aktualni_pozice[1] - cilova_pozice[1]) <= 1:
            return True
    # Implementace pravidel pohybu pro různé figury zde.
    return False


if __name__ == "__main__":
    # my tests:
    # vez = {"typ": "věž", "pozice": (5, 3)}
    # obsazene_test = {(5, 3)}
    # print(je_tah_mozny(vez, (5, 6), obsazene_test)) # True
    # print()
    # strelec_test = {"typ": "střelec", "pozice": (4, 4)}
    # obsazene_test = {(4, 4), (3, 3)}
    # print(je_tah_mozny(strelec_test, (6, 6), obsazene_test)) # True
    # print()
    # pesec = {"typ": "pěšec", "pozice": (2, 4)}
    # print(je_tah_mozny(pesec, (3, 4), {(2, 4)})) # True
    # print(je_tah_mozny(pesec, (4, 4), {(2, 4)}))# True
    # print(je_tah_mozny(pesec, (5, 4), {(2, 4)}))# False
    # print(je_tah_mozny(pesec, (1, 4), {(2, 4)})) # False
    # print(je_tah_mozny(pesec, (3, 5), {(2, 4)}))# False
    # print(je_tah_mozny(pesec, (3, 4), {(2, 4), (3, 4)}))# False
    # print(je_tah_mozny(pesec, (4, 4), {(2, 4), (3, 4)}))# False
    # print()
    # jezdec = {"typ": "jezdec", "pozice": (4, 4)}
    # print(je_tah_mozny(jezdec, (6, 5), {(4, 4)}))# True
    # print(je_tah_mozny(jezdec, (3, 6), {(4, 4)}))# True
    # print(je_tah_mozny(jezdec, (6, 4), {(4, 4)}))# False
    # print(je_tah_mozny(jezdec, (5, 5), {(4, 4)}))# False
    # print(je_tah_mozny(jezdec, (9, 5), {(4, 4)}))# False
    # print()
    # strelec = {"typ": "střelec", "pozice": (4, 4)}
    # print(je_tah_mozny(strelec, (6, 6), {(4, 4)}))# True
    # print(je_tah_mozny(strelec, (2, 2), {(4, 4)}))# True
    # print(je_tah_mozny(strelec, (4, 7), {(4, 4)}))# False
    # print(je_tah_mozny(strelec, (7, 4), {(4, 4)}))# False
    # print(je_tah_mozny(strelec, (7, 7), {(4, 4), (5, 5)}))# False
    # print(je_tah_mozny(strelec, (9, 9), {(4, 4)}))  # False
    # print(je_tah_mozny(strelec, (7, 7), {(4, 4), (3, 3)}))  # True
    # print()
    # vez = {"typ": "věž", "pozice": (4, 4)}
    # print(je_tah_mozny(vez, (9, 4), {(4, 4)})) # False
    # print(je_tah_mozny(vez, (4, 6), {(4, 4), (4, 6)}))# False
    # print(je_tah_mozny(vez, (0, 4), {(4, 4)}))# False
    # print(je_tah_mozny(vez, (4, 8), {(4, 4)})) # True
    # print(je_tah_mozny(vez, (8, 4), {(4, 4)}))# True
    # print(je_tah_mozny(vez, (6, 6), {(4, 4)}))# False
    # print(je_tah_mozny(vez, (4, 8), {(4, 4), (4, 6)}))# False
    # print(je_tah_mozny(vez, (9, 9), {(4, 4)}))# False
    # print(je_tah_mozny(vez, (1, 4), {(4, 4), (5,4)}))# True
    # print()
    # dama = {"typ": "dáma", "pozice": (4, 4)}
    # print(je_tah_mozny(dama, (4, 8), {(4, 4)})) # True
    # print(je_tah_mozny(dama, (8, 4), {(4, 4)})) # True
    # print(je_tah_mozny(dama, (7, 7), {(4, 4)}))# True
    # print(je_tah_mozny(dama, (6, 5), {(4, 4)}))# False
    # print(je_tah_mozny(dama, (7, 7), {(4, 4), (5, 5)}))# False
    # print(je_tah_mozny(dama, (9, 9), {(4, 4)}))# False
    # print()
    # kral = {"typ": "král", "pozice": (4, 4)}
    # print(je_tah_mozny(kral, (4, 5), {(4, 4)})) # True
    # print(je_tah_mozny(kral, (5, 5), {(4, 4)})) # True
    # print(je_tah_mozny(kral, (6, 4), {(4, 4)})) # False
    # print(je_tah_mozny(kral, (4, 4), {(4, 4)}))# False
    # kral = {"typ": "král", "pozice": (1, 4)}
    # print(je_tah_mozny(kral, (0, 4), {(4, 4)}))# False

    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # True, při prvním tahu, může pěšec jít o 2 pole dopředu
    print(je_tah_mozny(pesec, (5, 2), obsazene_pozice))  # False, protože pěšec se nemůže hýbat o tři pole vpřed (pokud jeho výchozí pozice není v prvním řádku)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False, protože pěšec nemůže couvat
    print()
    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False, jezdec se pohybuje ve tvaru písmene L (2 pozice jedním směrem, 1 pozice druhým směrem)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False, tato pozice je obsazená jinou figurou
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False, je to pozice mimo šachovnici
    print()
    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False, dámě v cestě stojí jiná figura
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
    print()
    print(je_tah_mozny(strelec, (1, 8), obsazene_pozice))  # True