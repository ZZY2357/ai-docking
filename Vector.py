
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, v):
        self.x += v.x
        self.y += v.y
        return self
    
    def mult(self, m):
        self.x *= m
        self.y *= m
        return self

    def div(self, m):
        self.x /= m
        self.y /= m
        return self

    def copy(self):
        return Vector(self.x, self.y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def set_length(self, l):
        self.x *= l / self.get_length()
        self.y *= l / self.get_length()
    
    def limit(self, max_speed):
        if self.get_length() > max_speed:
            self.set_length(max_speed)

    def distance_to(self, v):
        return ((self.x - v.x) ** 2 + (self.y - v.y) ** 2) ** 0.5
