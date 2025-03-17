class Person:
    def __init__(self, name, person_id, gender):
        self.name = name
        self.person_id = person_id
        self.gender = gender

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_id(self):
        return  self.person_id

    def set_id(self, new_id):
        self.person_id = new_id

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

class Empl(Person):
    def __init__(self, name, empl_id, gender, salary):
        super().__init__(name, empl_id, gender)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary


if __name__ == '__main__':
    empl = Empl("Alice", "001", "Female", 100000)
    print(empl.get_salary())



