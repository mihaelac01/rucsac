def rucsac(valoarea, volum, V):
    index = list(range(len(valoarea)))
    raport = [v / w for v, w in zip(valoarea, volum)]
    index.sort(key = lambda a: raport[a], reverse=True)
    max_valoarea = 0
    frac = [0] * len(valoarea)
    for a in index:
        if volum[a] <= V:
            frac[a] = 1
            max_valoarea += valoarea[a]
            V -= volum[a]
        else:
            frac[a] = V / volum[a]
            max_valoarea += valoarea[a] * V / volum[a]
            break
    return max_valoarea, frac
n = int(input("nr. de lucruri "))
valoarea = [int(input(f"valoarea a {n} de lucruri ")) for _ in range(n)]
volum = [int(input(f"volumul a {n} de lucruri: ")) for _ in range(n)]
V = int(input("volumul rucsacului: "))
max_valoarea, frac = rucsac(valoarea, volum, V)
for a in range(len(frac)):
    print(f"încap {round(frac[a], 2)} de lucruri, cu pretul de {valoarea[a]}")
print('suma valorilor lucrurilor :', max_valoarea)