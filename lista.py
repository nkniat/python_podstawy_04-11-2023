my_list = [1, 2, 3, 3, 'mama', 'tata']

# dodawanie do listy
my_list.append('babcia')
print(my_list)

my_list.extend([4, 5])
print(my_list)

my_list.insert(2, 2.5)
print(my_list)

# usuwanie z listy
my_list.remove('babcia')
print(my_list)

# uwuwa tylko pierwsze wysapienie elementu
my_list.remove(3)
print(my_list)

if 'mama' in my_list:
    my_list.remove('mama')

# ściąga ostatni element z listy i zwraca nam go
ostatni_element = my_list.pop()
print(ostatni_element)
print(my_list)

del my_list[0]
print(my_list)

del my_list[2:4]
print(my_list)

# usuwanie calej listy
# del my_list
# print(my_list)

# czyszczenie listy
my_list.clear()
print(my_list)

my_list2 = [5, 15, 2, 12, 4, 14, 0, -15, -5, -25]
print('Nieposortowana: ', my_list2)
my_list2.sort(reverse=True)
print('Posortowana: ', my_list2)

print("Element 0, ma index: ", my_list2.index(0))

my_list3 = ['natalia', 'ania', 'marek']
print(my_list3[0].upper())
print(my_list3)

