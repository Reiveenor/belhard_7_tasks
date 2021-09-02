"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand: str
    model: str
    issue_year: int

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __str__(self):
        print(f"Модель: {self.model}")
        print(f"Бренд: {self.brand}")
        print(f"Год выпуска: {self.issue_year}")

    def get_info(self):
        return self.brand, self.model, self.issue_year

    def receive_call(self, name):
        self.name = name
        print(f"Звонит {name}")


my_phone = Phone('Iphone', '11', 2020)

my_phone.__str__()
print(my_phone.get_info())
my_phone.receive_call("Vovan")
