
class Department:

    def __init__(self):
        self.department = 'Cybersecurity'
    
    def department_name(self):
        return print(f'The department name is: {self.department}')

my_department = Department()
my_department.department_name()


class Employee(Department):
    def __init__(self, first_name, last_name, id):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.salary = 800000
        self.rate = 1.05
        self.insurance = 5000
    
    def get_name(self):
        return print(f'First name: {self.first_name}. Last name: {self.last_name}.')
    
    def id_to_employee(self):
        return print(f'Employee id for {self.first_name} {self.last_name} is: {self.id}')
    
    def email(self):
        return print(f'Email is: {self.first_name}.{self.last_name}@company.department.com')
    
    def get_department(self):
        return print(f'{self.first_name} {self.last_name} belongs to department {self.department}')

    def increase_salary(self):
        self.salary = self.salary * self.rate
        return print(round(self.salary))
    
    def insurance_work(self):
        self.salary -= self.insurance
        return print(f'Your salary after insurance: {self.salary}')

employee = Employee('Lisa', 'Larsen', 10)
employee.get_name()
employee.id_to_employee()
employee.email()
employee.get_department()
employee.increase_salary()
employee.insurance_work()


class Hobby(Employee, Department):
    
    def __init__(self, first_name, last_name, id):
        super().__init__(first_name, last_name, id)
        self.hobby = 'Coding'
        self.money_hobby = 0
        self.money_hobby_list = list()
    
    def hobby_employee(self):
        return print(f'{self.first_name} {self.last_name} has {self.hobby} as a hobby.')
    
    def money_spent_on_hobby(self):
        if self.salary >= 6000:
            self.money_hobby += 5000
            self.money_hobby_list.append(self.money_hobby)
            return print(f'You can spend {self.money_hobby_list} on your hobby')
        
        else: 
            return print(f'You cannot use any money on your hobby.')

my_hobby = Hobby('Lisa', 'Larsen', 10)
my_hobby.hobby_employee()
my_hobby.money_spent_on_hobby()
