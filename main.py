from raytracer.ray import Raytracer, GREY
from raytracer.material import Material, Light
from raytracer.geometry import Sphere, Plane, Cube, Cylinder, Pyramid
from raytracer.utils import Color
from raytracer.math import V3

# Colors & Materials
ivory = Material(diffuse=Color(255, 255, 200), albedo=(0.6, 0.3, 0.1, 0), spec=50)
rubber = Material(diffuse=Color(80, 0, 0), albedo=(0.9, 0.1, 0, 0, 0), spec=10)
mirror = Material(diffuse=Color(255, 255, 255), albedo=(0, 10, 0.8, 0), spec=1425)
glass = Material(
    diffuse=Color(150, 180, 200),
    albedo=(0, 0.5, 0.1, 0.8),
    spec=125,
    refractive_index=1.5,
)


# Render
render = Raytracer(400, 400)
render.light = Light(position=V3(0, 0, 0.2), intensity=1.5)
render.background_color = GREY
render.scene = [
    Cube(V3(2, -2, -10), 1, rubber),
    Sphere(V3(-1, -0.4, -5), 0.4, ivory),
    Cylinder(0.3, 1.5, V3(0, 0, -4), rubber),
]

render.finish()
