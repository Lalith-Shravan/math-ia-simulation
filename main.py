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

orbit_path_1 = [[], [], []] # x-values, y-values, z-values
orbit_path_2 = [[], [], []] # x-values, y-values, z-values

previous_distance = orbital_object_1.point.distanceTo(orbital_object_2.point)

time_interval = 10

for simulation_time in range(0, 6000, time_interval):
    orbital_object_1.move(simulation_time)
    orbital_object_2.move(simulation_time)

    object_1_plot = ax.scatter(orbital_object_1.point.x, orbital_object_1.point.y, orbital_object_1.point.z, label="Object 1", color="blue")
    object_2_plot = ax.scatter(orbital_object_2.point.x, orbital_object_2.point.y, orbital_object_2.point.z, label="Object 2", color="green")


    connection_x = [orbital_object_1.point.x, orbital_object_2.point.x]
    connection_y = [orbital_object_1.point.y, orbital_object_2.point.y]
    connection_z = [orbital_object_1.point.z, orbital_object_2.point.z]
    connection_line = ax.plot(connection_x, connection_y, connection_z, color="red")

    orbit_path_1[0].append(orbital_object_1.point.x)
    orbit_path_1[1].append(orbital_object_1.point.y)
    orbit_path_1[2].append(orbital_object_1.point.z)
    
    orbit_path_2[0].append(orbital_object_2.point.x)
    orbit_path_2[1].append(orbital_object_2.point.y)
    orbit_path_2[2].append(orbital_object_2.point.z)

    orbit_path_1_plot = ax.plot(orbit_path_1[0], orbit_path_1[1], orbit_path_1[2], color="blue")
    orbit_path_2_plot = ax.plot(orbit_path_2[0], orbit_path_2[1], orbit_path_2[2], color="green")

    current_distance = orbital_object_1.point.distanceTo(orbital_object_2.point)
    relative_speed = (current_distance - previous_distance) / time_interval

    if simulation_time % 500 == 0:
        print(f"Time {round(simulation_time)} - Speed {round(relative_speed)}")

    plt.pause(0.001)

    object_1_plot.remove()
    object_2_plot.remove()
    for line in connection_line:
        line.remove()
    
    for line in orbit_path_1_plot:
        line.remove()
    
    for line in orbit_path_2_plot:
        line.remove()

    previous_distance = current_distance