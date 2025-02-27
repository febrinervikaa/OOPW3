class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

orang1 = Orang("Jeno", 20)
print(orang1)

del orang1
print("Objek orang1 telah dihapus")
