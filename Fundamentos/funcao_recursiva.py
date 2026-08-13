def factorial(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num * factorial(num - 1)
number = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {number} é {factorial(number)}")