import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
df = pd.DataFrame({'k-cycles':
                  [70, 90, 96, 97, 99, 100, 103, 104, 104, 105,
                    107, 108, 108, 108, 109, 109, 112, 112, 113, 
                    114, 114, 114, 116, 119, 120, 120, 120, 121,
                    121, 123, 124, 124, 124, 124, 124, 128, 128,
                    129, 129, 130, 130, 130, 131, 131, 131, 131,
                    131, 132, 132, 132, 133, 134, 134, 134, 134,
                    134, 136, 136, 137, 138, 138, 138, 139, 139,
                    141, 141, 142, 142, 142, 142, 142, 142, 144,
                    144, 145, 146, 148, 148, 149, 151, 151, 152,
                    155, 156, 157, 157, 157, 157, 158, 159, 162,
                    163, 163, 164, 166, 166, 168, 170, 174, 196, 212]})
#summary df makeing
Vertical_axis1 = []
Vertical_axis2 = []
Horizontal_axis = []
for i in range(0, 240, 10):
    Vertical_axis1.append(0)        #Vertical axis1
    Vertical_axis2.append(0)        #Vertical axis2
    Horizontal_axis.append(i)      #Horizontal axis


for row in df['k-cycles']:
    for i in range(0, 240, 10):
        if row>=i and row<i+10:
            Vertical_axis1[int(i/10)] += 1
for i in range(0, 240, 10):
    if i == 0:
        Vertical_axis2[int(i/10)] = Vertical_axis1[int(i/10)]
    else:
        Vertical_axis2[int(i/10)] = Vertical_axis2[int((i-10)/10)] + Vertical_axis1[int(i/10)]

#transform from list to ndarray
np_Vertical_axis1 = np.array(Vertical_axis1)
np_Vertical_axis2 = np.array(Vertical_axis2)
np_Horizontal_axis = np.array(Horizontal_axis)

fig1 = plt.figure()
ax1 = fig1.add_subplot(2, 2, 1)
ax2 = fig1.add_subplot(2, 2, 2)
ax3 = fig1.add_subplot(2, 2, 3)
ax4 = fig1.add_subplot(2, 2, 4)


ax1.set_title('Number of failures')
ax1.set_xlabel('Repeated cycle number (10^3)')
ax1.set_ylabel('Number of failures')
ax1.bar(np_Horizontal_axis, np_Vertical_axis1, width=10)

ax2.set_title('Total number of failures')
ax2.set_xlabel('Repeated of Number (10^3)')
ax2.set_ylabel('Total number of failures')
ax2.bar(np_Horizontal_axis, np_Vertical_axis2, width=10)

ax3.set_title('Probabilty densify function')
ax3.plot(np_Horizontal_axis, np_Vertical_axis1)

ax4.plot(np.log(np_Horizontal_axis), np.log(np.log(1/(1-np_Vertical_axis1))))

plt.show()