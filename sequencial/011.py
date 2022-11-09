n1 = int(input('Informe um numero interiro: '))
n2 = int(input('Informe outro numero  interiro: '))
n3 = int(input('Informe um numero real: '))

#a = o produto do dobro do primeiro com a  metade do segundo
d_n1 = (n1*2)
m_n2 = (n2 / 2)
soma1 = (d_n1 + m_n2)
#print (soma1)

#b = a soma do tripo do primeiro com o terceiro
t_n1 = (n1*3)
soma2= (t_n1 + n3)
#print(soma2)
    
#c = o terceiro elevado ao cubo (x³) 
cubo = (n3*n3*n3)
#print(cubo)
    
print ('''a = o produto do dobro do primeiro com a  metade do segundo é: {}.\n
b = a soma do tripo do primeiro com o terceiro é: {}. \n
c = o terceiro elevado ao cubo (x³) é: {}'''.format(soma1, soma2, cubo))
