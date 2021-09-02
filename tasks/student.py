"""
Создать класс Student.

Определить атрибуты:

- surname - фамилия
- name - имя
- group - номер группы
- average_score - средний балл

Определить методы:

- инициализатор __init__
- Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
  студентов по среднему баллу

Создать список из 5 объектов класса и вывести его отсортированным по возрастанию
и убыванию.

Вывести студентов, у которых средний балл больше 5
"""

import decimal


class Student:
    surname: str
    name: str
    group: int
    average_score: decimal

    def __init__(self, surname, name, group, average_score):
        self.surname = surname
        self.name = name
        self.group = group
        self.average_score = average_score

    def get_info(self):
        return self.surname, self.name, self.group, self.average_score

    def __repr__(self):
        return repr(f"<Student: {self.surname}, {self.name}, Group: {self.group}, Score: {self.average_score}>")

    def __lt__(self, other):
        return self.average_score < other.average_score

    def __gt__(self, other):
        return self.average_score > other.average_score

    def __eq__(self, other):
        return self.average_score == other.average_score

    def __le__(self, other):
        return self.average_score <= other.average_score

    def __ge__(self, other):
        return self.average_score >= other.average_score

    def __ne__(self, other):
        return self.average_score != other.average_score


if __name__ == '__main__':
    students_list = [
        Student("Targaryen", "Daenerys", 27, 8.8),
        Student("Snow", "Jon", 27, 3.7),
        Student("Stark", "Arya", 27, 5.1),
        Student("Stark", "Sansa", 27, 6.2),
        Student("Clegane", "Sandor", 27, 2.2)
    ]
    print(repr(sorted(students_list, key=lambda student: student.average_score)))
