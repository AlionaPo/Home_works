import numpy as np
import pandas as pd

# HW: DataKit
# 1. Numpy
# a. Create an array with shape (4, 3) of: 
#       a. all zeros 
#       b. ones 
#       c. numbers from 0 to 11
# b. Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.
# c. Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.

#1.a
all_zeroes = np.zeros((4, 3))
print(all_zeroes)

all_ones = np.ones((4, 3))
print(all_ones)

numbers_list = np.arange(12)
numbers_array = numbers_list.reshape(4, 3)
print(numbers_array)

#1.b
from tabulate import tabulate

range_x = range(1, 100, 1)
list_x = []
for x in range_x:
    func_x = 2 * (x**2) + 5 
    list_x.append(func_x)
print(list_x)

list_to_array = np.array(list_x)
table = tabulate([list_to_array])
                #  , headers='firstrow',tablefmt='grid')
print(table)

# 1c
import math

range_x = range(-10, 10, 1)
list_x = []
for x in range_x:
    func_x = math.exp(-x)
    list_x.append(func_x)
print(list_x)

list_to_array = np.array(list_x)
table = tabulate([list_to_array])
                #  , headers='firstrow',tablefmt='grid')
print(table)


# 2. Pandas
# a. Import the dataset and assign it to df variable.
# b. Select only the Team, Yellow Cards and Red Cards columns.
# c. How many teams participated in the Euro2012?
# d. Filter teams that scored more than 6 goals

# 2a
df = pd.read_csv("https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv")  
 # parameter can be added: (""..., skiprows = 1) if we do notwant 1st row
print(df.head())

# 2b
choosen_columns = ["Team", "Yellow Cards", "Red Cards"]
print(df[choosen_columns])

# 2c
print(df.shape[0]) 
# df.count() will only return the count of non-NA/NaN rows for each column

# 2d
print(df[(df['Goals'] > 6)]['Team'])

# Example
# select the degree cell where age is greater than 28 and grade is 'A'
# df[(df['age'] > 28) & (df['grade'] == 'A')]["degree"]


# 3. DataViz
# a. Choose a dataset, you can use Seaborn [example datasets]. 
# Create a cheat sheet for yourself containing all plot types discussed
# in the lecture. Provide the following info:

# - Plot type
# - Use cases (categorical data, distribution, etc.)
# - Example on the dataset

#In a separate file