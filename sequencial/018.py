tamanho = float(input('Informe o tamanho do arquivo para download (MB): '))
net = float(input('informe a velocidade da sua internet em (mb/s): '))

rs = (tamanho/(net/8))
conv = (rs/60)
      
print (f'O tempo necessário para baixar o arquivo será de {conv:.2f} minutos')
