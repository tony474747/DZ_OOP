class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Вы где-то ошиблись'

    def average_grade(self):
        if not self.grades:
            return 0
        average = []
        for i in self.grades.values():
            average += i
        return sum([grade for grade in average]) / len(average)

    def __str__(self):
        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)
        res = f'Имя: {self.name}\n' \
              f'Фамилия: {self.surname}\n' \
              f'Средняя оценка за домашнее задание: {self.average_grade()}\n' \
              f'Курсы в процессе обучени: {courses_in_progress_string}\n' \
              f'Завершенные курсы: {finished_courses_string}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Так сравнивать не получится')
            return
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Так сравнивать не получится')
            return
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Так сравнивать не получится')
            return
        return self.average_grade() == other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        average = []
        for i in self.grades.values():
            average += i
        return sum([grade for grade in average]) / len(average)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Так сравнивать не получится')
            return
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Так сравнивать не получится')
            return
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Так сравнивать не получится')
            return
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Вы где-то ошиблись'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


lecturer_1 = Lecturer('Иван', 'Иванов')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Петр', 'Петров')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

rewiewer_1 = Reviewer('Антон', 'Антонов')
rewiewer_1.courses_attached += ['Python']
rewiewer_1.courses_attached += ['Git']

rewiewer_2 = Reviewer('Сергей', 'Сергеев')
rewiewer_2.courses_attached += ['Python']
rewiewer_2.courses_attached += ['Git']

student_1 = Student('Павел', 'Павлов')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Николай', 'Николаев')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

student_1.rate_lecturer(lecturer_1, 'Python', 1)
student_1.rate_lecturer(lecturer_2, 'Python', 2)
student_1.rate_lecturer(lecturer_1, 'Git', 8)
student_1.rate_lecturer(lecturer_2, 'Git', 7)

student_2.rate_lecturer(lecturer_1, 'Python', 3)
student_2.rate_lecturer(lecturer_2, 'Python', 4)
student_2.rate_lecturer(lecturer_1, 'Git', 8)
student_2.rate_lecturer(lecturer_2, 'Git', 7)

rewiewer_1.rate_student(student_1, 'Python', 2)
rewiewer_1.rate_student(student_2, 'Python', 3)
rewiewer_1.rate_student(student_1, 'Git', 10)
rewiewer_1.rate_student(student_2, 'Git', 9)

rewiewer_2.rate_student(student_1, 'Python', 1)
rewiewer_2.rate_student(student_2, 'Python', 4)
rewiewer_2.rate_student(student_1, 'Git', 10)
rewiewer_2.rate_student(student_2, 'Git', 9)

print(f'Перечень студентов:\n\n{student_1}\n\n{student_2}\n')
print(f'Перечень лекторов:\n\n{lecturer_1}\n{lecturer_2}\n')
print(f'Перечень проверяющих:\n\n{rewiewer_1}\n\n{rewiewer_2}\n')
print(f'Результат сравнения студентов по средним оценкам за ДЗ: ')
print(f'{student_1 > student_2}')
print(f'{student_1 < student_2}')
print(f'{student_1 == student_2}\n')
print(f'Результат сравнения лекторов по средним оценкам за ДЗ: ')
print(f'{lecturer_1 > lecturer_2}')
print(f'{lecturer_1 < lecturer_2}')
print(f'{lecturer_1 == lecturer_2}\n')

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]


def student_rating(student_lists, course_name):
    average = []
    for students in student_lists:
        for i, k in students.grades.items():
            if course_name == i:
                average += k
    return sum([grade for grade in average]) / len(average)


def lectorer_rating(lectorer_lists, course_name):
    average = []
    for lectorer in lectorer_lists:
        for i, k in lectorer.grades.items():
            if course_name == i:
                average += k
    return sum([grade for grade in average]) / len(average)


print(f'Средняя оценка для всех студентов на курсе Python: {student_rating(student_list, "Python")}')
print(f'Средняя оценка для всех студентов на курсе Git: {student_rating(student_list, "Git")}\n')
print(f'Средняя оценка для всех преподавателей на курсе Python: {lectorer_rating(lecturer_list, "Python")}')
print(f'Средняя оценка для всех преподавателей на курсе Git: {lectorer_rating(lecturer_list, "Git")}')
