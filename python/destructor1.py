class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama
        print(f'Mahasiswa {self.nama} dibuat')
    
    def __del__(self):
        print(f'Mahasiswa {self.nama} dihapus')
 
# print('Hello World!')       
# budi = Mahasiswa('budi')
# print('Halo Semuanya')
# andi = Mahasiswa('andi')
# print('1 + 1 = 2')
# print('2 + 2 = 4')

mahasiswaX = Mahasiswa('Budi')
mahasiswaX = 10 # Budi kehilangan referensi

print(f'mahasiswaX = {mahasiswaX}')