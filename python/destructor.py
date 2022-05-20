class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        print(f'Mahasiswa {self.nama} dibuat')
    
    def __del__(self):
        print(f'Mahasiswa {self.nama} dihapus')
        
budi = Mahasiswa('budi')
andi = Mahasiswa('andi')

del andi
del budi