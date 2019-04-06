# Lists
maListe = [1, 2, 3]
print(maListe)
maListe = ['hello', 3.5, True, maListe]
print(maListe)

maListe = ['a', 'b', 'c', 1, 2, 3]
print(maListe)
print(maListe[0])
print(maListe[-1])
print(maListe[3:5])

print("avant")
print(maListe)
maListe[0] = "New element"
print("après")
print(maListe)

maListe.append('new item at the end')
print(maListe)

maListe.append([4, 5, 6])
print(maListe)

maListe.extend([4, 5, 6])
print(maListe)

item = maListe.pop()
print(maListe)
print(item)

maListe.reverse()
print(maListe)

maListe = [4, 5, 3, 1, 2]
print("avant le tri")
print(maListe)
maListe.sort()
print("après le tri")
print(maListe)

maListe.append(['a', 'b', 'c'])
print(maListe)
print(maListe[5][1])

matrix = [[1,2,3],[4,5,6],[7,8,9]]

first_col = [row[0] for row in matrix]

print(first_col)
