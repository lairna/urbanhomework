from math import inf


def fake_divide(first, second):
    if second == 0:
        return "Ошибка"
    else:
        return first / second


def true_divide(first, second):
    if second == 0:
        return inf
    else:
        return first / second


result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)
