class Komponent:
    def __init__(self, nazwa, czas_produkcji, ilosc_poczatkowa, ilosc_na_produkt):
        self.nazwa = nazwa
        self.czas_produkcji = czas_produkcji
        self.ilosc_poczatkowa = ilosc_poczatkowa
        self.ilosc_na_produkt = ilosc_na_produkt

class Produkt:
    def __init__(self, nazwa, czas_produkcji, ilosc_na_dzien, komponenty):
        self.nazwa = nazwa
        self.czas_produkcji = czas_produkcji
        self.ilosc_na_dzien = ilosc_na_dzien
        self.komponenty = komponenty

def oblicz_zapotrzebowanie(produkty, dzien):
    zapotrzebowanie = {}
    for produkt in produkty:
        zapotrzebowanie[produkt.nazwa] = produkt.ilosc_na_dzien * dzien

        for komponent in produkt.komponenty:
            if komponent.nazwa not in zapotrzebowanie:
                zapotrzebowanie[komponent.nazwa] = 0

            zapotrzebowanie[komponent.nazwa] += produkt.ilosc_na_dzien * komponent.ilosc_na_produkt

    return zapotrzebowanie

def generuj_raport(zapotrzebowanie):
    print("Raport zapotrzebowania:")
    for nazwa, ilosc in zapotrzebowanie.items():
        print(f"{nazwa}: {ilosc}")

# Przykład użycia

komponent1 = Komponent("Śrubka", 1, 100, 2)
komponent2 = Komponent("Mutterka", 2, 50, 1)

produkt1 = Produkt("Krzesło", 5, 10, [komponent1, komponent2])

zapotrzebowanie = oblicz_zapotrzebowanie([produkt1], 5)
generuj_raport(zapotrzebowanie)