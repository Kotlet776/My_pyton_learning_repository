def numbers(a, b) -> int:
    """
    Docstring for numbers
    
    :param a: Description is equal to b
    :param b: Description b is the sum of a + b
    """
    a = b
    b = a+b
    return (a,b)

num = numbers(5, 50)

match num:
    case (0, 0):
        print("Center")
    case (0, y):
        print(f"x is equal to 0, but y is equal to {y}")
    case (x, 0):
        print(f"y is equal to 0, but y is equal to {x}")
    case _:
        print("Neither x or y is equal to 0")
