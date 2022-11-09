s_hora = float(input(' Qual seu sálario hora: '))
q_hora = float(input(' Quantas horas você trabalhou no mês: '))

s_bruto = (s_hora *q_hora)

renda = (s_bruto*0.11)
inss = (s_bruto*0.08)
sindicato = (s_bruto*0.05)
soma = (renda + inss+sindicato)
s_liquido= (s_bruto-soma)

print(f'''O salário hora informado foi {s_hora:.2f}

a quantidade de horas trabalhadas no mês foi {q_hora:.2f}

o salário bruto é {s_bruto:.2f}

debitado de Imposto de Renda é {renda:.2f}

debitado de inss é {inss:.2f}

debitado de sindicato é {sindicato:.2f}

O salário liquido a receber é de {s_liquido:.2f}''')
