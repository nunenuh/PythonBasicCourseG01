
isi_ruangan = ['lcd','meja','ac','papan','bantal']
jumlah = len(isi_ruangan)
index = 0

print("Menggunakan Reverse")
isi_ruangan.reverse()
for idx in range(index, jumlah):
    print(isi_ruangan[idx])


print("Menggunakan Sort")
isi_ruangan.sort()
for idx in range(index, jumlah):
    print(isi_ruangan[idx])
