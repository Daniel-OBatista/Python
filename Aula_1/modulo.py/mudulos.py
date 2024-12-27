print("Exmeplo de importação de modulo")
from math import sqrt

raiz_quadrada = int(sqrt(25))

print(raiz_quadrada)

print("\nCriação de módulo")
import meu_modulo

mensagem = meu_modulo.saudacao("Daniel")
resultado_dobro = meu_modulo.dobro(5)
print(mensagem)
print(f"o dobro de 5 é: {resultado_dobro}")