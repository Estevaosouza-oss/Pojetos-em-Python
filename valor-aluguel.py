diasRodados = int(input('Quantos dias voce Ficou com o Carro : '))
kmRodado = int(input("Quantos KM Voce Rodou com o Carro : "))
diaria = diasRodados * 60
kmaPagar = kmRodado * 0.15
valoraPagar = diaria + kmaPagar

print('Voce Ficou ' +str(diasRodados)+ ' Dias com o Carro')
print('Voce Rodou'+str(kmRodado)+'Km com o Carro')
print('O valor da diaria é R$60 e R$0,15 por Km Rodado')
print('Voce Tera que Pagar R${:.2f} Pela Diara e R${:.2f} Pelos Km rodados'.format(diaria, kmaPagar))
print('Ficando um Total de R${:.2f} a Empresa de Locação do Veiculo'.format(valoraPagar))
