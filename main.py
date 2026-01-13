import random

# ---------- 1. KLASĖS PLANAS ----------

f = open("vardai.txt", "r", encoding="utf-8")
mokiniai = f.read().split()
f.close()

random.shuffle(mokiniai)

n = int(input("Eilutės: "))
m = int(input("Vietos eilėje: "))

while len(mokiniai) > n * m - 1:
    print("Per mažai vietų!")
    n = int(input("Eilutės: "))
    m = int(input("Vietos eilėje: "))

ilgiausias = 0
for v in mokiniai:
    if len(v) > ilgiausias:
        ilgiausias = len(v)

plotis = ilgiausias + 1

klase = []
for i in range(n):
    klase.append([""] * m)

klase[0][0] = "---"

i = 0
for r in range(n):
    for c in range(m):
        if r == 0 and c == 0:
            continue
        if i < len(mokiniai):
            klase[r][c] = mokiniai[i]
            i += 1
        else:
            klase[r][c] = "laisva"

f = open("klases_planas.txt", "w", encoding="utf-8")
for r in range(n):
    for c in range(m):
        f.write(klase[r][c].ljust(plotis))
    f.write("\n")
    if (r + 1) % 2 == 0:
        f.write("\n")
f.close()

print("Klasės planas padarytas")


# ---------- 2. TVARKARAŠTIS ----------

f = open("pamokos.txt", "r", encoding="utf-8")
pamokos = f.read().splitlines()
f.close()

pamokos2 = []
for p in pamokos:
    pamokos2.append(p)
    pamokos2.append(p)

random.shuffle(pamokos2)

dienos = ["Pirmadienis", "Antradienis", "Trečiadienis", "Ketvirtadienis", "Penktadienis"]

f = open("rez_pamokos.txt", "w", encoding="utf-8")

k = 0
for d in dienos:
    f.write(d + "\n")
    for i in range(6):
        f.write(str(i + 1) + ". " + pamokos2[k] + "\n")
        k += 1
    f.write("\n")

f.close()

print("Tvarkaraštis padarytas")
