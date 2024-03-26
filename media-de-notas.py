nome=input('Digite seu Nome: ')
nota1 =float(input('Digite a Primeira Nota: '))
nota2 =float(input('Digite a Segunda nota: '))
nota3 =float(input('Digite a Terceira Nota: '))
nota4 =float(input('Digite a Quarta Nota: '))
nota5 =float(input('Digite a Quinta Nota: '))
pontuacao = nota1+nota2+nota3+nota4+nota5
media = pontuacao / 5

print('Olá, ' + nome )
print('As suas notas foram')
print(nota1)
print(nota2)
print(nota3)
print(nota4)
print(nota5)
print('Fazendo um total de ' + str(pontuacao) + 'Pontos')
print('E uma nota media de ' + str(media))