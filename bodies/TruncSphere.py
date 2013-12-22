import bounds
from py3D import Vector, Ray, Color, Body
from Sphere import Sphere
from Plane import Plane

class TruncSphere(Sphere):
    
    center = Vector()
    radius = 0.0
    R = 0.0
    color = [0.01,0.01,0.01]
    
    def p(self):
        """Returns the name of the type of body this is."""
        return 'TrunkSphere'
    
    def normal(self, point):
        """Returns normal vector of body at given point."""
        s = point - self.center
        if abs(s.dot(s) - self.R) < bounds.small:
            return s.norm()
        else:
            if s.dot(self._orientation) > 0.0:
                sign = 1
            else:
                sign = -1
            return self._orientation.dup().scale(sign)
    
    def set_color(self, c):
        self.color = c
        self._pp.set_color(c)
        self._pn.set_color(c)
        return self
    
    def set_reflectivity(self, r):
        r = max(0.0,min(1.0,r))
        self._r = r
        self._pp.set_reflectivity(r)
        self._pn.set_reflectivity(r)
        return self
    
    def set_orientation(self, v):
        self._orientation = v.norm()
        self._pp.set_normal(v.dup())
        self._pn.set_normal(v.dup().scale(-1.0))
        return self
    
    def set_cosine(self, c):
        self._cosine = c
        cp = self.center.dup().add(self._orientation, c * self.radius)
        cn = self.center.dup().add(self._orientation, -1 * c * self.radius)
        self._pp.set_position(cp)
        self._pn.set_position(cn)
        return self
    
    def __init__(self, center, radius, color = Color()):
        self._pp = Plane(Vector(), Vector(), Color())
        self._pn = Plane(Vector(),Vector(), Color())
        self.set_position(center)
        self.set_radius(radius)
        self.set_color(color)
        self.set_reflectivity(0.2)
        self.set_orientation( Vector() )
        self.set_cosine(1.0)
        
    
    def intersection(self, ray):
        """Returns distance from ray to closest intersection with sphere."""
        
        S = ray.o - self.center
        SD = S.dot( ray.d )
        SS = S.dot(S)
        
        # no hit if sphere is really far away
        if SS > bounds.too_far ** 2:
            return -1.0
        
        radical = SD ** 2 + self.R - SS
        # negative radical implies no solutions
        if radical < 0.0:
            return -1.0
        
        radical **= 0.5
        hits = [-1 * SD - radical,  -1 * SD + radical]
        if hits[0] < bounds.too_close:
            if hits[1] < bounds.too_small:
                return -1.0
        
        pp = self._pp.intersection(ray)
        pn = self._pn.intersection(ray)
        
        if pp < pn:
            hitp = [pp,pn]
        else:
            hitp = [pn,pp]
        
        # if two plane hits before sphere hits, we miss
        if hitp[1] < hits[0]:
            return -1.0
        
        # if two sphere hits before plane hits, we miss
        if hits[1] < hitp[0]:
            return -1.0
        
        # if the second thing hit is forward, that's our distance
        hit = max(hits[0],hitp[0])
        if hit > 0:
            return hit
        # otherwise it's the third hit (if positive)
        hit = min(hits[1],hitp[1])
        if hit > 0:
            return hit
        # otherwise, we didn't hit anything
        else:
            return -1.0
        
        
        
