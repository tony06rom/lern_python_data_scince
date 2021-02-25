class Dog():
    """Простая модель собаки"""

    def __init__(self, name, age):
        """инициализируем атрибуты имя и возраст"""
        self.name = name
        self.age = age
        print("Собака создана")

    def sit(self):
        """Собака будет садиться по команде"""
        print(self.name.title() + " сесть")

    def jump(self):
        """Собака будет прыгать по команде"""
        print(self.name.title() + " прыжок")

    def gav(self):
        """Собака будет гавкать по команде"""
        print("Гав-гав")

my_dog = Dog('Topic', 4)
my_dog2 = Dog('Nick', 7)
poppy = Dog('Poppy', 2)

print(str(my_dog.age) + " года", "Кличка " + str(my_dog.name))
print(str(my_dog2.age) + " года", "Кличка " + str(my_dog2.name))

my_dog.jump()
my_dog2.sit()
poppy.gav()