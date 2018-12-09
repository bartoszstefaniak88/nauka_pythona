samolot = {'name': 'boeing',
           'przebieg': 10000,
           'type': 'pasazerski'}

#print(samolot['name'])
#print(samolot['przebieg'])
#print(samolot['nieznany_klucz'])
for key, value in samolot.iteritems():
    print("{0}:{1}".format(key, value))

for key in samolot:
    print("{0}:{1}".format(key, samolot[key]))
