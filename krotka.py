my_tuple = (1, 2, 3, 'mama', 'tata')
print("Typ elementu: ", my_tuple, "to ", type(my_tuple))

my_list = ['mama', 'tata', 'babcia']
print("Typ elementu: ", my_list, "to ", type(my_list))

my_tuple2 = tuple(my_list)
print("Typ elementu: ", my_tuple2, "to ", type(my_tuple2))

my_tuple3 = tuple("Natalia")
print("Typ elementu: ", my_tuple3, "to ", type(my_tuple3))

concatenated_tuple = my_tuple + my_tuple2
print("Typ elementu: ", concatenated_tuple, "to ", type(concatenated_tuple))

# liczenie elementów 'mama' w tupli concatenated_tuple
print(concatenated_tuple.count('mama'), 'razy wystapilo slowo mama')

# wypisanie wielokrotne
print(my_tuple * 10)

# tupla jednoelementowa
my_tuple4 = (1, )
print("Typ elementu: ", my_tuple4, "to ", type(my_tuple4))

# przypisywanie wielu wartości do wielu zmiennych w jendym kroku
a, b = 1, 2
print(a, b)

print("Dlugosc tupli: ", len(concatenated_tuple))

for element in concatenated_tuple:
    print(element)