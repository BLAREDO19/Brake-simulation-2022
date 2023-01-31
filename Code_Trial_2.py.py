#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Braking distance of a car##
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
g = 9.81  # m/s2
velocity = 50 # km/hr
m = 1200
t = 10
so=5
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

plt.plot(bd, velocity_list, "b")
plt.xlabel("Distance(m)")
plt.ylabel("Velocity (m/s)")
plt.title("Braking distance")
plt.legend(['Dry Condition'])
#plt.show()
    
# Braking Distance
bd_wet = []
#bd_final = []

for ind in range(0, len(velocity_list)):
    bd_wet.append(((velocity_list_2[ind]) * (velocity_list_2[ind]) / (2 * g * ud1)))
print("Bd=", bd_wet, "m")

plt.plot(bd_wet, velocity_list, "r")
plt.xlabel("Distance(m)")
plt.ylabel("Velocity (m/s)")
plt.title("Braking distance Concrete Road")
plt.legend(['Wet condition'])
plt.legend(["Dry Condition", "Wet Condition "], loc ="upper right")
plt.show()

#Scenario of a car in ICE ROAD
udi=0.15 #Friction coefficient (dynamic) dry condition
udi1= 0.08 #Friction coefficient (dynamic) wet condition

# Braking Distance
bd = []
#bd_final = []

for ind in range(0, len(velocity_list)):
    bd.append(((velocity_list_2[ind]) * (velocity_list_2[ind]) / (2 * g * udi)))
print("Bd=", bd, "m")

plt.plot(bd, velocity_list, "b")
plt.xlabel("Distance(m)")
plt.ylabel("Velocity (m/s)")
plt.title("Braking distance")
plt.legend(['Dry Condition'])
#plt.show()
    
# Braking Distance
bd_wet = []
#bd_final = []

for ind in range(0, len(velocity_list)):
    bd_wet.append(((velocity_list_2[ind]) * (velocity_list_2[ind]) / (2 * g * udi1)))
print("Bd=", bd_wet, "m")


plt.plot(bd_wet, velocity_list, "r")
plt.xlabel("Distance(m)")
plt.ylabel("Velocity (m/s)")
plt.title("Braking distance ICE Road")
plt.legend(['Wet condition'])
plt.legend(["Dry Condition", "Wet Condition "], loc ="upper right")
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




