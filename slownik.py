my_dict = {
    'Name': 'Natalia',
    'Age': 36,
    'Height': 170.5
}

print(my_dict['Name'])

my_dict_num = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: ['four', 'cztery']
}

print(my_dict_num[4])

my_dict_num.update({0: 'zero'})
print(my_dict_num)

my_dict_cars = {
    ('Toyota', 'Aygo'): 'KR12345',
    ('Toyota', 'Yaris'): 'KR12345'
}
print(my_dict_cars)

print("Dlugosc slownika: ", len(my_dict_num))

print("Wartosc pod kluczem Name: ", my_dict.get('Name'))

print('Lista wszystkich kluczy:', my_dict.keys())
print('Lista wszystkich wartosci: ', my_dict.values())
print('Lista wszystkich elementów:', my_dict.items())

for key in my_dict:
    print('Klucz: ', key)

for value in my_dict.values():
    print('Wartość: ', value)

for key, value in my_dict.items():
    print('Dla klucza: ', key, 'masz wartosc: ', value)
