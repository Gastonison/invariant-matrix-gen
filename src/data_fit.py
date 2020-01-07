from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

x = [[x] for x in range(51,83)]
y = [3478761,
3819816,
4187106,
4582116,
5006386,
5461512,
5949147,
6471002,
7028847,
7624512,
8259888,
8936928,
9657648,
10424128,
11238513,
12103014,
13019909,
13991544,
15020334,
16108764,
17259390,
18474840,
19757815,
21111090,
22537515,
24040016,
25621596,
27285336,
29034396,
30872016,
32801516,
34826302]

poly = PolynomialFeatures(degree=3, include_bias=False)
x_new2 = poly.fit_transform(x)
model = LinearRegression()
model.fit(x_new2,y)
print(model.predict(x_new2))