class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def escreve(self):
        print(self.nome, self.idade)
        
class Estudante(Pessoa):
    pass    

x = Estudante('Jo', 21)
x.escreve()