jednotky = ["","jeden","dva","tři","čtyři","pět","šest","sedm","osm","devět"]
jedenact_devatenact = [ " ", "jedenáct","dvanáct","třináct","čtrnáct","patnáct","šestnáct","sedmnáct","osmnáct","devatenáct"]
desitky = ["","deset","dvacet","třicet","čtyřicet","padesát","šedesát","sedmdesát","osmdesát","devadesát"]

def cislo_text(cislo):
    cislo = int(cislo)
    if cislo == 0:
        return "nula"

    if cislo < 0 or cislo > 100:
        return "error: a number greater than 100"

    if cislo == 100:
        return "sto"
    
    a = cislo // 10
    b = cislo % 10

    if 11 <= cislo <= 19:
            return jedenact_devatenact[b]

    if a == 0:
       return jednotky[b]
    elif b!=0:
       return desitky[a] + " " + jednotky[b]
    else:
        return desitky[a]
    
    # funkce zkonvertuje cislo do jeho textove reprezentace
    # napr: "25" -> "dvacet pět", omezte se na cisla od 0 do 100
    #return "dvacet pět"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)