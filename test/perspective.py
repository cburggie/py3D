import pytrace
import py3D

filename = 'perspective.png'
ppu = 400
passes = 16

S = py3D.Sphere
C = py3D.Color
V = py3D.Vector

cam = pytrace.Camera(V(0.0,10.0,0.0), V(0.0,0.0,0.0), 2.0, 2.0, V(0.0,0.0,1.0))
cam.set_ppu(ppu)


center = S(V(0.0,0.0,0.0), 1.0, C(0.99,0.99,0.99)).set_reflectivity(0.8)

bodies = []

bodies.append( S(V(0.0,0.0,3.0), 1.0, C(0.01,0.01,0.01)) )
bodies.append( S(V(3.0,0.0,3.0).norm().scale(3.0), 1.0, C(0.99,0.01,0.01)) )
bodies.append( S(V(3.0,0.0,0.0), 1.0, C(0.99,0.99,0.01)) )
bodies.append( S(V(3.0,0.0,-3.0).norm().scale(3.0), 1.0, C(0.01,0.99,0.01)) )
bodies.append( S(V(0.0,0.0,-3.0), 1.0, C(0.01,0.99,0.99)) )
bodies.append( S(V(-3.0,0.0,-3.0).norm().scale(3.0), 1.0, C(0.01,0.01,0.99)) )
bodies.append( S(V(-3.0,0.0,0.0), 1.0, C(0.99,0.01,0.99)) )
bodies.append( S(V(-3.0,0.0,3.0).norm().scale(3.0), 1.0, C(0.99,0.99,0.99)) )
for b in bodies:
    b.set_reflectivity(0.4)
bodies.append(center)

world = pytrace.World(bodies, py3D.Sky(V(0.0,1.0,0.0), C(0.01,0.01,0.3)) )

pytrace.Tracer(world, cam).draw(passes).write(filename)
