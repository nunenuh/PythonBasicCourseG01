
#Inheritance (Pewarisan)
# dalam OOP python
class Pohon:
    batang = "Kayu"
    ranting = "Besi"
    daun = "Plastik"


class PohonMangga(Pohon):
    buah = "Bulat Manis"


pm = PohonMangga()

#mengakses atribut bapaknya
print(pm.batang)

#mengakses atribut dirinya
print(pm.buah)