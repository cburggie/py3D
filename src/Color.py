_close = 0.001

class Color:
    _r = 0.0
    _b = 0.0
    _g = 0.0
    
    def __init__(self, r = 0.001, g = 0.001, b = 0.001):
        self._r = r
        self._g = g
        self._b = b
    
    def __eq__(self, c):
        if abs(self._r - c._r) > _close:
            return False
        if abs(self._g - c._g) > _close:
            return False
        if abs(self._b - c._b) > _close:
            return False
        return True
    
    def __add__(self, color):
        self._r += color._r
        self._g += color._g
        self._b += color._b
        return self
    
    def p(self):
        return [min(int(self._r * 256),255),
                min(int(self._g * 256),255),
                min(int(self._b * 256),255)]
    
    def gamma(self, gamma):
        self._r **= gamma
        self._g **= gamma
        self._b **= gamma
        return self
    
    def dup(self):
        return Color(self._r, self._g, self._b)
    
    def set_rgb(self, r, g, b):
        self._r = r
        self._g = g
        self._b = b
        return self
    
    def copy(self, color):
        self._r = color._r
        self._g = color._g
        self._b = color._b
        return self
    
    def dim(self, factor):
        self._r *= factor
        self._g *= factor
        self._b *= factor
        return self
    
