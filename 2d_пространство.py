# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 
# 2D пространстве.

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

X1 = int(input('Введите координату X1: '))
Y1 = int(input('Введите координату Y1: '))

X2 = int(input('Введите координату X2: '))
Y2 = int(input('Введите координату Y2: '))

# d = √ [(x2-x1)2+ (y2-y1)2], Где (x1, y1) и (x2, y2) 

result = ((X2 - X1)**2 + (Y2 - Y1)**2)**(0.5)
print(result)

