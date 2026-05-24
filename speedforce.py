# aqui temos um codigo representando a força de aceleração de uma forma orientada a objetos.
class speedforce:
# abaixo temos uma função para reconhecer cada parâmetro dela mesma.
    def __init__(self, nome, eletricidade, poderes, usuario):
       self.nome = nome
       self.funcionarios = eletricidade
       self.produtos = poderes
       self.usuario = usuario
# aqui atribuio que força_original é o objeto speedforce que tem seus parâmetros personalizados.
força_original = speedforce('F.A_original', "laranja", "velocidade","bryanwesley" )
# temos abaixo uma serie de 'prints' para cada parâmetro.
print(força_original)
print(força_original.nome)
print(força_original.eletricidade)
print(força_original.poderes)
print(força_original.usuario)
# esse é o fim do codigo
