produkty = {'S1222': 'sukienka trojkat',
           'P1222': 'spodnie krata',
           'X212': 'konsola do gier'}

igla = 'X212'

if igla in produkty:
    print("Znalazlem {0}".format(igla))
else:
    print("Brak w magazynie {0}".format(igla))
