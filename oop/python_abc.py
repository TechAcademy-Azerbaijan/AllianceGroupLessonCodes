from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetr(self):
        pass


class Square(Shape):

    def __init__(self, a):
        self.__a = a

    @property
    def a(self):
        return self.__a

    def area(self):
        return self.__a**2
    
    def perimetr(self):
        return self.__a * 4


class Rectange(Shape):

    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def area(self):
        return self.__a * self.__b
    
    def perimetr(self):
        return 2 * (self.__a + self.__b)


def print_shape_area_and_perimetr(shape):
    print(shape.area())
    print(shape.perimetr())

s = Square(4)
print('kvadratin sahesi ve perimetri')
print_shape_area_and_perimetr(s)

r = Rectange(2,3)
print('Duzbucaqlinin sahesi ve perimetri')
print_shape_area_and_perimetr(r)

print(s.a)