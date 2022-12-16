# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

# def f(x):
#  if x == 1:
#     return 'Целое'
#  elif x == 2.3:
#     return 23
#  else:
#     return

# arg = 2
# print(f(arg))
# print(type(f(arg)))

A = int(input('Введите номер четверти: '))
if A == 1:
    print('X>0, Y>0')
elif A == 2:
    print('X<0,Y>0')
elif A == 3:
    print('X<0,Y<0')
elif A == 4:
    print('X>0,Y<0')