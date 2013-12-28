from Vector import Vector

_zero = Vector(0.0,0.0,0.0)

class Ray:
    """This class handles ray manipulation."""
    o = Vector(0.0,0.0,0.0)
    d = Vector(0.0,1.0,0.0)
    
    def __init__(self, o = Vector(0.0,0.0,0.0), d = Vector(0.0,1.0,0.0)):
        self.o = o
        self.d = d.norm()
    
    def __eq__(self, r):
        if self.o == r.o and self.d == r.d:
            return True
        else:
            return False
    
    def dup(self):
        return Ray(self.o.dup(), self.d.dup())
    
    def set_origin(self, origin):
        self.o = origin
        return self
    
    def set_direction(self, direction):
        self.d = direction.norm()
        return self
    
    def follow(self, d):
        # could rewrite as:
        #   return self.o.dup().add(self.d, d)
        return Vector(self.o._x + self.d._x * d,
                self.o._y + self.d._y * d,
                self.o._z + self.d._z * d)
    
    def refract(self, point, normal, sin_t):
        if sin_t > 1.0:
            return self.reflect(point, normal)
        self.o = point
        p = self.d.dup().proj(normal).add(self.d, -1.0).scale(1 - sin_t)
        if p == _zero:
            return self
        else:
            self.d = p.norm()
            return self
    
    def reflect(self, point, normal):
        # o = p, d = d - 2 (n dot d) n
        self.o = point
        s = -2.0 * self.d.dot(normal)
        self.d.add(normal, s).norm()
        return self
    
    
