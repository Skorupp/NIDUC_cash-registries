import random


class Klient:

    def __init__(self, idTransaction : int):
        self.exists = True
        self.family = random.randint(0, 5)
        self.IdTransaction = idTransaction
        self.local = random.randint(0, 1)
        self.wroclaw = random.randint(0, 2)
        self.family = random.randint(0, 5)
        self.total = random.randint (10, 500) * self.family
        self.age = random.randint(10, 90)
        self.card = random.randint(0, 1)
        self.totalTime = random.randint(2, 6) + (self.family * 2) - self.card # oblicza calkowity czas na obsluge wliczajac wielkosc rodziny oraz posiadanie karty

