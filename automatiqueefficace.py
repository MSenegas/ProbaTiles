import matplotlib.pyplot as plt
import numpy as np
f,m = 6, 50
fM = np.zeros((m+1,m+1),dtype=bool)
for i in range(1,f+1):
    fM+=np.eye(m+1,k=-i,dtype=bool)
fCH = np.zeros((m+1,m+1,m+1))
fCH[0] = np.eye(m+1)
for i in range(1,m+1):
    fCH[i]=fCH[i-1]@fM
CH=np.zeros(fCH.shape)
for i in range(m+1):
    CH[i]=fCH[i]/f**i
SCH = np.sum(CH,axis=0)
p = SCH[:,0]
X = np.arange(m+1)
plt.plot(X[1:],p[1:])
plt.ylim(0,0.38)
plt.show()
