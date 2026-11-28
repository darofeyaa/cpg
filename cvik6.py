class Auto:
    def __init__(self, znacka, model, barva):
        self.znacka = znacka
        self.model = model
        self.barva = barva

    def vrat_popis(self):
        return f"Auto: {self.znacka} {self.model} {self.barva}"

if __name__ == '__main__':
    a1= Auto("t","c","z")
    a2= Auto("s","f","c")

    print(a1.model)
    print(a2.model)
    print(a1.vrat_popis())
    print(a2.vrat_popis())
    print(Auto.vrat_popis(a1))
    print(Auto.vrat_popis(a2))
