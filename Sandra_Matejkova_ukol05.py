teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

#Vytvořte seznam průměrných teplot pro každý den.
LIST_AVG = [sum(teplota) / len(teplota)  for teplota in teploty]
print(LIST_AVG)
#Vytvořte seznam ranních teplot.
LIST_FIRST = [teplota[0] for teplota in teploty]
print(LIST_FIRST)
#Vytvořte seznam nočních teplot.
LIST_LAST = [teplota[-1] for teplota in teploty]
print(LIST_LAST)
#Vytvořte seznam dvouprvkových seznamů obsahujících pouze polední a noční teplotu.
LIST_NEW = [[teplota[0], teplota[-1]] for teplota in teploty]
print(LIST_NEW)