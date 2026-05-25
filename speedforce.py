# aqui temos um codigo representando a força de aceleração de uma forma orientada a objetos.
class speedforce:
# abaixo temos uma função para reconhecer cada parâmetro dela mesma.
    def __init__(self, nome, eletricidade, cor_do_raio, poderes, usuario):
       self.nome = nome
       self.eletricidade = eletricidade
       self.poderes = poderes
       self.usuario = usuario
       self.cor_do_raio = cor_do_raio
#aqui temos um codigo representando a força de aceleração negativa de uma forma orientada a objetos.
class negative_speedforce(speedforce):
    def __init__(self, nome, eletricidade, cor_do_raio, poderes, usuario):
        super().__init__(nome, eletricidade, cor_do_raio, poderes, usuario)
        self._negatividade = []

# aqui atribuio que força_original é o objeto speedforce que tem seus parâmetros personalizados.
força_original = speedforce('F.A_original', "5000 volts", "laranja", "velocidade","Flash" )
# aqui atribuio que força_negativa é o objeto negative_speedforce que tem seus parâmetros personalizados.
força_negativa = negative_speedforce('F.A negativa', '5000 volts', 'vermelho', 'velocidade', 'flash reverso')
# temos abaixo uma serie de 'prints' para cada parâmetro.
print(força_original)
print(força_original.nome)
print(força_original.eletricidade)
print(força_original.poderes)
print(força_original.usuario)
print(força_original.cor_do_raio)
# temos abaixo uma serie de 'prints' para cada parâmetro.
print(força_negativa)
print(força_negativa.nome)
print(força_negativa.eletricidade)
print(força_negativa.poderes)
print(força_negativa.usuario)
print(força_negativa.cor_do_raio)
# esse é o fim do codigo
