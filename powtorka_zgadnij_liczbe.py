szukanaLiczba = 13
zgadywanaLiczba = 0

while zgadywanaLiczba != szukanaLiczba:
    zgadywanaLiczba = int(input("Jaką liczbę mam na myśli? "))

    if zgadywanaLiczba == szukanaLiczba:
        print("Zgadłeś!")
    elif zgadywanaLiczba > szukanaLiczba:
        print("Liczba jest za duża")
        print("Różnica to: ", zgadywanaLiczba - szukanaLiczba)
    elif zgadywanaLiczba < szukanaLiczba:
        print("Zgadywana liczba jest za mała")
