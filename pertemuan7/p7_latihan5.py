
class CetakanAgarAgar:    
    warna = ""
    gula = ""


print("Cetakan Agar Agar ")
a = 0
arlist = []
while a < 3:
    wr = str(input("Warna O"+str(a+1)+": "))
    gl = str(input("Gula O"+str(a+1)+": "))

    caa = CetakanAgarAgar()
    caa.warna = wr
    caa.gula = gl

    arlist.append(caa)

    a = a+1

print(arlist)

print(arlist[0].warna)