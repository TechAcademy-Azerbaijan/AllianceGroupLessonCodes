from datetime import datetime

class Employee:

    def __init__(e, first_name, last_name):
        e.name = first_name
        e.surname = last_name


    @classmethod
    def create_employee(cls, employee_data):
        f_name, l_name = employee_data.split(" ")
        return cls(f_name, l_name)

    def __repr__(self):
        return f"{self.name} {self.surname}"
    

emp_data = input("Ad ve soyadi daxil edin: ") # "Ali jksndfjkn"

emp = Employee.create_employee(emp_data)
print(emp)

#f_name = input('Adini daxil edin: ') # ali
#l_name = input('Soyadini daxil edin: ')

#e = Employee(first_name=f_name, last_name=l_name)
#print(e.name)