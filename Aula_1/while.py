print("While")
contador = 0
while contador < 6:
    print("Contagem:", contador)
    contador += 1

    print("Programa finalizado")

print("\n\nWhile Break")
contador = 0
while True:
    print("Contagem:", contador)
    contador += 1
    if contador == 5:
        break

    print("Programa finalizado break.")