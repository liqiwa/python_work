import matplotlib.pyplot as plt 
x_values = list(range(1,100))
y_values = [x**2 for x  in x_values]
plt.axis([0,200,0,25000])
plt.scatter(x_values,y_values,c = y_values,s= 40,cmap = plt.cm.rainbow,edgecolor = 'none')

plt.show()