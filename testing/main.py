
class Calc:
    def __init__(self, first, second):
        self.a = first
        self.b = second

    def add(self):
        return self.a + self.b

    def divide(self):
        if self.b == 0:
            raise ZeroDivisionError("You can't divide by zero")
        return self.a / self.b

# if __name__ == '__main__':
#    print('from main.py: ', add(7,5))
