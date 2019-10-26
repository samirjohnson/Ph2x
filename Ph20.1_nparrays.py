import sys
import math
import matplotlib.pyplot as plt
import numpy as np
    
def xyzfunctions(fx, fy, Ax, Ay, phi, t):
    X = Ax * math.cos(2*math.pi * fx * t)
    Y = Ay * math.sin(2*math.pi * fy * t + phi)
    Z = X + Y
    return [X, Y, Z]
        

fx = float(sys.argv[1])
fy = float(sys.argv[2])
Ax = float(sys.argv[3])
Ay = float(sys.argv[4])
phi = float(sys.argv[5])
dt = float(sys.argv[6])
N = int(sys.argv[7])
data_list = np.zeroes((4,1000))
for n in range(N):
    data_list[0][n] = xyzfunctions(fx, fy, Ax, Ay, phi, n * dt)[0]
    data_list[1][n] = xyzfunctions(fx, fy, Ax, Ay, phi, n * dt)[1]
    data_list[2][n] = xyzfunctions(fx, fy, Ax, Ay, phi, n * dt)[2]
    data_list[3][n] = n * dt
    print("X: {} Y: {} Z: {}").format(data_list[0][n], data_list[1][n], data_list[2][n])
    
plt.plot(data_list[3], data_list[2])
plt.xlabel("t")
plt.ylabel("Z(t)")
plt.show()

plt.plot(data_list[0], data_list[1])
plt.xlabel("X(t)")
plt.ylabel("Y(t)")
plt.show()
