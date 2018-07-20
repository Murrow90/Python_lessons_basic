# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

a = input(int("Введите координату точки а: "))
b = input(int("Введите координату точки b: "))
c = input(int("Введите координату точки c: "))

class Triangle
	def __init__(self, a, b, c, c1, b1):
		self.a = [x1, y1]
		self.b = [x2, y2]
		self.c = [x3, y3]
		self.c1 = [x1, y3]
		self.b1 = [y1, x2]
		
		
	def AB(self):
		return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
		
	def AC(self):
		return math.sqrt((y3 - y1) ** 2 + (x3 - x1) ** 2)
		
	def BC(self):
		return msth.sqrt((x3 - x2) ** 2 + (y2 - y3) ** 2)
		
	def AC1(self):
		return y3 - y1

	def AB1(self):
		return x2 - x1
	
	def P(self):
		return P = self.AB() + self.AC() + self.BC()
		
	def cosCAC1(self):
		return AC1 / AC
		
	def cosBAB1(self):
		return AB1 / AB
	
	def CAB(self):
		return 90 - (math.acos(self.cosCAC1()) + math.acos(self.cosBAB1()))

	def H(self):
		return math.sin(self.CAB()) * self.AC()
		
	def S(self):
		return (self.AC() / 2) * self.H()
	

Triag = Triangle(a, b, c)
print("P = " + str(Triag.P())
print("h = " + str(Triag.h())
print ("S = " + str(Triag.S())
	

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

