import json

class osoba:
    def __init__(self, jmeno, prijmeni, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek

    def __str__(self):
        return f"Jméno: {self.jmeno}, Příjmení: {self.prijmeni}, Věk: {self.vek}"

if __name__ == "__main__":
    # Načtení dat ze souboru osoby.json
    with open("osoby.json", "r") as file:
        data = json.load(file)

    print("Načtená data ze souboru osoby.json:")
    for item in data:
        print(f"Jméno: {item['jmeno']}, Příjmení: {item['prijmeni']}, Věk: {item['vek']}") 