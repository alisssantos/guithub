v_hora = float(input('Quanto você ganha por hora? '))
q_hora =  int(input('Informe a quantidade de horas trabalhadas no mês "horas sem casa decimal ex 0.0": '))
mult = (v_hora * q_hora)
print('O valor do seu sálario hora é {}, o total de horas trabalhadas no mês é {}, o valor referente ao seu salário mensal é de {}'.format(v_hora, q_hora, mult))
