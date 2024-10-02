'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
'''

def is_fibonacci(num):
    # Inicializando os dois primeiros números da sequência de Fibonacci
    fib1, fib2 = 0, 1

    # Caso o número informado seja 0 ou 1, já pertence à sequência
    if num == fib1 or num == fib2:
        return True

    # Gerando a sequência de Fibonacci e verificando se o número pertence
    while fib2 < num:
        fib1, fib2 = fib2, fib1 + fib2
        if fib2 == num:
            return True

    return False


# Número a ser verificado (pode ser alterado ou pode-se usar input para pedir ao usuário)
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
