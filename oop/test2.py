class Bmw:
    engine = 3.0

    @classmethod
    def change_engine(cls, new_eng):
        cls.engine = new_eng
    
    @staticmethod
    def create_new_branch():
        print('new branch created')

f30 = Bmw()
print(f30.engine)
f30.engine = 3.5
print(f30.engine)
Bmw.change_engine(3.5)

f80 = Bmw()
print(f80.engine)
Bmw.create_new_branch()
