#Z písemky nebude známka, ale jen Pass/Fail hodnocení neboli prospěl(a)/neprospěl(a). 
# Vytvoř nový slovník. Jeho klíče budou opět jména žáků, a hodnotou bude řetězec "Pass", pokud má jednotlivec alespoň než 60 bodů. Pokud má méně než 60, hodnota bude "Fail".

#Výsledný slovník ulož jako JSON do souboru prospech.json.

import json
with open('ukol_03.json', encoding='utf-8') as soubor:
    data = json.load(soubor)

print(data) 


for jmeno, body in data.items():
    if body > 60:
        with open('prospech.json', mode='w', encoding='utf-8') as vystupni_soubor:
            json.dump(data, vystupni_soubor, ensure_ascii=False, indent=4)
        with open('prospech.json', encoding='utf-8') as file:
            output[data] = json.load(file)
        output[data]['hodnoceni'].update(str('Pass'))
        
    else:
        with open('prospech.json', mode='w', encoding='utf-8') as vystupni_soubor:
            json.dump(data, vystupni_soubor, ensure_ascii=False, indent=4)
        with open('prospech.json', encoding='utf-8') as file:
            output = json.load(file)
        output[data]['hodnoceni'].update(str('Fail'))

print(vystupni_soubor)
