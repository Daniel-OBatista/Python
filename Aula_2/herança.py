class animal:
    def __init__(self, nome) -> None:
        self.nome = nome

    def andar(self):
        print(f"O animal {self.nome} andou")

    def emitir_som(self):
        pass

class Cachorro(animal):
    def emitir_som(self):
        return "Au, au"
    
class Gato(animal):
    def emitir_som(self):
        return "Miau"
    
dog = Cachorro(nome="Rex")
cat =  Gato(nome="Felix")

print("Lista de poliformismo")
animais = [dog, cat]
for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")