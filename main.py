import matplotlib.pyplot as plt
from orbitalobject import OrbitalObject
import numpy as np
from math import pi

fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
ax.set_aspect("equal")

sphere_radius = 6000000

u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
sphere_x = sphere_radius * np.cos(u) * np.sin(v)
sphere_y = sphere_radius * np.sin(u) * np.sin(v)
sphere_z = sphere_radius * np.cos(v)
ax.plot_wireframe(sphere_x, sphere_y, sphere_z, color="gray")

earth_mass = 5.972 * pow(10, 24)
orbital_object_1 = OrbitalObject(earth_mass, 7000000, 0, 0)
orbital_object_2 = OrbitalObject(earth_mass, 7000000, pi / 2, 0)

object_1_plot = ax.scatter(orbital_object_1.point.x, orbital_object_1.point.y, orbital_object_1.point.z, label="Object 1", color="blue")
object_2_plot = ax.scatter(orbital_object_2.point.x, orbital_object_2.point.y, orbital_object_2.point.z, label="Object 2", color="green")

plt.show()