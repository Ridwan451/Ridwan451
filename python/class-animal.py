from ast import ClassDef
from msilib.schema import Class


class hewan(object):
    
    def __init__(self, nama):
        self.nama = nama
        
    def makan(self, makan):
        self.makan = makan
        
        print(f'{self.nama} memakan {self.makan}')
        
    def perilaku(self, bersuara, bergerak):
        self.bersuara = bersuara
        self.bergerak = bergerak
        
        print(f'{self.nama} suaranya {self.bersuara}')
        print(f'{self.nama} bergerak menggunakan {self.bergerak}')
        
class kucing(hewan):

    def __init__(self, nama):
        super().__init__(nama)
        
    def makan(self, makan):
        return super().makan(makan)
 
class anjing(hewan):
    pass

class burung(hewan):
    pass
        
k = kucing('Kucing')
a = anjing('anjing')

k.makan('Wiskas')
a.makan('makanan anjing')

k.perilaku('meow','4 kaki')
a.perilaku('woof woof','4 kaki')