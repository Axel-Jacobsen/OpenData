""" Lorenz Attractor

Simple differential equations for modelling the atmosphere

dx/dt = a(y-x)      -> a == sigma
dy/dt = x(p-z) - y  -> p == ro
dz/dt = xy-bz       -> b == beta

dx = a(y-x)*dt
x = x + dx

dy = (x(p-z)-y)*dt
y = y + dy

dz = (xy-bz)*dt
z = z + dz
"""
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants (Base Constants)
a = 10
p = 28
b = 8.0/3.0

# Starting Positions of x,y,z (Base Starting Positions)
x = 1
y = 1
z = 1

# Write a function to write n x,y,z coords to a file
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for n in range(3001):

    dt = 0.00001*n
    x += a*(y-x)*dt
    y += (x*(p-z)-y)*dt
    z += (x*y-b*z)*dt
    ax.scatter(x,y,z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
