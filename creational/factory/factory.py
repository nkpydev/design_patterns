from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woff!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type: str) -> Animal:
        match animal_type.lower(): # for Python 3.10+ versions, else use if-elif-else
            case "dog":
                return Dog()
            case "cat":
                return Cat()
            case _:
                raise ValueError("Unknown animal type!")
            

if __name__ == "__main__":
    animal1 = AnimalFactory.create_animal("Dog")
    print(f"Dog says: {animal1.speak()}")

    animal2 = AnimalFactory.create_animal("Cat")
    print(f"Cat says: {animal2.speak()}")
