marka = 'Peugot'
ilosc_drzwi = 5
pojemnosc = 1.3
marka_up = marka.lower()

print ("Samochod" + marka.lower()  + "ma" + str(ilosc_drzwi) + "drzwi")
print (marka_up)
print("pojemnosc po zmianach: " + str(pojemnosc * 2))

if ilosc_drzwi > 3:
    print('Duzy Samochod')
else:
    print('Inny')

if marka.startswith( 'Pe' ):
    print ('samochod francuski')
else:
    print('Inny')
