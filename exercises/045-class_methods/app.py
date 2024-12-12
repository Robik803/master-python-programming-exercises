import numpy

class MathOperations:
    pi = 3.14159

    @classmethod
    def calculate_circle_area(cls,area):
        return cls.pi*area**2
    
print(MathOperations.calculate_circle_area(5))
