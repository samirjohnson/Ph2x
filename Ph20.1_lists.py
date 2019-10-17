import sys
import math
import matplotlib.pyplot as plt
    
def xyzfunctions(fx, fy, Ax, Ay, phi, t):
    X = Ax * math.cos(2*math.pi * fx * t)
    Y = Ay * math.sin(2*math.pi * fy * t + phi)
    Z = X + Y
    return [X, Y, Z]
        
X_list = []
Y_list = []
Z_list = []
t_list = []
fx = float(sys.argv[1])
fy = float(sys.argv[2])
Ax = float(sys.argv[3])
Ay = float(sys.argv[4])
phi = float(sys.argv[5])
dt = float(sys.argv[6])
N = int(sys.argv[7])
for n in range(N):
    X_list.append(xyzfunctions(fx, fy, Ax, Ay, phi, n * dt)[0])
    Y_list.append(xyzfunctions(fx, fy, Ax, Ay, phi, n * dt)[1])
    Z_list.append(xyzfunctions(fx, fy, Ax, Ay, phi, n * dt)[2])
    t_list.append(n*dt)
    print("X: {} Y: {} Z: {}").format(X_list[n], Y_list[n], Z_list[n])
    
plt.plot(t_list, Z_list)
plt.xlabel("t")
plt.ylabel("Z(t)")
plt.show()
    

        
        