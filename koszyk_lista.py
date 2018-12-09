koszyk = [
    {'name': 'mleko', 'cena': 12.5},
    {'name': 'ser', 'cena': 4.0},
    {'name': 'konsola gier', 'cena': 114.0}
]
#print(koszyk[0] ['cena'])

#mleko i ser => 10%
#stan_raguly = {'mleko': False, 'ser': False}
bylo_mleko = False
#'ser' = False
byl_ser = False

suma = 0
for poz in koszyk:
    suma = suma + poz['cena']
    nazwa_prod = poz['name']
    if nazwa_prod == 'mleko':
        bylo_mleko = True
    if nazwa_prod == 'ser':
        byl_ser = True

if bylo_mleko and byl_ser:
    suma = suma - (suma * 10) / 100
print (suma)
