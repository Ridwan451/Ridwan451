from tokenize import Double
import math


class Lingkaran(object):
    def __init__(self, r:Double):
        self.r = r
    
    def getDiameter(self):
        print(f'diameter : {self.r * 2}')
        
    def getKeliling(self):
        print(f'Keliling : {2 * math.pi * self.r}')      

    def getLuas(self):
        print(f'Luas : {math.pi * (self.r * self.r)}')
    
    
class Kerucut(Lingkaran):
    def __init__(self, r: Double, tinggi:Double):
        super().__init__(r)
        self.tinggi = tinggi
        
    def getTinggi(self):
        return self.tinggi
    
    def getVolume(self):
        print (f'Volume : {1/3 * self.r * self.tinggi}')
    
    def getLuas(self):
        return super().getLuas()

class Silinder(Lingkaran):
    def __init__(self, r: Double, tinggi:Double):
        super().__init__(r)
        self.tinggi = tinggi

    def getTinggi(self):
        return self.tinggi
    
    def getVolume(self):
        print(f'Volume : {self.tinggi * math.pi * (self.r * self.r)}')

    def getLuas(self):
       return super().getLuas()

hitung = Lingkaran(
    r=10
)

hitungK=Kerucut(
    r=10,
    tinggi=5
)

hitungs=Silinder(
    r=10,
    tinggi=5
)

hitung.getDiameter()
hitung.getKeliling()
hitung.getLuas()
print("_____")
hitungK.getVolume()
hitungK.getLuas()
print("___")
hitungs.getVolume()
hitungs.getLuas()