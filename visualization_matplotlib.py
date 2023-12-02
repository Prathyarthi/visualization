import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

# plt.figure(figsize=(6,2))       # For particular size of the figure
# plt.scatter(x,y,c="#223BDC",alpha=0.7,marker="*")    # c is for color and alpha is for intensity adn marker is the symbol
# plt.show()

# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("X vs Y")
# plt.grid()      # To display grid lines
# plt.show()



# x1 = np.linspace(1,10,100)
# y1 = np.sin(x1)
# plt.plot(x1,y1,'--y')         # '--y indicates the plot will be dashed lines with yellow colour'
# plt.show()


# x2 = ['a','b','c','d','e']
# y2 = np.random.rand(5)
# plt.bar(x2,y2)
# # plt.barh(x2,y2)           # To get horizontal bar
# plt.show()


# data = [1,2,3,3,4,4,4,4,5,5,5,5,5,6,6,7,8,8,8,8,8,8,8,8]
# plt.hist(data)                         # This is a histogram where unique numbers are in the x-axis, and the frequency of that numbers are represented in y-axis 
# plt.savefig('histogram.png')          # To save the fig
# plt.show()

# To show 3D plot,
x3 = np.random.rand(50)
y3 = np.random.rand(50)
z3 = np.random.rand(50)

fig = plt.figure()
axis = fig.add_subplot(projection = '3d')
axis.scatter(x3,y3,z3)
plt.show()