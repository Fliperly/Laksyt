def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = float(input("Anna gallonamäärä: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print(f"{litrat} litraa")

    gallonat = float(input("Anna gallonamäärä: "))