class Employee(object):
    all_employee = 0
    change_pay = 1

    def __init__(self, first, last, pay):
        self.fname = first.lower()
        self.lname = last.lower()
        self.pay = pay
        Employee.all_employee += 1

    def get_email(self):
        return f"{self.fname}.{self.lname}@gmail.com"

    def get_fullname(self):
        return f"{self.fname} {self.lname}"

    @classmethod
    def increase_pay(cls, increament):
        """ Use to modify a class property """
        cls.change_pay *= increament

    def apply_raise(self):
        self.pay = int(float(self.pay) * Employee.change_pay)
        

    @classmethod
    def parse_string(cls, details):
        """ Use as alternative constructor """
        first, last, pay = details.split('-')
        return cls(first, last, pay)





def main():
    emp1 = Employee('Dotun', 'Peter', 100000)
    emp2 = Employee('Sola', 'Thomas', 200000)
    emp3 = Employee.parse_string('Kunle-Alade-120000')

    print('employee1 fullname: ', emp1.get_fullname())
    print('employee1 email: ', emp1.get_email())
    print('employee2 fullname: ', emp2.get_fullname())
    print('employee2 email: ', emp2.get_email())
    print('employee3 fullname: ', emp3.get_fullname())
    print('employee3 email: ', emp3.get_email())
    print('emp1: ', emp1.pay)
    Employee.increase_pay(1.05)
    emp1.apply_raise()
    print('emp1: ',emp1.pay)
    print('emp2: ',emp1.pay)

if __name__ == '__main__':
    main()





