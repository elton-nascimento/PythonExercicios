"""
FATIAMENTO DE STRINGS
"""

frase = 'Curso em Vídeo Python'
print(frase)
print(frase[9:21])
print(frase[9:21:2])
print(frase[:5])
print(frase[15:])
print(frase[9::3])

print(len(frase))
print('aqui')
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Python' in frase)

print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
div = frase.split()
print(len(div))
print(div)
print(div[0])
jun = '-'.join(frase)
print(jun)

fr = '   Aprendendo python  '
print(fr)
print(fr.strip())
print(fr.rstrip())
print(fr.lstrip())



