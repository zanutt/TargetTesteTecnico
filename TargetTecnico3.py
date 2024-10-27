#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def carregar_dados_faturamento(file_path):
    with open(file_path, 'r') as arquivo:
        return json.load(arquivo)

def calcular_faturamento(dados_faturamento):
    faturamento_valido = [dia['faturamento'] for dia in dados_faturamento if dia['faturamento'] > 0]
    if not faturamento_valido:
        return None, None, 0
    
    menor_faturamento = min(faturamento_valido)
    maior_faturamento = max(faturamento_valido)
    media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

    dias_maior_media = sum(1 for faturamento in faturamento_valido if faturamento > media_faturamento)
    return menor_faturamento, maior_faturamento, dias_maior_media

dados_faturamento = carregar_dados_faturamento('faturamento.json')
faturas = calcular_faturamento(dados_faturamento)
print(f"O Menor faturamento é {faturas[0]}, o maior faturamento é {faturas[1]} e dias acima da media são {faturas[2]}")



