class Mahasiswa:
    nama = ""
    
    def __init__(self, namaBaru):
        self.nama = namaBaru

    def tampil(self):
        print("Nama : "+str(self.nama))
    
mhs1 = Mahasiswa("Eby Sofyan Fadly")
mhs1.tampil()
# mhs1.nama = "Eby Sofyan Fadli"


        
        
        