pituus = float(input("kuhan pituus"))

if pituus <37:

    # Kuha on alamittainen. Lasketaan kuinka paljon.
    alamittaisuus = 37 - pituus
    print(f"kalasi on {alamittaisuus}cm liian lyhyt!")

else:
    print("voit syödä kalan")
