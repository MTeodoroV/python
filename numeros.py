from itertools import permutations

x = input("Digite o primeiro valor: ")
y = input("Digite o segundo valor: ")
z = input("Digite o terceiro numero: ")


count = 0

caracteres = [x, y, z]
for subset in permutations(caracteres, 3):
    print(subset)
    count = count +1
print(count)
