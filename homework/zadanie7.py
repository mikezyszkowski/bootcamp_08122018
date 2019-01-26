import time

def czas_wykonania(dekorowana_funkcja):

    def wrapper(*args, **kwargs):
        start = time.time()
        wynik = dekorowana_funkcja(*args, **kwargs)
        stop = time.time()
        print(f"Czas wykonania funkcji {dekorowana_funkcja.__name__} z argumentami {args}, {kwargs} wynosi{stop-start} s")
        return wynik

    return wrapper