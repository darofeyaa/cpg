def convarsion(value):
   return int(value)

def division(a,b):
   a = convarsion(a)
   b = convarsion(b)
   return a / b




if __name__ == '__main__':
    # přidej try-except blok, odchyť obecnou vyjímku Exception a vypiš ji
    try:
        data = ["10", "5", "1"]
        numbers = []

        for value in data:
            try:
                nuber = int(value) + 1
            except ValueError:
                print("jen cislo")
                continue
            except ZeroDivisionError:
                print("nelze 0")
                continue
            numbers.append(nuber)

        print(numbers)
    except Exception as exception:
        print(exception)

   
   