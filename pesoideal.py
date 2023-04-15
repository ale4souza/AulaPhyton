sexo = input("Você é homem ou mulher? ")
alt = float(input('Qual a sua altura: '))

if sexo == "homem":
    peso = alt-58
    print("Seu peso ideal é: ", peso)
    
elif sexo == "mulher":
    peso = alt-44.7
    print("Seu peso ideal é: ", peso)
    
else:
    print("Favor informar homem ou mulher: ")