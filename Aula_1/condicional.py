#if, elif, else

#IF
idade = int(input("Digite sua idade:"))

if idade >= 18:
    print("Maior de idade.")
elif idade >= 12:
    print("Você é um adolescente.")
else:
    print("Menor de idade.")

mensagem = "Pode tirar CNH" if idade >= 18 else "Voce nao pode tirar CNH"

print(mensagem)