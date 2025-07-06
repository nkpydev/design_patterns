class SingletonMeta(type):
    """
    A meta class that creates a Singleton class. 
    Ensures only one instance exists.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Creating new instance for class: {cls.__name__}")
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"Returning existing instance for {cls.__name__}")
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self, value: str = None):
        self.value = value

    def show(self):
        print(f"Singleton value: {self.value}")

if __name__ == "__main__":
    obj1 = Singleton("first")
    obj1.show()

    obj2 = Singleton("second")
    obj2.show()

    print(f"obj1 is obj2? {obj1 is obj2}")