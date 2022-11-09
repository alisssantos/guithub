altura = float(input(f' Informe a sua altura e o sistema retornara o peso ideal para homem e para mulher: '))
calc_h = ((72.7*altura)-58)
calc_m = ((62.1*altura)-44.7)

print(f' A altura informada foi {altura:.2f}, o peso ideal para homem é {calc_h:.2f} e o peso ideal para mulher é {calc_m:.2f}')
