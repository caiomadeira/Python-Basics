"""
Escreva uma função recursiva que receba um número e retorne-o convertido para o formato string. (o mesmo que é feito pela função str)
"""


# n % 10 --> sempre é o ultimo digito do numero
# n // 10 --> o numero sem o ultimo digito

def convertString(n):
    num1 = (n % 10)
    num = num1
    convertString(num1)



# callback
print(convertString(n=134))
