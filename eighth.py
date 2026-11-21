def bin_to_dec(binarni_cislo):
    # funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    # 111 -> 7
    # "101" -> 5
    binarni_cislo = str(binarni_cislo)
    dec_value = 0
    for digit in binarni_cislo:
        dec_value = dec_value * 2 + int(digit)
    return dec_value


def test_bin_to_dec():
    print(bin_to_dec("0"))
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128