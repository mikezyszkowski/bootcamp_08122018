def sumator(arg):
    total = 0
    if isinstance(arg, dict):
        arg = arg.values()
    for x in arg:
        try:
            x = int(x)
            total += x
        except ValueError:
            pass
    return total


assert sumator([1, 2, 3]) == 6
assert sumator([10, 20, 30]) == 60
assert sumator([1, 2, 'a', 3]) == 6
assert sumator({'a': 10, 1: 20, 'c': 30, 'd': '40'}) == 100