class Mahasiswa:
    nama = ""
    nim = ""
    jurusan = ""
    ipk = 0.0

    def tampil(self):
        print("Nama : "+str(self.nama))
        print("NIM : "+str(self.nim))
        print("Jurusan : "+str(self.jurusan))
        print("IPK : "+str(self.ipk))

mhs1 = Mahasiswa()
mhs1.nama = "Eby Sofyan Fadli"
mhs1.nim = "1410530181"
mhs1.jurusan = "S1 Teknologi Informasi (TI)"
mhs1.ipk = "3.4"
mhs1.tampil()

# mhs2 = Mahasiswa()
# mhs2.nama = "Faris"
# mhs2.nim = "1410530248"
# mhs2.jurusan = "S1 Teknologi Informasi (TI)"
# mhs2.ipk = "3.1"
# mhs2.tampil()


        
        
        