import math
area = int(input('Informe a area a ser pintada em m²: '))

litros = ((area / 6 )* 1.1)
latas = math.ceil(litros / 18)
valor_lata = (latas * 80.0)
galao = math.ceil(litros / 3.6)
valor_galao = (galao * 25)

mix_latas = round(litros/18)
mixgaloes = round((litros - mix_latas * 18) / 3.6)

if (litros - (mix_latas * 18)%3.6 != 0):
    mixgaloes +=1
    total_mix = (mix_latas * 80) + (mixgaloes * 25)

print(f'se for comprar so latas de 18 litros você ira precisar de {latas:.2f} latas e ira custar R${valor_lata:.2f}\n se for comprar só galoes de 3.6 litros irá precisar de {galao:.2f} galão(ões) e irá custar RS {valor_galao:.2f}')
print(f'se desejar mesclar latas e galões para dar o que realmente precisar será necessário {mix_latas:.2f} latas(s) e {mixgaloes:.2f} galão(ões) e irá custar R$ {total_mix:.2f}')
