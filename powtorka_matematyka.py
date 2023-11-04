# Pobierz od użytkownika listę liczb
# i policz średnią z tych liczbe
# wyświetl wynik (średnią)

# rozwiazanie bez listy
# result = 0
# x = int(input("Ile liczb chcesz wprowadzić?"))
#
# for i in range(x):
#     liczba_podana = float(input("Podaj liczbę:"))
#     result = result + liczba_podana
#
# result = int(result / x)
#
# print("Średnia z podanych liczb to", result)


# rozwiazanie za pomoca listy
numbers = []
while True:
    num = int(input("Podaj liczbę:"))
    numbers.append(num)

    addmore = input("Chcesz podać kolejną liczbę?(T/N)")
    if addmore == 'N':
        break

total = 0

for number in numbers:
    total += number

average = total / len(numbers)
print("Srednia to ", average)
