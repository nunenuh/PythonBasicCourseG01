jml_makan = int(input("Masukan Jumlah Makan Per Hari : "))
jml_makan = jml_makan + 1

for i in range(1, jml_makan):
    if i==1:
        print("makan ke-"+str(i)+" Sarapan Pagi")
    elif i==2:
        print("makan ke-"+str(i)+" Makan Siang")
    elif i==3:
        print("makan ke-"+str(i)+" Makan Malam")
    elif i>3:
        print("makan ke-"+str(i)+" Melak")
    else:
        print("kasian belum makan")