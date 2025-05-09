from abc import ABC, abstractmethod, ABCMeta

class Car():
    def __init__(self, name):
        self.name = name
        
class Manual():
    def __init__(self, dictory):
        self.dictory = dictory
        
class Build(ABC):
    __metaclass__ = ABCMeta
    @abstractmethod
    def reset(self):
        """Reset the builder"""
        pass
    
    @abstractmethod
    def set_seats(self):
        """Set the number of seats"""
        pass
    
    @abstractmethod
    def set_engine(self):
        """Set the engine"""
        pass
    
    @abstractmethod
    def set_trip_computer(self):
        """Set the trip computer"""
        pass
    
    @abstractmethod
    def set_gps(self):
        """Set the GPS"""
        pass
    
    
class CarBuilder(Build):
    def __init__(self):
        car = None
        
    def reset(self):
        """Reset the builder"""
        self.car = Car("Car")
        return
    
    def set_seats(self):
        """Set the number of seats"""
        print("Setting seats")
        return
    
    def set_engine(self):
        """Set the engine"""
        print("Setting engine")
        return
    
    def set_trip_computer(self):
        """Set the trip computer"""
        print("Setting trip computer")
        return
    
    def set_gps(self):
        """Set the GPS"""
        print("Setting GPS")
        return
    
    def get_product(self):
        """Get the product"""
        self.reset()
        return self.car
    
class CarManualBuilder(Build):
    def __init__(self):
        manual = None
        
    def reset(self):
        """Reset the builder"""
        self.manual = Manual("Manual")
        return
    
    def set_seats(self):
        """Set the number of seats"""
        print("Setting seats in manual")
        return
    
    def set_engine(self):
        """Set the engine"""
        print("Setting engine in manual")
        return
    
    def set_trip_computer(self):
        """Set the trip computer"""
        print("Setting trip computer in manual")
        return
    
    def set_gps(self):
        """Set the GPS"""
        print("Setting GPS in manual")
        return
    
    def get_product(self):
        """Get the product"""
        self.reset()
        return self.manual
    
class Director():
    def __init__(self, builder):
        self.builder = builder
        
    def build_minimal_viable_product(self):
        """Build the minimal viable product"""
        self.builder.reset()
        self.builder.set_seats()
        return
    
    def build_full_featured_product(self):
        """Build the full featured product"""
        self.builder.reset()
        self.builder.set_seats()
        self.builder.set_engine()
        self.builder.set_trip_computer()
        self.builder.set_gps()
        return
    
def Application():
    """Application class"""
    car_builder = CarBuilder()
    manual_builder = CarManualBuilder()
    
    director = Director(car_builder)
    director.build_minimal_viable_product()
    car = car_builder.get_product()
    
    print(f"Car built: {car.name}")
    
    director = Director(manual_builder)
    director.build_full_featured_product()
    manual = manual_builder.get_product()
    
    print(f"Manual built: {manual.dictory}")
    
    
if __name__ == "__main__":
    Application()