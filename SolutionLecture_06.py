import pandas as pd
import numpy
from matplotlib import pyplot as plt
from numpy import polyfit, polyval
from numpy import arange
df = pd.read_csv("D:/BABIIII/babiiii/Concordia UN/First Course Introduction to Pathon/Lecture_06/Assignment_Lecture06/Data/complete.csv")
reviews = df["number_of_reviews"]
prices = df["price"]
df.query("price > 100 and price < 150")
p = polyfit(reviews, prices, 1)
plt.plot(reviews, prices, '+')
plt.plot(sorted(reviews), polyval(p, sorted(reviews)))
plt.ylim(0, 2000)
plt.show()