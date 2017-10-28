
class Manusia:
    
    #attribute
    nama = ""
    tanggal_lahir = ""
    tempat_lahir = ""
    gender = ""

    #constructor
    def __init__(self):
        pass

    #method
    def makan(self):
        print(self.nama + ' Sedang Makan') 
    
    def minum(self):
        print(self.nama + ' Minum 2 Gelas Air Putih')
    
m = Manusia()
m.nama = "Fandi"
m.tanggal_lahir = "24 Oktober 1988"
m.tempat_lahir = "Mataram"
m.gender = "Pria"

m.makan()
m.minum()

