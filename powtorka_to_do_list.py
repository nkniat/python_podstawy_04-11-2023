# program, który wyświetla proste menu i dodaje do listy rzeczy do zrobienia
# użytkownik może usuwać zadania, wyświetlić zadania

# lista moze skladac sie z list - przy zadaniu mamy status zadania
todo_list = []

while True:
    print('TO DO LIST - Menu:')
    print('1. Dodaj zadanie ')
    print('2. Wyświetl zadania ')
    print('3. Usuń zadanie ')
    print('4. Koniec programu')

    choice = input("Wybierz opcję z menu ")

    if choice == '1':
        task = input("Jakie zadanie? ")
        todo_list.append(task)
    elif choice == '2':
        print("Tyle masz jeszcze do zrobienia: ", todo_list)
        # co zrobic, jesli lista jes pusta?
        # jak 'ładniej' wypisać elementy z listy?
    elif choice == '3':
        print("Na razie nie wiem, jak usuwać :( ")
        # jak usuwać elementy?
    elif choice == '4':
        break
