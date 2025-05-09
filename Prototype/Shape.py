from abc import ABC, abstractmethod, ABCMeta

class Shape(ABC):
    """Abstract Shape class"""
    __metaclass__ = ABCMeta
    
    def __init__(self):
        super().__init__()
        self.X = 0
        self.Y = 0
        self.color = "black"
    
    def clone_init(self, source):
        super().__init__()
        self.X = source.X
        self.Y = source.Y
        self.color = source.color
        
    @abstractmethod
    def clone(self):
        """Clone the shape"""
        pass
    
class Circle(Shape):
    """Circle class"""
    def __init__(self):
        super().__init__()
        self.radius = 2
    
    @classmethod
    def clone_init(self, source):
        print(type(source))
        new_instance = Circle()      
        new_instance.radius = source.radius
        return new_instance
        
    def clone(self):
        """Clone the circle"""
        return Circle.clone_init(self)
    
class Rectangle(Shape):
    """Rectangle class"""
    
    def __init__(self):
        super().__init__()
        self.width = 4
        self.height = 2
        
    @classmethod
    def clone_init(self, source):
        new_instance = Rectangle()
        new_instance.width = source.width
        new_instance.height = source.height
        return new_instance
        
    def clone(self):
        """Clone the rectangle"""
        return Rectangle.clone_init(self)
    
class Application():
    """Application class"""
    def __init__(self):
        self.shapes = []
        
        circle = Circle()
        circle.X = 10
        circle.Y = 10
        circle.color = "red"
        circle.radius = 5
        
        rectangle = Rectangle()
        rectangle.X = 20
        rectangle.Y = 20
        rectangle.color = "blue"
        rectangle.width = 10
        rectangle.height = 5
        
        self.shapes.append(circle)
        self.shapes.append(rectangle)
        
    def businessLogic(self):
        """Run the application"""
        newShapes = []
        for shape in self.shapes:
            newShape = shape.clone()
            newShapes.append(newShape)
            
        return newShapes
    
if __name__ == "__main__":
    app = Application()
    newShapes = app.businessLogic()
    
    for shape in newShapes:
        print(f"Shape: {shape.__class__.__name__}, X: {shape.X}, Y: {shape.Y}, Color: {shape.color}")