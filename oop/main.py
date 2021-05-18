class Human:
    first_name = 'Sebuhi'
    last_name = 'Cavadli'
    __age = 26

    def move(self):
        print('Moved')

    def work(self):
        print('Human worked')

    def run(self):
        print('I am running')

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_value):
        if new_value < self.__age:
            raise Exception('Yeni age evvelkinden kicik ola bilmez!')
        self.__age = new_value


class Employee:

    def work(self):
        print('Worked')


class Programmer(Human, Employee):
    
    def work(self): # overiding
        print('i am write the code')


sebuhi_obj = Programmer()  
sebuhi_obj.work()


#print(sebuhi_obj.age)
#sebuhi_obj.age -= 1
# print(sebuhi_obj.age)

# print(Programmer.)

# sebuhi_obj.move()

