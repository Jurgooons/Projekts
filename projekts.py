from statistics import mode

def Vid(dati): 
    return sum(dati) / len(dati) 

dati = []
n = int(input("Ieraksti datu skaitu : ",))
for i in range(0, n):
    ele = int(input())
    dati.append(ele)

dati.sort

if(len(dati) %2 == 0):
    ind1 = int((len(dati)-1)//2)
    ind2 = int(((len(dati))/2))
    # print(ind1,ind2)
    med = (dati[ind1]+dati[ind2])/2
    print("Mediāna ir:", med)
    
else:
    indeks = len(dati)//2
    print("Mediāna ir :",dati[indeks])

print("Lielākais skaitlis ir", max(dati))
print("Mazākais skaitlis ir", min(dati))
print("Amplituda ir", max(dati)-min(dati))
print("Vidējais ir", Vid(dati))
print("Moda ir", mode(dati))