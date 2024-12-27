lista = [1,2,3,4,5]
for elemento in lista:
    print(elemento)

tupla = (1,2,3,4,5)
for elemento in tupla:
    print(elemento)

pessoa = {"nome": "joão", "idade": 30, "cidade": "São Paulo"}
print("For utilizando dicionario - chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionario - valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utiznado items")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

#range
print(list(range(0,10)))

print("\nFor range()")
for numero in range(20):
    print("Número:",numero)