import math
import numpy as np

def calculate_buoyancy(V: float, density_fluid: float):
    """This calculates buoyancy
    takes v as volume (cubic meters), 
    density_fluid as density (kg/m^3)
    """
    if(density_fluid >0 and V>0):
        return density_fluid*V*9.81
    else:
        raise ValueError("V and density_fluid must be greater than zero.")


def will_it_float(V: float, mass: float):
    """Returns true or false if object with volume V (cubic meters) and 
    mass mass (kg) can float in water
    """
    if(V>0 and mass>0):
        density = mass/V
        if(density>1):
            return False
        return True
    else:
        raise ValueError("volume and mass cannot be zero.")

def calculate_pressure(depth):
    """calculates pressure is gravity on earth times density of water times depth (meters) plus atmospheric pressure;
    assumes acceleration due to gravity is 9.81;
    assumes density of water is 1000 kg/m^3
    if above water surface, returns air pressure
    """
    if(depth <=0):
        return 101325-1.293*9.81*math.abs(depth)
    return 1000*9.81*depth + 101325

def calculate_acceleration(F, m):
    """returns acceleration of object with mass m (kg) with net force of F (Newtons) applied
    """
    if(m<=0 ):
        raise ValueError("cannot have mass of zero or negative mass")
    return F/m

def calculate_angular_acceleration(tau,I):
    """returns angular acceleration of object with moment of inertia I and with torque tau apllied
    """
    if(I<=0):
        raise ValueError("moment of inertia cannot be zero or negative")
    return tau/I

def calculate_torque(F_magnitude,F_direction, r):
    """returns torque given force of magnitude F_magnitude,
    angle 
    """
    return F_magnitude*r*math.sin(F_direction)

def calculate_moment_of_inertia(m,r):
    return m*r**2

def calculate_auv_acceleration(F_magnitude, F_angle, m = 100):
    F_net = F_magnitude*np.array(np.cos(F_angle), np.sin(F_angle))
    return F_net/m

def calculate_auv_angular_acceleration(F_magnitude,F_angle):
    torque = F_magnitude*0.5*math.sin(F_angle)
    return calculate_angular_acceleration(torque,1)

def calculate_auv2_acceleration(T, alpha, theta):
    horizontal_force = np.ndarray()
    vertical_force = np.ndarray()
    horizontal_force.add(T[1]*math.cos(alpha))
    horizontal_force.add(T[2]*math.cos(alpha))
    horizontal_force.add(-T[3]*math.cos(alpha))
    horizontal_force.add(-T[4]*math.cos(alpha))
    vertical_force.add(T[1]*math.sin(alpha))
    vertical_force.add(T[4]*math.sin(alpha))
    vertical_force.add(-T[2]*math.sin(alpha))
    vertical_force.add(-T[3]*math.sin(alpha))
    net_h = np.sum(horizontal_force)
    net_v = np.sum(vertical_force)
    net_force = math.sqrt(net_h**2+net_v**2)
    return np.ndarray(net_force, theta)

def calculate_auv2_angular_acceleration(T, alpha, theta, L, l):
    sum_of_torques = 0
    d = math.sqrt(L**2+l**2)
    for force in T.len():
        sum_of_torques = sum_of_torques + force*d*math.sin(alpha)
    return sum_of_torques/100

def simulate_auv2_motion(T, alpha, L, l):

    acceleration = calculate_acceleration(T,alpha, )
    t = np.ndarray()
    x = np.ndarray()
    y = np.ndarray()
    theta = np.ndarray()
    v = np.ndarray()
    omega = np.ndarray()
    a = np.ndarray()

    return np.ndarray([t, x, y, theta, v, omega, a])

def plot_auv2_motion(t, x, y, theta, v, omega, a):
    