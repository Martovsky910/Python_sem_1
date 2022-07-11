# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
x = 0
y = 1
z = 2
left_xyz = not(x or y or z)
right_xyz = not x and not y and not z 
result = left_xyz == right_xyz
print(result)