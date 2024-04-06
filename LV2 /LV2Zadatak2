import numpy as np
import matplotlib.pyplot as plt

#a
data = np.loadtxt(open("mtcars.csv", "rb"), usecols=(1,2,3,4,5,6), delimiter=",", skiprows=1)

#b
plt.scatter(data[:, 3], data[:, 0], color='blue')

#c
sizes = (data[:,5] - min(data[:, 5])) / (max(data[:, 5])-min(data[:, 5]))
#alpha - prozirnost, sizes*100 zbog velicine tockica
plt.scatter(data[:, 3], data[:, 0], s = sizes*100, color='red', alpha=0.5)

#d
mpg_min = np.min(data[:, 0])
mpg_max = np.max(data[:, 0])
mpg_mean = np.mean(data[:, 0])
print("Min mpg: ", mpg_min)
print("Max mpg: ", mpg_max)
print("Mean mpg: ", mpg_mean)

#e
cyl_data = data[data[:, 1] == 6]
mpg_min_cyl = np.min(cyl_data[:, 0])
mpg_max_cyl = np.max(cyl_data[:, 0])
mpg_mean_cyl = np.mean(cyl_data[:, 0])
print("Min mpg for cars with 6 cylinders: ", mpg_min_cyl)
print("Max mpg for cars with 6 cylinders: ", mpg_max_cyl)
print("Mean mpg for cars with 6 cylinders: ", mpg_mean_cyl)


plt.xlabel('hp')
plt.ylabel('mpg')
plt.title('mpg vs hp')
plt.show()
