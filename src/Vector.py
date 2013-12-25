from rand import rand
import bounds

class Vector:
    """This handles vector math and manipulation."""
    _x = 0.0
    _y = 0.0
    _z = 0.0
    
    def dot(self, vector):
        """Calculate dot product of this vector and another."""
        return self._x * vector._x + self._y * vector._y + self._z * vector._z
    
    def length(self):
        """Calculates vector length."""
        return self._x * self._x + self._y * self._y + self._z * self._z
    
    def __init__(self, x = 0.0, y = 1.0, z = 0.0):
        """Initialize vector with x,y,z coordinates."""
        self._x = x
        self._y = y
        self._z = z
    
    def __sub__(self, vector):
        """Overload '-' operator for vector differences."""
        return Vector(
                self._x - vector._x,
                self._y - vector._y,
                self._z - vector._z
                )
    
    def __eq__(self, v):
        """Overload '=' operator for vector equality."""
        # treat the vectors as equal if they are very close together
        if (self - v).length() < bounds.very_small:
            return True
        else:
            return False
    
    def dup(self):
        """Create copy of vector."""
        return Vector(self._x, self._y, self._z)
    
    def copy(self, vector):
        self._x = vector._x
        self._y = vector._y
        self._z = vector._z
        return self
    
    def add(self, vector, scalar = 1.0):
        """Translate vector by vector addition"""
        self._x += vector._x * scalar
        self._y += vector._y * scalar
        self._z += vector._z * scalar
        return self
    
    def scale(self, scalar):
        self._x *= scalar
        self._y *= scalar
        self._z *= scalar
        return self
    
    def trans(self, x, y, z):
        """Translate vector by x,y,z offsets."""
        self._x += x
        self._y += y
        self._z += z
        return self
    
    def norm(self):
        """Normalize vector to length 1."""
        l = (self._x * self._x + self._y * self._y + self._z * self._z )
        if l <  bounds.very_small:
            raise 'Normalized a zero vector'
        else:
            l = l ** -0.5
            self._x *= l
            self._y *= l
            self._z *= l
            return self
    
    def cross(self, vector):
        """Returns cross product of this vector by another."""
        return Vector(
                self._y * vector._z - self._z * vector._y,
                self._z * vector._x - self._x * vector._z,
                self._x * vector._y - self._y * vector._x
                )
    
    def delta(self, d):
        """slightly nudges direction of vector."""
        dx,dy,dz = 1,1,1
        while dx ** 2 + dy ** 2  + dz ** 2 > 1:
            dx = rand(2) - 1.0
            dy = rand(2) - 1.0
            dz = rand(2) - 1.0
        dx *= d
        dy *= d
        dz *= d
        self.trans(dx,dy,dz)
        return self
    
    def p(self):
        return "[{0},{1}.{2}]".format(self._x, self._y, self._z)






