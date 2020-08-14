tp = 12345, 54321, 'hello!'
print(tp)


def test(a):
    return [a,10,15,16]

x,y,z,b =test(5)
print(x)
print(y)
print(z)

student = ("Tunde", 70)
student2 = ("Abel", 70)

# Dictionaries
dico = dict([
    student,
    student2
])


print(dico)

banana = ("banana", 4)
apple = ("apple", 2)
orange = ("orange", 3)

fruits = dict([
    banana,
    apple,
    orange
])

print(fruits)

total=0

for fruit, qty in fruits.items():
    total = total + qty
print(total)