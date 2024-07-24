print('Введите три целых числа')
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Введите третье число:'))
if a == b and b == c:
    print('3')
elif a == b or b == c or a == c:
    print('2')
else:
    print('0')
