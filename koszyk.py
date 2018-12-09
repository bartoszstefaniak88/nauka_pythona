owoce = ['jablko', 'gruszka','banan', 'arbuz']
cena = [3, 6, 4, 2]
suma = 0

for c in cena:
    suma = suma + c

if len(owoce) > 3:
    print( 'Promocja 30%')
    suma = suma - (suma * 30.0) / 1000
    print("Do zaplaty: {0}".format(suma))
