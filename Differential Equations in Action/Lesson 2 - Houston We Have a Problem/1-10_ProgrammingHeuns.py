# QUIZ
#
# Implement Heun's Method in the function below, 
# building off of the Forward Euler method as a 
# base. The resulting diagram will show the 
# errors in comparison.

import math
import numpy
import matplotlib.pyplot

total_time = 24. * 3600. # s
g = 9.81 # m / s2
earth_mass = 5.97e24 # kg
gravitational_constant = 6.67e-11 # N m2 / kg2
radius = (gravitational_constant * earth_mass * total_time**2. / 4. / math.pi ** 2.) ** (1. / 3.)
speed = 2.0 * math.pi * radius / total_time

# These are used to keep track of the data we want to plot
h_array = []
euler_error_array = []
heuns_error_array = []

def acceleration(spaceship_position):
    vector_to_earth = - spaceship_position # earth located at origin
    return gravitational_constant * earth_mass / numpy.linalg.norm(vector_to_earth)**3 * vector_to_earth

def heuns_method(num_steps):
    ###Original Euler Method
    h = total_time / num_steps

    x = numpy.zeros([num_steps + 1, 2]) # m
    v = numpy.zeros([num_steps + 1, 2]) # m / s

    x[0, 0] = radius
    v[0, 1] = speed

    for step in range(num_steps):
        x[step + 1] = x[step] + h * v[step]
        v[step + 1] = v[step] + h * acceleration(x[step])

    error = numpy.linalg.norm(x[-1] - x[0])
    h_array.append(h)
    euler_error_array.append(error)
    ###End Original Euler Method

    ###Heun's Method
    #My solution:
    #for step in range(num_steps):
        #x[step + 1] = x[step] + h * (v[step] + (v[step] + h * acceleration(x[step]))) / 2
        #v[step + 1] = v[step] + h * (acceleration(x[step]) + acceleration(x[step+1])) / 2 
    
    #Answer:
    for step in range(num_steps):
        xE = x[step] + h * v[step]
        vE = v[step] + h * acceleration(x[step])
        
        x[step + 1] = x[step] + h * (v[step] + vE) / 2
        v[step + 1] = v[step] + h * (acceleration(x[step]) + acceleration(xE)) / 2   

    error = numpy.linalg.norm(x[-1] - x[0])
    heuns_error_array.append(error)
    
    #Error with my method: [1388391.6985412019, 348624.3520075141, 87253.826379482867, 13965.018184683293, 3491.4121457942001]
    #Error with answer:    [6448715.6790178688, 1531032.8478095494, 367367.50575808738, 57076.353423313216, 14119.245855289646]

    ###End Heun's Method

    return x, v, error

for num_steps in [50, 100, 200, 500, 1000]:
    x, v, error = heuns_method(num_steps) #Check x, v, error



def plot_me():
    matplotlib.pyplot.scatter(h_array, euler_error_array, c = 'g')
    matplotlib.pyplot.scatter(h_array, heuns_error_array, c = 'b')
    matplotlib.pyplot.xlim(xmin = 0.)
    matplotlib.pyplot.ylim(ymin = 0.)
    axes = matplotlib.pyplot.gca()
    axes.set_xlabel('Step size in s')
    axes.set_ylabel('Error in m')
    
plot_me()
matplotlib.pyplot.show()
print heuns_error_array