import time

def log(funkcja):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = funkcja(*args, **kwargs)
        stop = time.time()
        duration = stop-start
        print(f'Długość wywołania {funkcja.__name__} to {duration}s')
        return result

    return wrapper




@log
def foo(arg):
    return f'to jest{arg}'


foo('1')

# def test_decorated_foo():
#     assert "Długość wywołania foo" in foo(1)