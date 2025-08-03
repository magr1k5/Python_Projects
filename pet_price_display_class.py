import math as m
a=int(input("Введите координату точки центра по оси x: "))
b=int(input("Введите координату точки центра по оси y: "))
c=int(input("Введите радиус: " ))
class Circle:
   def circle_lenght(c):
       return  m.pi * c * c
print("Координаты точки центра(по x,y): " , a,b)
print("Радиус равен: " , c)
print("Площадь окружности равна: " ,Circle.circle_lenght(c))
