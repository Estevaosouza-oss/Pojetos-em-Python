from math import hypot
catetoOposto = int(input('Digite o Cateto Oposto : '))
catetoAdjacente = int(input('Digite o Cateto Adjacente : '))
hipotenusa = hypot(catetoOposto, catetoAdjacente)

print(' O Valor da Hipotenusa é {:.3f}'.format(hipotenusa))