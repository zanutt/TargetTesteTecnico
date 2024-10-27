#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

entrada = "Bom dia target, serei um ótimo estagiario."
invertido = ""

for i in range (len(entrada) -1, -1, -1):
    invertido += entrada[i]

print(invertido)
