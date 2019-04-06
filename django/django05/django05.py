# Dictionaries

# strings as keys
office_number = {
    'pierre': 1234,
    'paul': 2341,
    'jack': 3412
}
print(office_number)
print("Pierre's office number is", office_number['pierre'])
office_number['arthur'] = 4132
print(office_number)

numbers as keys
rooms_assignation = {
    1:'Pierre',
    4:'Paul',
    2:'Jack',
    3:'Jean'
}
print(rooms_assignation)
print("Who is in room 1? It's", rooms_assignation[1])
print("Who is in room 4? It's", rooms_assignation[4])

# heterogeneous dictionary
wallet = {
    "key1": 123,
    'key2': 'value2',
    'key3': {
        '123': [1,2, 'truc'],
        'what': 'the fuck'
    }
}
print(wallet['key3']['123'][2].capitalize())
