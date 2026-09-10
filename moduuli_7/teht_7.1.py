kuukausien_vuodenajat = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

kuukausi = int(input("Anna kuukausi numeroina: "))

if 1 <= kuukausi <= 12:
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {kuukausien_vuodenajat[kuukausi - 1]}")
else:
    print("Virheellinen kuukausi. Anna luku väliltä 1-12.")