my_set = {1, 2, 'A', 'B', 'a', 'b', True, False}
print(my_set)

my_set2 = set([1, 2, 3, 3, 'mama', 'tata'])
print(my_set2)

# elementy w zbiorze nie są poindexowane
# print(my_set[0]) #  >> error

if 'mama' in my_set2:
    print("Tak, jest")

my_set2.update(my_set)
my_set2.add(6)
print(my_set2)

my_set2.remove('tata')
print(my_set2)

