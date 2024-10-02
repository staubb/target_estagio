'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''

import json

# JSON como fonte de dados (pode ser carregado de um arquivo)
dados_faturamento = '''
{
  "faturamento_diario": [
    2000, 3500, 0, 2800, 1500, 1200, 0, 2100, 3300, 0,
    1000, 2500, 3600, 1900, 0, 2900, 2700, 3100, 0, 4100
  ]
}
'''

# Carregar dados do JSON
faturamento = json.loads(dados_faturamento)["faturamento_diario"]

# Filtrar os dias com faturamento diferente de 0
faturamento_valido = [dia for dia in faturamento if dia > 0]

# Cálculo do menor e maior valor de faturamento
menor_faturamento = min(faturamento_valido)
maior_faturamento = max(faturamento_valido)

# Cálculo da média mensal
media_mensal = sum(faturamento_valido) / len(faturamento_valido)

# Cálculo do número de dias com faturamento superior à média
dias_acima_da_media = len([dia for dia in faturamento_valido if dia > media_mensal])

# Exibição dos resultados
print(f"Menor faturamento do mês: {menor_faturamento}")
print(f"Maior faturamento do mês: {maior_faturamento}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

