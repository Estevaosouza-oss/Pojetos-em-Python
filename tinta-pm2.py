print('|===========Seja Bem Vindo===========|')
print('|  Nesse Programa mostraremos quanto |')
print('| de Tinta é necessario para pintar  |')
print('|        Um determinado M² de        |')
print('|             Uma Parede             |')
print('|             Vamos lá               |')
print('|====================================|')
l = int(input('| Me Diga a Largura da Parede: '))
a = int(input('| Me diga agora a Altura da Parede: '))
t = int(input('| Quantos M² sua Tinta Rende: |'))
mq = l*a
lt = mq/t
print('|======================================|')
print('|     Voce tem uma Parede com {} M²    |'.format(mq))
print('|    Cada Litro de Tinta Rende {} M²   |'.format(t))
print('| Voce precisara de {} Litros de tinta |'.format(lt))
print('|         Para Pintar sua parede       |')
print('|======================================|')
print('         OBRIGADO POR PARTICIPAR        ')