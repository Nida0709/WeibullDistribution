import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
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
Vertical_axis = []
Horizontal_axis = []
for i in range(0, 240, 10):
    Horizontal_axis.append(i)      #Horizontal axis
    Vertical_axis.append(0)        #Vertical axis


for row in df['k-cycles']:
    for i in range(0, 240, 10):
        if row>=i and row<i+10:
            Vertical_axis[int(i/10)] += 1


#transform from list to ndarray
np_Vertical_axis = np.array(Vertical_axis)
np_Horizontal_axis = np.array(Horizontal_axis)
plt.bar(np_Horizontal_axis, np_Vertical_axis, width=10)
plt.show()