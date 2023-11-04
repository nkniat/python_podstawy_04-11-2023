letters_1 = {'a', 'b', 'c'}
letters_2 = {'b', 'c', 'd', 'e'}

# suma >> |
print("Suma zbiorów 1 i 2", letters_1.union(letters_2))

# czesc wspolna >> &
print("Czesc wspolna zbiorów 1 i 2: ", letters_1.intersection(letters_2))

# roznica 1 - 2 >> -
print("To, co jest w zbiorze 1, ale bez zbioru 2: ", letters_1.difference(letters_2))

# roznica symetryczna >> ^
print("Odwrotnosc czesci wspolnej to: ", letters_1.symmetric_difference(letters_2))
