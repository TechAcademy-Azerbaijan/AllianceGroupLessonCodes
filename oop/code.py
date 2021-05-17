class Trever:

    def __init__(self):
        pass

    def sound(self):
        print('Trever danisir')


class Michel(Trever):

    def sound(self):
        print('Michel danisir')


class Frank(Trever):

    def sound(self):
        super().__init__()
        print('Trever danisir')

Trever.__init__()