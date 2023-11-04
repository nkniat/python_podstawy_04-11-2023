"""
Napisać program, który pozwoli użytkownikowi:
1. dodać nowe definicje do słownika
2. szukać instniejacych definicji
3. usunąć wybraną przez niego definicję
"""

definicje = {}

while True:
    print('Mój interaktywny słownik - bez baz danych ')
    print('1. Dodaj definicje ')
    print('2. Wyświetl definicje ')
    print('3. Usuń definicje ')
    print('4. Koniec programu')

    choice = input("Wybierz opcję z menu ")

    if choice == '1':
        klucz = input("Podaj słowo, które będziesz definiować ")
        definicja = input("Podaj definicję tego słowa: ")
        definicje[klucz] = definicja
        print("Definicja dodana poprawnie")
    elif choice == '2':
        klucz = input("Czego szukasz? ")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Nie znam takiego słowa.")
    elif choice == '3':
        klucz = input("Co chcesz usunąć? ")
        if klucz in definicje:
            del definicje[klucz]
            print("Usunieto defnicje slowa: ", klucz)
        else:
            print("Nie znam takiego słowa.")
    elif choice == '4':
        break
