import py3D
import pytrace
from py3D.bodies.TruncSphere import TruncSphere

filename = 'TS-test.png'

V = py3D.Vector

body = TruncSphere(V(0.0,1.0,0.0), 1.0, py3D.Color(0.999,0.001,0.001))
body.set_orientation(V(1.0,1.0,1.0))
body.set_cosine(0.1)
cam = pytrace.Camera(V(0.0,1.0,10.0), V(0.0,0.0,-1.0), 4.0, 4.0)
world = pytrace.World([body])
t = pytrace.Tracer(world, cam)
t.draw(1).write(filename)
