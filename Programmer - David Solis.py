class Person(object):
    def __init__(self, name, age, education):
        self.name = name
        self.education = education
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


christian = Person("Christian", "14", "9th Grade")
christian.work()


class Employee(Person):
    def __init__(self, name, age, education, job, salary):
        super(Employee, self).__init__(name, age, education)
        self.job = job
        self.salary = salary

    def maintenance(self):
        print("Christian dies by slipping on the floor during maintenance.")


worker = Employee("Alek", "14", "9th Grade", "Dad Helper", "$10/day")


worker.maintenance()


class Programmer(Employee):
    def __init__(self, name, age, education, job, salary, type_of_computer, program):
        super(Programmer, self).__init__(name, age, education, job, salary)
        self.type_of_computer = type_of_computer
        self. program = program

    def code(self):
        print("Ian is now coding")


ian = Programmer("Ian", "14", "9th Grade", "Programmer", "$1,000,000", "Most Expensive one on market.", "Python")


ian.code()
