'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

# String a ser invertida (pode ser fornecida pelo usuário ou pré-definida)
string_original = input(str("Digite uma string: "))

# Inicializar uma variável para armazenar a string invertida
string_invertida = ""

# Percorrer a string original de trás para frente e construir a nova string

for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

# Exibir a string invertida
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
