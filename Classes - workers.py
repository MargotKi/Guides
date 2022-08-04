class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek


    def osoba1(self):
        print(self.imie)

    def osoba2(self):
        print(self.nazwisko)

    def osoba3(self):
        print(self.wiek)


def main():

    imiona = Osoba("Arek", "Tadeusz", "Kacper")
    nazwiska = Osoba("Grzechnik", "Kochaniec", "Stępień")
    wieki = Osoba("84", "27", "19")


#osoba 1
    imiona.osoba1(), nazwiska.osoba1(), wieki.osoba1()
#osoba 2
    imiona.osoba2(), nazwiska.osoba2(), wieki.osoba2()
#osoba 3
    imiona.osoba3(), nazwiska.osoba3(), wieki.osoba3()


main()