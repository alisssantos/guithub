cobertura_tinta = 3
capacidade_lata = 18
preco_lata = 80.0

tamanho_area = float(input('Digite o tamanho da area a ser pintada em m²: '))
litros = (tamanho_area / cobertura_tinta)
latas_inteiras = int(litros/capacidade_lata)
if(litros%capacidade_lata != 0):
    latas_inteiras += 1

valor_total = (latas_inteiras * preco_lata)

print(f' quantidade de litros de tinta necessários: {litros},\n quantidade de latas de tinta necessárias: {latas_inteiras},\n Valor total da compra: {valor_total}.')
