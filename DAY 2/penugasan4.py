import math

# Definisikan kelas dasar Shape
class Shape:
    def hitung_luas(self):
        pass
    # Definisikan kelas turunan Square yang mewarisi dari Shape
    class Square(Shape):
        def__init__(self, sisi):
        self.sisi = sisi

        def hitung_luas(self):
            return self.sisi ** 2
        
        # Definisikan kelas turunan Circle yang mewarisi dari Shape
        class Circle(Shape):
            def__init__