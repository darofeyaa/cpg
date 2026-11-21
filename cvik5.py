from jakard import jaccardova_vzdalenost_mnozin



if __name__ == "__main__":
    data1 = ["https://www.seznam.cz", "https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz", "https://www.google.com"]
    data2 = ["https://www.seznam.cz", "https://www.google.com", "https://www.novinky.cz", "https://www.idnes.cz", "https://www.zpravy.cz", "https://www.tn.cz"]
    data3 = ["https://www.jcu.cz", "https://www.czu.cz", "https://www.cvut.cz", "https://www.uk.cz"]

    print(jaccardova_vzdalenost_mnozin(data1, data2))
    print(jaccardova_vzdalenost_mnozin(data2, data3))
    print(jaccardova_vzdalenost_mnozin(data1, data3))