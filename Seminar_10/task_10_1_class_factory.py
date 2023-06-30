# Доработаем задачи 5-6. Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики. 

       # Задача 5. Создайте три (или более) отдельных классов животных. 
        # Например рыбы, птицы и т.п. 
        # У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
        # Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
        # Задача 6. Доработайте задачу 5. 
        # Вынесите общие свойства и методы классов в класс Животное. 
        # Остальные классы наследуйте от него. 
        # Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self):
        pass

    def __str__(self):
        return f"{self.name} {self.weight} {self.age}"


class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return "Fly"

    def say(self):
        return self._sound

    def __str__(self):
        return f"{super().__str__()} {self.bird_type}"


class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return "Run"

    def say(self):
        return "Gov"

    def __str__(self):
        return f"{super().__str__()} {self.dog_type}"


class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return "Swim"

    def say(self):
        return ""

    def __str__(self):
        return f"{super().__str__()} {self.fish_type}"


class FactoryOfAnimals:
    # animal = Animal("Животное", 40, 5)
    def __init__(self, animal_kind: str, name: str, weight: int, age: int, animal_type: str):
        match animal_kind:
            case "Bird":
                self.animal = Bird(name, weight, age, animal_type, "Чирик")
            case "Dog":
                self.animal = Dog(name, weight, age, animal_type)
            case "Fish":
                self.animal = Fish(name, weight, age, animal_type)
            case _:
                self.animal = Animal(name, weight, age)

    def __str__(self):
        return f"{super().__str__()} {type(self.animal)}"



if __name__ == '__main__':
    # dog = Dog("Рэкс", 40, 5, "Такса")
    # bird = Bird("Гоша", 1, 3, "Попугай", "Чирик")
    # fish = Fish("Карп", 10, 5, "Речной")

    # print(dog)
    # print(bird)
    # print(fish)

    factory_dog = FactoryOfAnimals("Dog","Рэкс", 40, 5, "Такса")
    factory_bird = FactoryOfAnimals("Bird", "Гоша", 1, 3, "Попугай")
    factory_fish = FactoryOfAnimals("Fish", "Карп", 10, 5, "Речной")

    print(factory_dog)
    print(factory_bird)
    print(factory_fish)