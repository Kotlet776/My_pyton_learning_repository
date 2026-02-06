def func(num1, num2):
    l = [num1, num2]
    if num1 > num2:
        l.reverse()
        return list(range(*l))
    elif num1 < num2:
        return list(range(*l))
    elif num1 == num2:
        return [num1]

print(func(10, 2))
print(func(5, 5))
print(func(-3, -10))

