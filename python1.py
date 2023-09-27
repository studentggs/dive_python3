# Задача 2 

a, b, c = map(int, input('Введите длину сторон треугольника через пробел: ').split())

def ex_check(x, y, z):
    return True if (a + b > c) and (b + c > a) and (c + a > b) else False

def side_check(x, y, z):
    return 'равнобедренный' if x == y or y == z or x == z else 'разносторонний'

print('Треугольник существует и он ' + side_check(a, b, c) if ex_check(a, b, c) else 'Треугольник не существует')

# Задача 3 

num = int(input('Введите число от 1 до 100 тысяч: '))
def is_valid(x):
    if 0 < x < 10000:
        return x
    else:
        x = int(input('Ваше число не правильно! Введите число от 1 до 100000: '))
        return is_valid(x)

if is_valid(num):
    print('Число простое' if len([i for i in range(1, num+1) if num % i == 0]) == 2 else 'Число составное')
