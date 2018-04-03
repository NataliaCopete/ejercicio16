import numpy as np
import matplotlib.pyplot as plt


datos=np.loadtxt("album.txt")
sobres_comprados=np.zeros(len(datos))

for i in range (len(datos)):
  sobres_comprados[i]=i

laminas=datos[:,0]
repetidas=datos[:,1]

plt.plot(sobres_comprados,laminas,label="laminas")
plt.plot(sobres_comprados,repetidas,label="repetidas")
plt.legend()
plt.savefig("album.png")

