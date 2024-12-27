def saudacao(nome):
    print(f"Olá, {nome}!")

print("\nChamando a função:")
saudacao("Daniel")
saudacao("Aéveli")

def quadrado(numero):
    resultado = numero ** 2
    return resultado

print("\nChamando função quadrado")
resultado_quadrado = quadrado (10)
print("Resultado: ", resultado_quadrado)

def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

print("\nChamando a função soma:")
numero1 = 50
numero2 = 50
resultado_soma = soma (numero1, numero2)
print("A soma dos números %s + %s é: %s." % (numero1, numero2, resultado_soma))