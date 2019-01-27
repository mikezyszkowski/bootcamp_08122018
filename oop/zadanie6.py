class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        if isinstance(other, int):
            return Vector(self.x * other, self.y * other)
        return NotImplemented

    def lenght(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __lt__(self, other):
        return self.lenght() < other.lenght()

def test_vector_init():
    vector_1 = Vector(x=1, y=2)
    assert vector_1.x == 1
    assert vector_1.y == 2

def test_vector_lenght():
    assert Vector(3, 4).lenght() == 5

def test_vector_add():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 2
    assert vector_3.y == 4
    assert vector_1.x == 1
    assert vector_1.y == 2

    vector_1 = Vector(x=2, y=3)
    vector_2 = Vector(x=4, y=5)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 2+4
    assert vector_3.y == 3+5

def test_vector_sub():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    vector_3 = vector_1 - vector_2
    assert vector_3.x == 0
    assert vector_3.y == 0

def test_vector_mul_vector():
    vector_1 = Vector(x=1, y=2)
    vector_2 = Vector(x=1, y=2)
    assert vector_1 * vector_2 == 1*1 + 2*2

# def test_vector_mul_int():
#     vector_1 = Vector(x=1, y=2)
#     vector_2 = Vector(x=1, y=2)
#     assert