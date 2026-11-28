class Ucet:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.zustatek = 0

    def vlozit(self, castka):
        if castka > 0:
            self.zustatek += castka
        else:
            raise zaporna_castka("Castka k vlozeni musi byt kladna")

    def vybrat(self, castka):
        if castka < 0:
            raise zaporna_castka("Castka k vybrani musi byt kladna")
        if castka > 0 and castka <= self.zustatek:
            self.zustatek -= castka
            return True
        else:
            return False
        
        return castka
        
    def __str__(self):
        return f"Ucet: {self.jmeno} ma zustatek {self.zustatek}"

class zaporna_castka(Exception):
    pass
class nedostatecny_zustatek(Exception):
    pass

class sporici_ucet(Ucet):
    def __init__(self, jmeno, urok):
        super().__init__(jmeno)
        self.urok = urok

    def pripocitat_urok(self):
        self.zustatek += self.zustatek * self.urok / 100

    def __str__(self):
        return f"Sporici ucet: {self.jmeno} ma zustatek {self.zustatek} a urok {self.urok}%"
    
    def vybrat(self, castka):
        if castka < 0:
            raise zaporna_castka("Castka k vybrani musi byt kladna")
        if castka > 0 and castka <= self.zustatek:
            self.zustatek -= castka
            return True
        else:
            raise nedostatecny_zustatek("Nedostatečný zůstatek na účtu.")



if __name__ == '__main__':
    u1 = Ucet("standart")
    u1.vlozit(100)
    print ("vybrano:", u1.vybrat(100))
    print(u1)
    u2 = sporici_ucet("sporici", 1.3)
    u2.vlozit(100)
    print("vybrano:", u2.vybrat(100))
    print(u2)
