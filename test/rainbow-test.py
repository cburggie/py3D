from py3D import Vector as V
from py3D import skys, Sphere, Color, Plane
from pytrace import Camera, Tracer, World


ppu = 50
passes = 1
width = 3.0
height = 3.0
filename = 'Rainbows-{0}x{1}.png'.format(int(width * ppu), int(height * ppu))


cam_o = V(0.0,10.0,10.0)
cam_f = V(0.0,0.0,0.0)
cam = Camera(cam_o, cam_f, 3.0,3.0)
cam.set_ppu(ppu)

sky = skys.Rainbow(V(0.0,1.0,0.0))
sphere = Sphere(V(0.0,0.0,0.0), 1.0, Color(0.001,0.001,0.001))
sphere.set_reflectivity(0.3)
plane = Plane(V(0.0,1.0,0.0), V(0.0,0.0,0.0), Color(0.001,0.001,0.001))
plane.set_reflectivity(0.2)


world = World([sphere, plane], sky)
world.set_base_brightness(0.8)

Tracer(world, cam).draw(passes).write(filename)
