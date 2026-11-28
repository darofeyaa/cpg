class osoba:
    def __init__(self, jmeno, vek):
        self.jmeno = self.uprav_imeno(jmeno)
        self.vek = vek

    def __str__(self):
        return f"Osoba: {self.jmeno} ma {self.vek} let"
    
    def vrat_popis(self):
        return f"Osoba: {self.jmeno} {self.vek}"
    
    def pridej_rok(self):
        self.vek += 1

    def uprav_imeno(self, jmeno):
        vysledek_jmeno =[]
        for part in jmeno.split():
            vysledek_jmeno.append(part.capitalize())
        return " ".join(vysledek_jmeno)

class student(osoba):
    def __init__(self, jmeno, vek, rocnik):
        super().__init__(jmeno, vek)
        self.rocnik = rocnik

    def __str__(self):
        return f"Student: {self.jmeno} ma {self.vek} let a je v {self.rocnik}. rocniku"
    
    def pridej_rok(self):
        super().pridej_rok()
        if self.rocnik < 5:
            self.rocnik += 1

class ucitel(osoba):
    def __init__(self, jmeno, vek, let_praxe):
        super().__init__(jmeno, vek)
        self.let_praxe = let_praxe

    def __str__(self):
        return f"Ucitel: {self.jmeno} ma {self.vek} let a ma {self.let_praxe} let zkusenosti"
    
    def pridej_rok(self):
            super().pridej_rok()
            self.let_praxe += 1


if __name__ == '__main__':
    osoby = [
        student("Petr", 19, 1),
        student("jana", 20, 2),
        ucitel("Karel", 40, 10), 
        ucitel("eva", 35, 5)
    ]
    for osoba in osoby:
        print(osoba)
        osoba.pridej_rok()
        print(osoba)    