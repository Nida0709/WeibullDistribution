import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math, seaborn

df = pd.DataFrame({'k-cycles':
                  [80, 90, 96, 97, 99, 100, 103, 104, 104, 105,
                    107, 108, 108, 108, 109, 109, 112, 112, 113, 
                    114, 114, 114, 116, 119, 120, 120, 120, 121,
                    121, 123, 124, 124, 124, 124, 124, 128, 128,
                    129, 129, 130, 130, 130, 131, 131, 131, 131,
                    131, 132, 132, 132, 133, 134, 134, 134, 134,
                    134, 136, 136, 137, 138, 138, 138, 139, 139,
                    141, 141, 142, 142, 142, 142, 142, 142, 144,
                    144, 145, 146, 148, 148, 149, 151, 151, 152,
                    155, 156, 157, 157, 157, 157, 158, 159, 162,
                    163, 163, 164, 166, 166, 168, 170, 174, 182]})
#initial setting
timetimetime = 230
rangerange = 10

#custom setting
#timetimetime = 1400
#rangerange = 50







#summary df making
Vertical_axis1 = []
Vertical_axis2 = []
Horizontal_axis1 = []
for i in np.arange(0, timetimetime+rangerange, rangerange):
    Vertical_axis1.append(0)        #Vertical axis1
    Vertical_axis2.append(0)        #Vertical axis2
    Horizontal_axis1.append(i)      #Horizontal axis


for row in df['k-cycles']:
    for i in np.arange(0, timetimetime+rangerange, rangerange):
        if row>=i and row<i+rangerange:
            Vertical_axis1[int(i/rangerange)] += 1
for i in np.arange(0, timetimetime+rangerange, rangerange):
    if i == 0:
        Vertical_axis2[int(i/rangerange)] = Vertical_axis1[int(i/rangerange)]
    else:
        Vertical_axis2[int(i/rangerange)] = Vertical_axis2[int((i-rangerange)/rangerange)] + Vertical_axis1[int(i/rangerange)]

#transform from list to ndarray
np_Vertical_axis1 = np.array(Vertical_axis1)
np_Vertical_axis2 = np.array(Vertical_axis2)
np_Horizontal_axis1 = np.array(Horizontal_axis1)

#fig set
fig1 = plt.figure()
ax1 = fig1.add_subplot(2, 2, 1)
ax2 = fig1.add_subplot(2, 2, 2)
ax3 = fig1.add_subplot(2, 2, 3)
ax4 = fig1.add_subplot(2, 2, 4)


ax1.set_title('Number of failures')
ax1.set_xlabel('Repeated cycle number (10^3)')
ax1.set_ylabel('Number of failures')
ax1.bar(np_Horizontal_axis1, np_Vertical_axis1, width=rangerange)

ax2.set_title('Total number of failures')
ax2.set_xlabel('Repeated of Number (10^3)')
ax2.set_ylabel('Total number of failures')
ax2.bar(np_Horizontal_axis1, np_Vertical_axis2, width=rangerange)

ax3.set_title('Probabilty densify function')
ax3.plot(np_Horizontal_axis1, np_Vertical_axis1)





#Weibull Distribution making
np_Horizontal_axis2 = np.log(np_Horizontal_axis1)
np_Vertical_axis3 = np.log(np.log(1/(1-np_Vertical_axis2/len(df))))     #this is ???lnln(1/(1/F(x)))???

#error removing ex."inf" or "-inf"
df4 = pd.DataFrame(np_Horizontal_axis2, columns=['x'])
df4['y'] = np_Vertical_axis3
rom = []        #for recording
for i in range(len(df4)):       #inf, -inf filter
    if str(df4['y'][i]) == '-inf' or str(df4['y'][i]) == 'inf':
        rom.append(i)
    elif str(df4['x'][i]) == '-inf' or str(df4['x'][i]) == 'inf' or df4['x'][i] == 0:
        rom.append(i)
df4 = df4.drop(index=rom).reset_index()
ax4.set_xlabel('ln(t)')
ax4.set_ylabel('lnln(1/1-F(x))')
ax4.plot(df4['x'], df4['y'])




output_correlationCoefficien = 1000.0
output_gamma = 0.0
output_alpha = 0.0
output_m = 0.0
i=0
for gamma in np.arange(0.01, 10, 0.01):#1000
    for alpha in np.arange(0.01, 10, 0.01): #1000
        for m in np.arange(0.1, 10, 0.1):#100
            #time left function
            whole = 100*1000*1000
            i+=1
            temp = i
            process = int(temp / whole * 10)
            word = ''
            for p in range(process):
                word += '???'
            for p in range(10-process):
                word += '???'




            x = np.array(df4['x'].values)
            y = m * (np.log(x - gamma) - math.log(alpha))
            #???????????????(pandas)
            #s1 = pd.Series(df4['y'].values)
            #s2 = pd.Series(y)
            #res = s1.corr(s2)

            #???????????????(numpy)???????????????????????????
            #y1 = np.array(df4['y'].values)
            #y2 = np.array(y)
            #res = np.corrcoef(y1, y2)[0, 1]

            #???????????????
            y1 = np.array(df4['y'].values)
            y2 = np.array(y)
            delta = np.square(y1-y2)
            res = np.sum(delta)


            print('????????????????????????????????? ' + word + ' alpha='+str(round(alpha, 3))+' gamma='+str(round(gamma, 3))+' m(??????)='+str(round(m, 3)) + ' res='+str(round(res, 3))+' max_res='+str(round(output_correlationCoefficien, 3)))
            if res < output_correlationCoefficien:
                output_correlationCoefficien = res
                output_gamma = gamma
                output_alpha = alpha
                output_m = m






x = np.array(df4['x'].values)
y = output_m * (np.log(x - output_gamma) - math.log(output_alpha))
ax4.plot(x, y)

print('res')
print(output_correlationCoefficien)
print('alpha')
print(output_alpha)
print('gamma')
print(output_gamma)
print('m')
print(output_m)
















plt.show()