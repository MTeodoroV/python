num1 = int(input("Digite o primeiro nuemro:"))
num2 = int(input("Digite o segundo numero:"))

if num1 > num2:
    maior = num1
else:
    maior = num2
while True:
    if maior % num1 == 0 and maior % num2 == 0:
        print(maior)
        break
    else:
        maior += 1
    