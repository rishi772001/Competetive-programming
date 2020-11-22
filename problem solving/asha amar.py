Gold = []
def calc(asha,amar,a1,a2,skip=-1):
    gold = 0
    check = 0
    alien1 = a1.copy()
    alien2 = a2.copy()
    while len(alien1) > 0 and len(alien2) > 0:
        if(check % 2 == 0):  #Asha's turn
            if (check == skip): #Asha skips
                check += 1
                continue

            m = min(alien1)
            val = [i for i, j in enumerate(alien1) if j == m]
            ans = val[0]
            for i in val:
                if(alien2[i] > alien2[ans]):
                    ans = i
            if(alien1[ans] <= asha):
                min_energy = ans
                gold += alien2[min_energy]
                alien1.pop(min_energy)
                alien2.pop(min_energy)
            else:     #amar's turn
                max_gold = alien2.index(max(alien2))
                alien1[max_gold] -= asha
        else:
            if(alien1[0] <= amar):
                alien1.pop(0)
                alien2.pop(0)
            else:
                alien1[0] -= amar
        check += 1
    Gold.append(gold)
    return check

asha = 20
amar = 60
aalien1 = [80,80,120]
aalien2 = [100,200,300]
val = calc(asha,amar,aalien1,aalien2)
for i in range(val):
    calc(asha,amar,aalien1,aalien2,i)

print(Gold)
print(max(Gold))