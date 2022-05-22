alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = alt*lar
tinta = area/2
print('Para pintar um parede {}m x {}m = {}m² vai precisar de {} litros de tinta'.format(alt,lar,area,tinta))