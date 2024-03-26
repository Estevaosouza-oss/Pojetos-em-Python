metros =float(input("Digite uma Medida em Metros: "))
cm = metros * 100
mm = cm * 10

print('Voce Escreveu ' + str(metros)+ 'Metros')
print('{}M Em Centrimetros São {}cm'.format(metros, int(cm)))
print('{}M em Milimetros são {}mm'.format(metros, int(mm)))