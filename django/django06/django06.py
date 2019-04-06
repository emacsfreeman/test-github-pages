# Booleans
print(True and True)
print(True and False)
print(False and False)

print(True or True)
print(True or False)
print(False or False)

# Tuples
monTuple = (1, 2, 3)
print(monTuple)
print(monTuple[0])


# Sets
x = set()
x.add(1)
x.add(2)
print(x)
s = {1, 1, 1, 1, 2, 2, 2, 3, 3, 3}
print(s)

# Défi 1
djang = "Django"
# Afficher o, g, n, a, D
for i in range(len(djang)):
    print(djang[-i-1], end=" ")
print("")

# puis go, Dja, ognajD
print(djang[-2] + djang[-1])
print(djang[:3])
for i in range(len(djang)):
    print(djang[-1-i], end="")
print("")

# Défi 2
liste = [1, 2, [3, 4, 'salut']]
# remplacer 'salut' par 'ciao'
print(liste)
liste[2][2] = 'ciao'

# Défi 3
# Utiliser les clés et indices
# pour récupérer le 'salut' de
# chacun des dictionnaires
d1 = {'simple_key': 'salut'}
salut = d1['simple_key']
print(salut)

d2 = {'k1':{'k2':'salut'}}
salut = d2['k1']['k2']
print(salut)

d3 = {'k1':[{'nest_key':['this is deep', ['salut']]}]}
salut = d3['k1'][0]['nest_key'][1][0]
print(salut)

# Défi 4
mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3]
# utiliser set pour trouver les valeurs uniques
myset = set(mylist)
print(myset)

# Défi 5
valeur = 5028.02
btc = 'Bitcoin'
# utiliser la méthode format pour obtenir
"Le Bitcoin a une valeur de 5028.02 dollars US"
print("Le {y} a une valeur de {x} dollars US".format(x=btc, y=valeur))
