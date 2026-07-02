from app.animals.animal import Animal
from app.animals.cat import Cat
from app.animals.dog import Dog


def feed_animals(animals: list[Animal]) -> int:
    return sum(animal.feed() for animal in animals)

cat = Cat("Cat", False)
lion = Animal("Lion", 25, True)
dog = Dog("Dog")

print(feed_animals([cat, lion, dog]) )