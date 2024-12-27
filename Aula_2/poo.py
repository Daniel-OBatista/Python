#programação orientada a objetos (Instancias de classes)

class pessoa:
    def __init__(self,nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

#objetos
pessoa1 = pessoa("Alice",30)
mensagem = pessoa1.saudacao()
print(mensagem)

pessoa2 = pessoa("Daniel",30)
mensagem = pessoa2.saudacao()
print(mensagem)