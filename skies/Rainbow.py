from py3D import Vector, Color
from Sky import Sky


class Rainbow(Sky):
    """Class that describes the sky."""
    def __init__(self, light = Vector(0.0,1.0,0.0)):
        Sky.__init__(self, light)

    def get_color(self, ray):
        cosine = ray.d.dot(self.light)
        if cosine < -0.5:
            red = 1.0
            green = 2.0 * (cosine + 1.0)
            blue = 0.0
        elif cosine < 0.0:
            red = 1.0 - 2.0 * (cosine + 0.5)
            green = 1.0
            blue = 0.0
        elif cosine < 0.5:
            red = 0.0
            green = 1.0
            blue = 2.0 * cosine
        else:
            red = 0.0
            green = 1.0 - 2.0 * (cosine - 0.5)
            blue = 1.0
        return Color(red, green, blue)
    
