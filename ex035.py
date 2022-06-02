seg1 = int(input('Informe o 1º segmento: '))
seg2 = int(input('Informe o 2º segmento: '))
seg3 = int(input('Informe o 3º segmento: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos {} {} {} formam um triângulo: '.format(seg1, seg2, seg3))
else:
    print('Os segmentos {} {} {} não formam um triângulo: '.format(seg1, seg2, seg3))