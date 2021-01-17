class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def set_salary(self,salary):
        if salary > 0:
            self.salary = salary
    def set_name(self,name):
        if len(name) > 0:
            self.name = name
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def display_employee(self):
        print(f"employee name: {self.name} and his/her salary : {self.salary}")
    
class Company:
    def __init__(self,employee_list = None):
        if employee_list == None:
            self.employee_list = []
        else:
            self.employee_list = employee_list
    def get_employee_list(self):
        return self.employee_list
    def set_employee_list(self,employee_list):
        self.employee_list = employee_list
    def add_employee(self,new_employee):
        if isinstance(new_employee,Employee):
            self.employee_list.append(new_employee)
    def calc_avrg_salary(self):
        total = 0
        for emp in self.employee_list:
            total += emp.get_salary()
        return total / len(self.employee_list)
    def display_info(self):
        for emp in self.employee_list:
            print(emp.display_employee())
c = Company()
e1 = Employee("Deniz", 10)
e2 = Employee("Aslı", 20)
e3 = Employee("Ahmet", 30)

c.add_employee(e1)
c.add_employee(e2)
c.add_employee(e3)
c.add_employee(90)
c.display_info()

print("Average Salary:", c.calc_avrg_salary())