#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math
x1 = float(input(f'Enter the coordinate for \"x1" '))
y1 = float(input(f'Enter the coordinate for \"y1"'))
x2 = float(input(f'Enter the coordinate for \"x2"'))
y2 = float(input(f'Enter the coordinate for \"y2"'))
result = math.sqrt ((x2-x1)**2+(y2-y1)**2)
print(f'The distance between two points is {round(result,3)}')