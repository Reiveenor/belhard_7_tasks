"""
Описать класс Counter, реализующий целочисленный счетчик.
который может увеличивать или уменьшать свое значение (атрибут value)
на единицу в заданном диапазоне.

Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

Определить атрибуты:

- value - текущее значение счетчика

Определить методы:

- инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
- increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
- decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
- метод __iter__
- метод __next__
"""


class Counter:
    value: int

    def __init__(self, value=0):
        self.value = value

    def increase(self, value=1):
        self.value += value
        return self.value

    def decrease(self, value=1):
        self.value -= value
        return self.value

    def __iter__(self):
        return self

    def __next__(self):
        value = self.value
        self.increase()
        return value


iterator = iter(Counter())


if __name__ == '__main__':
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
