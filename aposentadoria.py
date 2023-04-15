sexo = input('Informe o sexo: (M ou F):')

idade = int(input("Informe a idade: "))
contribuicao = int(
    input("Informe o tempo de contribuiçao contribuiçao, em anos: "))

if sexo == "M" or sexo == "m" and idade >= 65 and contribuicao >= 10:
    print("Aposentável")
elif sexo == "M" or sexo == "m" and idade >= 63 and contribuicao >= 15:
    print("Aposentável")
elif sexo == "F" or sexo == "f" and idade >= 63 and contribuicao >= 10:
    print("Aposentável")

elif sexo == "F" or sexo == "f" and idade >= 61 and contribuicao >= 15:
    print("Aposentável")
else:
    print("Não Aposentável")
