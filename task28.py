'''Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

Пример:

2 4
6'''
def suma(a, b):
    if a == 0:
        return b
    return suma(a-1, b+1)
    
a = int(input('Введите число a: ')) 
b =  int(input('Введите число b: ')) 

print(suma(a, b))