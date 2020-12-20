st = input()
stlist = st.split()
s = int(stlist[0])
t = int(stlist[1])
ab = input()
ablist = ab.split()
a = int(ablist[0])
b = int(ablist[1])
mn = input()
mnlist = mn.split()
m = int(mnlist[0])
n = int(mnlist[1])
appdist = input()
appdistlist = appdist.split()
oradist = input()
oradistlist = oradist.split()
apple = 0
for i in range(m):
    if (((int(appdistlist[i]) + a) >= s) and ((int(appdistlist[i]) + a) <= t)):
        apple += 1
orange = 0
for i in range(n):
    if (((int(oradistlist[i]) + b) >= s) and ((int(oradistlist[i]) + b) <= t)):
        orange += 1
print(apple)
print(orange)
