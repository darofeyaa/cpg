def sude_nebo_liche(cislo):
    """
    Upravte funkci tak, aby vypisovala, zda je cislo sude nebo liche
    """
    
    if cislo % 2 == 0 and cislo != 0:
        print(f"Cislo {cislo} je sudé")
    elif cislo == 0:
        print(f"Cislo {cislo} je nula")
    else:
        print(f"Cislo {cislo} je liché")


if __name__ == "__main__":
    sude_nebo_liche(5)
    sude_nebo_liche(1000000)
