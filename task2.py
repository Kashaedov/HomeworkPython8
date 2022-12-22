from random import randint

names = ["Иван", "Антатолий", "Егор", "Артем", "Николай", "Денис", "Александр", "Дмитрий", "Сергей", "Кирилл"]
last_names = ["Иванов", "Сидоров", "Петров", "Волевой", "Смирнов", "Кузнецов", "Попов", "Васильев", "Михайлов", "Соколов"]
groups = ["Группа №1:Техник-строитель", "Группа №2:Техник-механик"]


class Student:
    def __init__(self, name: str, group: str, progress: list[int]):
        self.name = name
        self.group = group
        self.progress = progress

    def __str__(self) -> str:
        return self.name + ' | ' + self.group + ' | ' + str(self.progress)

    def average_marks(self) -> float:
        return sum(self.progress) / len(self.progress)


class Faculty:
    def __init__(self, quantity=1):
        self.quantity = quantity
        self.students = []
        for _ in range(self.quantity):
            student_name = ' '.join([names[randint(0, len(names) - 1)],
                                     last_names[randint(0, len(last_names) - 1)]])
            student_group = groups[randint(0, len(groups) - 1)]
            student_progress = [randint(1, 10) for _ in range(randint(3, 10))]
            self.students += [Student(student_name, student_group, student_progress)]

    def sort_by_names(self, reverse=True):
        self.students.sort(reverse=reverse, key=lambda x: x.name)

    def print_all_students(self):
        for student in self.students:

            print(student)


    def bad_raiting(self) -> None:
        print('Cтуденты с плохой успеваемостью (Средний балл меньше 4):')
        for student in self.students:
            if student.average_marks() <= 4:
                print(student)


    def add_student(self, student: Student) -> None:
        self.students += [student]


if __name__ == '__main__':
    faculty = Faculty(20)
    faculty.print_all_students()
    faculty.bad_raiting()
