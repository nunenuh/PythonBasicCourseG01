

class Lingkaran:

    r = 0.0
    
    def luas(self):
        return 3.14*self.r*self.r

    def keliling(self):
        return 2*3.14*self.r

    def tampil(self):
        self.luas()

        print("Jari - Jari : "+str(self.r))
        print("Luas : "+str(self.luas()))
        print("Keliling : "+str(self.keliling()))


ra = Lingkaran()
ra.r = 12.5
