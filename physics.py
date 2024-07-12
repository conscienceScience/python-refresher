import math
import numpy as np

def calculate_buoyancy(V, density_fluid):
    return density_fluid*V*9.81

def will_it_float(V, mass):
    density = mass/V
    if(density>1):
        return False
    return True

def calculate_pressure(depth):
    return 1000*9.81*depth

def calculate_acceleration(F, m):
    return F/m

def calculate_angular_acceleration(tau,I):
    return tau/I

def calculate_torque(F_magnitude,F_direction, r):
    return F_magnitude*r*math.sin(F_direction)

def calculate_moment_of_inertia(m,r):
    return m*r**2

def calculate_auv_acceleration(F_magnitude, F_angle):
    return calculate_acceleration(F_magnitude,100)

def calculate_auv_angular_acceleration(F_magnitude,F_angle):
    torque = F_magnitude*0.5*math.sin(F_angle)
    return calculate_angular_acceleration(torque,1)

def calculate_auv2_angular_acceleration(T, alpha, L, l):
    sum_of_torques = 0
    d = math.sqrt(L**2+l**2)
    for force in T.len():
        sum_of_torques = sum_of_torques + force*d*math.sin(alpha)
    return sum_of_torques/100

def simulate_auv2_motion(T, alpha, L, l):
    t = np.ndarray()
    x = np.ndarray()
    y = np.ndarray()
    theta = np.ndarray()
    v = np.ndarray()
    omega = np.ndarray()
    a = np.ndarray()
    