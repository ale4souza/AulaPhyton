string = input("Informe a primeira palavra: ")
string1 = input("Informe a segunda palavra: ")


def verificar_anagrama(str1, str2):
    order_str1 = sorted(str1)
    order_str2 = sorted(str2)

    if (order_str1 == order_str2):
        print("É Anagrama")
    else:
        print("Não é Anagrama")


print(verificar_anagrama(string, string1))
