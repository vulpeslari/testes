class Professor:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age
        self.lista = []

    def add_student(self, students):
        self.lista.append(students)


    def print_students(self):
        for i in range(len(self.lista)):
            print(self.lista[i].name, self.lista[i].id, self.lista[i].age)

    def remove



