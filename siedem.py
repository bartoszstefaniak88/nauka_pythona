owoce = ['jablko', 'gruszka','banan', 'arbuz']
ilosc = [3, 6, 4, 2]

for idx in range(len(owoce)):
    print("idx: " + str(idx) + ":" + owoce[idx])
    print(owoce[idx] + " w ilosci " + str(ilosc[idx]))
print("{0} w ilosci {1}".format(owoce, ilosc))
