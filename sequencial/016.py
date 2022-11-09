metros = float(input('Digite o valor da área em metros quadrados: '))
um_litro = 1
tres_metros = 3
x = 1


#meio pelos extremos

p1 = (um_litro*metros)
p2 = (x*tres_metros)
p3 = (p1/p2)
print (f'o valor de litros que o cliente irá precisar é de {p3:0.2f}L')

#condicional
if p3 <= 18.9:
    print(f'para pintar {metros}m² será necessário uma lata de 18L, o valor a ser pago é de R$80.00')
elif p3 >= 19 and p3 <= 36.9:
    print(f'para pintar {metros}m² será necessário duas latas de 18L, o valor a ser pago é de R$160.00')
elif p3 >= 37 and p3 <= 54.9:
    print(f'para pintar {metros}m² será necessário três latas de 18L, o valor a ser pago é de R$240.00')
else:
    print('complementar')

