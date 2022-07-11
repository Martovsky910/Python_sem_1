# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
print('Введите координаты точки A:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Введите координаты точки B: ")
x_B = float(input('X: '))
y_B = float(input('Y: '))
result = 0
result = ((x_B - x_A)**2) + ((y_B - y_A)**2)
print(result)
# ( x b — x a ) 2 + ( y b — y a ) 2