import math as m
x1=int(input("Введите отрезок x1: "))
x2=int(input("Введите отрезок x2: "))
y1=int(input("Введите отрезок y1: "))
y2=int(input("Введите отрезок y2: "))
class Otrezok:
    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2
    def __add__(self):
        z=self.x1+self.x2
        self.z = z
        return self.z
    def __sub__(self):
        p=self.y2-self.y1
        self.p=p
        return self.p
    def __abs__(self):
        a=self.x1-self.x2
        self.a=a
        return self.a if self.a > 0 else -self.a     
otr=Otrezok(x1,x2,y1,y2)
print("Сложение 2 отрезков x1 и x2: ",otr.__add__())
print("Вычитание 2 отрезков y2 и y1: ",otr.__sub__())
print("Модуль отрезков x1 и x2: ",otr.__abs__())
