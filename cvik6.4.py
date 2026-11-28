class ucet:
    def __init__(self, pocatecni_zustatek = 0):
        self.__zustatek = pocatecni_zustatek

    def __str__(self):
        return f"Účet s počátečním zůstatkem: {self.zustatek}"

    @property
    def zustatek(self):
        return self.__zustatek
    
    @zustatek.setter
    def zustatek(self, nova_hodnota):
        if nova_hodnota < 0:
            raise ValueError("Zůstatek nemůže být záporný.")
        self.__zustatek = nova_hodnota



    
if __name__ == "__main__":
    u = ucet(-1000)
    print(u)