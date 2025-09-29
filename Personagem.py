#especie = "humano"
    #def __new__(cls, nome):
        #print(cls)
        #return super().__new__(cls)
    #def __init__(self, nome):
        #self.nome = nome

#p1 = Pessoa("Maria")
#print(p1.nome)
#print(Pessoa.especie)


class Personagem:
    def __init__(self, nome):
        self._nome = nome
        self._hp = 100
        
    def get_nome(self):
        return self._nome
        
    def set_nome(self, novo_nome):
        self._nome = novo_nome
    
    def get_hp(self):
            return self._hp
    
    def sofrer_dano(self, valor):
        if valor > 0:
            self._hp -= valor
            if self._hp < 1:
                self._hp = 1
    
    def curar(self, valor):
        if valor > 0:
            self._hp += valor
            if self._hp > 100:
                self._hp = 100
    
personagem = Personagem("Herói")
print("Nome: ",
personagem.get_nome())

print("Hp inicial: ",
personagem.get_hp())

personagem.sofrer_dano(30)
print("Hp após dano: ",
personagem.get_hp())

personagem.curar(50)
print("Hp após cura: ",
personagem.get_hp())

personagem.set_nome("João")
print("Novo nome: ",
personagem.get_nome())