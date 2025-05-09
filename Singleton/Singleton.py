class SingletonMeta(type):
    _instances = {}
     
    def __call__(cls, *args, **kwds):
        if cls not in cls._instances:
            instance = super(SingletonMeta, cls).__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def somebusiness_logic(self):
        """Some business logic"""
        print("Doing some business logic")
        return
    
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()
    
    print(singleton1 is singleton2)  # True
    print(id(singleton1) == id(singleton2))  # True
    singleton1.somebusiness_logic()
    singleton2.somebusiness_logic()