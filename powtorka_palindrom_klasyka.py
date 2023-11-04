# lista ze slowami do sprawdzenia
lista_slow = ['mata', 'kajak', 'kaczka', 'axa']

for slowo in lista_slow:

    # liczba iteracji dla danego slowa w kazdym przebiegu petli po liscie
    liczba_iteracji = len(slowo) // 2

    # flaga na sprawdzaenie, czy slowo jest palindromem
    flaga_czy_palindrom = True

    print('Sprawdzam slowo: ', slowo)

    for i in range(liczba_iteracji):
        if slowo[i] != slowo[-1 - i]:
            print('Slowo ', slowo, 'nie jest palindromem')
            flaga_czy_palindrom = False
            break
        else:
            print('Literka', slowo[i], ' jest taka sama')

    if flaga_czy_palindrom:
        print('Slowo', slowo, 'jest palindromem')