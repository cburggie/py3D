from pytrace import World, Camera, Tracer
from py3D import Color, Vector
from py3D import Plane, CheckPlane, Sphere

win_w = 6.4
win_h = 4.0
ppu = 25
passes = 1
filename = 'room-{0}x{1}.png'.format(int(win_w * ppu), int(win_h * ppu))

ball = Sphere(Vector(0.0,0.0,0.0), 1.0, Color(0.1,0.1,0.1))
ball.set_reflectivity(0.6)

floor = CheckPlane().set_reflectivity(0.0)


wall_color = Color(0.1,0.1,0.1)
n_wall = Plane(Vector(0.0,0.0,-1.0), Vector(0.0,0.0,6.0), wall_color.dup())
s_wall = Plane(Vector(0.0,0.0,1.0), Vector(0.0,0.0,-6.0), wall_color.dup())
w_wall = Plane(Vector(-1.0,0.0,0.0), Vector(6.0,0.0,0.0), wall_color.dup())
e_wall = Plane(Vector(1.0,0.0,0.0), Vector(-6.0,0.0,0.0), wall_color.dup())
ceiling = Plane(Vector(0.0,-1.0,0.0), Vector(0.0,6.0,0.0), wall_color.dup())

bodies = [n_wall, s_wall, w_wall, e_wall, ceiling]
for b in bodies:
    b.set_reflectivity(0.6)
bodies.append(ball)
bodies.append(floor)

world = World(bodies).set_base_brightness(0.9)

cam = Camera(Vector(5.0,2.5,5.0), Vector(-5.0,0.0,-5.0), win_w, win_h)
cam.set_ppu(ppu)

Tracer(world, cam).draw(passes).write(filename)
