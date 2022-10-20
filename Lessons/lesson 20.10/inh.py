class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    name = property(get_name, set_name)
    age = property(get_age, set_age)

    def hello(self):
        print(f"Greetings, I'm {self.name}")

    def glory(self):
        print(f"I'm a person and I have some feelings")


class Employee(Person):

    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    position = property(get_position, set_position)
    salary = property(get_salary, set_salary)

    def work(self, hours):
        print(f"I'm working for the next {hours} hours")

    def hello(self):
        Person.hello(self)
        print(f"also I'm {self.position}")

class Student(Person):

    def __init__(self, name, age, speciality) -> None:
        super().__init__(name, age)
        self.speciality = speciality

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, speciality):
        self.__speciality = speciality

    speciality = property(get_speciality, set_speciality)

    def study(self, hours):
        print(f"I'm studying for the next {hours} hours")

    def hello(self):
        super().hello()
        print(f"also I'm a student")

class WorkingStudent(Student, Employee):

    def __init__(self, name, age, speciality, position, salary) -> None:
        self.name = name
        self.age = age
        self.speciality = speciality
        self.position = position
        self.salary = salary


# e = Employee("Mikita", 31, "lead dev", "over9000")
# s = Student("Mikita", 27, "technology engineer")

# e.work(8)
# s.study(3)

# print(e.salary, e.position)
# print(e.age)

# e.hello()
# s.hello()

# ws = WorkingStudent("Vasya", 25, "economics", "intern", "-1000")
# ws.hello()
# ws.work(8)
# ws.study(3)
# ws.glory()

print(Person.mro())
print(Employee.mro())
print(Student.mro())
print(WorkingStudent.mro())