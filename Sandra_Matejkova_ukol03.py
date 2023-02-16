#Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). 
# Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

#Výsledný slovník ulož jako JSON do souboru prospech.json.

import json
with open('ukol_03.json', encoding='utf-8') as soubor:
    data = json.load(soubor)

print(data) 

prospech = {}

for jmeno, body in data.items():
    if body > 60:
        prospech[jmeno] = 'Pass'
    else:
        prospech[jmeno] = 'Fail'

jsonString = json.dumps(prospech, ensure_ascii=False)

jsonFile = open("prospech.json", "w",  encoding='utf-8')
jsonFile.write(jsonString)
jsonFile.close()