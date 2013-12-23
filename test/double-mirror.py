import py3D
import pytrace
from py3D.bodies.TruncSphere import TruncSphere

filename = 'mmb.png'
ppu = 50
passes = 1

V = py3D.Vector

# setup Camera
cam_o = V(0.0,5.0,8.0)
cam_f = V(0.0,1.0,0.0)
cam = pytrace.Camera(cam_o, cam_f, 4.0, 4.0)
cam.set_ppu(ppu)


# setup sky
sun = V(3.0,10.0,3.0).norm()
sky = pytrace.Sky(sun, py3D.Color(0.5,0.5,0.99))

# setup ball
ball_c = V(0.0,1.0,10.0)
ball = py3D.Sphere(ball_c, 1.0, py3D.Color(0.1,0.8,0.2))

# setup mirror
m_c1 = V(-1.0,1.0,0.0)
m_c2 = V( 1.0,1.0,0.0)
m1 = TruncSphere(m_c1, 1.0, py3D.Color(0.5,0.5,0.5))
m_o1 = ((m_c2 - m_c1).norm() - (m_c1 - cam_o).norm()).norm()
m1.set_orientation(m_o1)
m1.set_cosine(0.1)
m1.set_reflectivity(0.7)

# setup second mirror
m2 = TruncSphere(m_c2, 1.0, py3D.Color(0.5,0.5,0.5))
m_o2 = ( (ball_c - m_c2).norm() - (m_c2 - m_c1).norm() ).norm()
m2.set_orientation(m_o2)
m2.set_cosine(0.1)
m2.set_reflectivity(0.7)

# setup plane
plane = py3D.CheckCircle(10.0)

# setup World
world = pytrace.World([m1, m2, ball, plane], sky)
world.set_base_brightness(0.4)

# trace
pytrace.Tracer(world, cam).draw(passes).write(filename)
