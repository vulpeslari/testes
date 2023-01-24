from main2 import Professor
from student import Student


def get_name(usuario):
    nome = input(f"Digite o nome do {usuario}:")
    return nome


def get_id():
    id = int(input("Digite o número de matrícula:"))
    return id


def get_age():
    age = int(input("Digite sua idade:"))
    return age


P1 = Professor(get_name("Professor"), get_id(), get_age())
#P2 = Professor(get_name("Professor"), get_id(), get_age())
#P3 = Professor(get_name("Professor"), get_id(), get_age())


E1 = Student(get_name("aluno"), get_id(), get_age())
P1.add_student(E1)

P1.print_students()
print(f"O nome do(a) professor(a):{P1.name}, matrícula de número:{P1.id}, idade:{P1.age}")
