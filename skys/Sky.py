from py3D import Vector, Ray, Color

class Sky:
    """Class that describes the sky."""
    
    def __init__(self, light = Vector(0.0,1.0,0.0)):
        self.light = light.norm()
    
    def get_color(self, ray):
        pass
    
    def get_light(self):
        return self.light.dup()
