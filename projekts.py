import math as m
dati = []
n = int(input("Ieraksti datu skaitu : "))
for i in range(0, n):
    ele = int(input())
    dati.append(ele)
dati.sort
print("Lielākais skaitlis ir", max(dati)-min(dati))
print("Mazākais skaitlis ir", min(dati))
print("Amplituda ir", max(dati)-min(dati))
if(len(dati) %2 == 0):
    ind1 = int((len(dati)-1)//2)
    ind2 = int(((len(dati))/2))
    # print(ind1,ind2)
    summa = dati[ind1]+dati[ind2]
    print("Moda ir:", summa/2)
    
else:
    indeks = len(dati)//2
    print(dati[indeks])

vid = sum(dati)/len(dati)
print("Vidējais ir", vid)