import seaborn as sns
import matplotlib.pyplot as plt

iris = sns.load_dataset('iris')       # Built-in dataset in seaborn

# print(iris)

# sns.scatterplot(x=iris.sepal_length,y=iris.sepal_width)
# plt.show()

# sns.displot(iris['sepal_length'])
# plt.show()

tips = sns.load_dataset('tips')
# print(tips.head())

# print(tips['smoker'].value_counts())
# t = (tips['smoker'].value_counts())
# sns.barplot(t)
# plt.show()

# sns.relplot(x = tips.total_bill,y = tips.tip,data=tips,hue='smoker')  # hue is the differentiator of categories using color
# plt.show()


# print(tips['size'].value_counts())
# sns.relplot(x = tips.total_bill,y = tips.tip,data=tips,style='size')    # style is the differentiator of categories using shapes
# plt.show()


# sns.relplot(x = tips.total_bill,y = tips.tip,data=tips,style='size',hue='time')
# plt.show()

# sns.catplot(x = 'day',y = 'total_bill',data=tips)
# plt.show()

# A combination of scatterplot and histogram is known as jointplot
# sns.jointplot(x = tips.total_bill,y = tips.tip)
# plt.show()

# pairplot is going to plot for all numerical data
sns.pairplot(tips)
plt.show()