# imie = "Natalia"
# print(imie[::-1])

# lista ze slowami do sprawdzenia
lista_slow = ['mama', 'kajak', 'kaczka', 'axa', 'Ala ma kota']

for slowo in lista_slow:
    # odwracamy slowo za pomocom slicow
    slowo_od_konca = slowo[::-1]
    # sprawdzamy, czy dane slowo jest rowne slowu odwroconemu
    if slowo == slowo_od_konca:
        print("Słowo: ", slowo, " jest palindromem")
    else:
        print("Słowo: ", slowo, " nie jest palindromem")
