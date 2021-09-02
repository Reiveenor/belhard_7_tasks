"""
Создайте класс RandSequence с методами, формирующими вложенную последовательность.

Определить атрибуты:

- n - длина последовательности
- sequence - последовательность

Определить методы:

- инициализатор __init__, который принимает длину последовательности n и генерирует
    случайную последовательность длиной n в атрибут sequence
- метод generate, который принимает длину последовательности n (если n не передано,
    то сгенерировать длиной self.n) и генерирует последовательность в атрибут sequence.
    Для получения некоторого рандомного числа - воспользоваться функцией
    random.randint(-n, n)
- метод print_seq, который выводит последовательность на экран
"""

import random


class RandSequence:
    n: int
    sequence: list

    def __init__(self, n=0):
        self.n = n
        self.sequence = [random.randint(-n, n) for n in range(n)]
        print(self.sequence)

    def generate(self, n=None):
        if n is None:
            self.n = random.randint(-self.n, self.n)
            sequence = [random.randint(-self.n, self.n) for n in range(self.n)]
        else:
            sequence = [random.randint(-n, n) for n in range(n)]
            print(sequence)

    def print_seq(self):
        print(self.sequence)


if __name__ == '__main__':
    some_v = RandSequence(5)
    some_v.generate()
    some_v.generate(10)
