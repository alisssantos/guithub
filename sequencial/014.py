limite = 50
excesso = 0
taxa_multa_kg = 4.00

peso = float(input('Digite o peso total dos peixes: '))

if peso > limite:
    excesso = (peso - limite)
    multa_pagar = (excesso * taxa_multa_kg)
    print (f'O peso do peixe é {peso:.2f},\n o excesso de peso foi de {excesso:.2f},\n a multa que deve ser paga é de {multa_pagar:.2f}.')
    
else (' O peso não ultrapassou o limite, não a multa a ser paga')


