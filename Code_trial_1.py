from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

"Code to simulate breaking distance of a car"
"Parameters description: "
# Vehicle basic parameters
# Vehicle mass=1700 kg
# Velocity in km/h
# Road type= wet and dry
# Wet & Dry road
# Car friction coeff
# udynamic
# ustatic
# Parameters to be used in formulas
g = 9.81  # m/s2
# Indicate the velocity of the vehicle in km/h and mass in kg and time in seconds
velocity = 50
m = 1200
t = 10
# Converting from km/hr to m/s
v = velocity * 1000 / 3600
v2 = 0
print("V=", v)
velocity_list = []
velocity_list_2 = []

# Scenario 1 concrete in dry condition, the friction coefficient (u)
ud = 0.5  # dynamic
# Scenario 2 Concrete in wet condition
ud1 = 0.35  # dynamic

# Calculation of breaking forces
fn = m / 4 * 10
print("FN= ", fn, "Newtons")
# Fr= ud*FN *4,
# print("Fr= ", Fr ,"Newtons")
fr = ud * m * g
print("FR=", fr, "N")
a = v / t
print("a=", a, "m/s2")

counter = 10
while counter > 0:
    velocity_list.append(v)
    v = v - a
    counter = counter - 1
counter = 10
v2 = velocity_list[-1]
while counter > 0:
    velocity_list_2.append(v2)
    v2 = v2 + a
    counter = counter - 1

# Braking Distance
bd = []
#bd_final = []

for ind in range(0, len(velocity_list)):
    bd.append(((velocity_list_2[ind]) * (velocity_list_2[ind]) / (2 * g * ud)))
print("Bd=", bd, "m")

plt.plot(bd, velocity_list, "")
plt.xlabel("Distance(m)")
plt.ylabel("Velocity (m/s)")
plt.title("Braking distance Concrete Dry Condition")
plt.show()

