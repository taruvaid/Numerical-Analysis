#Code to create a harmonograph https://en.wikipedia.org/wiki/Harmonograph
import numpy as np
import matplotlib.pyplot as plt

#Solution 1
f1,f2,f3,f4 = 3,1,2,2.5
A1,A2,A3,A4 = 1,1,1.5,1.5
p1,p2,p3,p4 = 0,0,0,0
d1,d2,d3,d4 = .004, .001, .002, .0015

x=[]
y=[]


for t in range(1,50): 
    x.append((A1*np.sin(t*f1+p1))*np.exp(-d1*t) + A2*np.sin(t*f2+p2)*np.exp(-d2*t))
    y.append((A3*np.sin(t*f3+p3))*np.exp(-d3*t) + A4*np.sin(t*f4+p4)*np.exp(-d4*t))
    


plt.plot(x,y,'k',linewidth=.1)
plt.axis('off')
plt.show()


#Solution 2
f1,f2,f3,f4 = 7,1,2,5
A1,A2,A3,A4 = 1,9,21,6
p1,p2,p3,p4 = 1,2,3,4
d1,d2,d3,d4 = .004, .07, .002, .09

n = 1000000
t = np.logspace(np.log10(10),np.log10(500),n)


x = (A1*np.sin(t*f1+p1))*np.exp(-d1*t) + A2*np.sin(t*f2+p2)*np.exp(-d2*t)
y = (A3*np.sin(t*f3+p3))*np.exp(-d3*t) + A4*np.sin(t*f4+p4)*np.exp(-d4*t)
    

plt.plot(x,y,'k',linewidth=.1)
plt.axis('off')
plt.show()

