import numpy as np

array = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

"""------------------------------------------------------------------------
1.) How many negative numbers are there?
------------------------------------------------------------------------"""
neg_num = array[array < 0].size

print(f'{neg_num} negative numbers')

"""------------------------------------------------------------------------
2.) How many positive numbers are there?
------------------------------------------------------------------------"""
pos_num = array[array > 0].size

print('{} positive numbers'.format(pos_num))

"""------------------------------------------------------------------------
3.) How many even positive numbers are there?
------------------------------------------------------------------------"""

pos_even = len(array[(array > 0) & (array % 2 == 0)])

print('{} even positive numbers'.format(pos_even))

"""------------------------------------------------------------------------
4.) if you were to add 3 to each data point, 
how many positive numbers would there be?
------------------------------------------------------------------------"""
# adding 3 to all the elements in the array

array2 = array + 3

new_even = len(array2[array2 > 0])

print('{} even numbers after 3 is added to the array'.format(new_even))

"""------------------------------------------------------------------------
5.) If you squared each number,
 what would the new mean and standard deviation be?
------------------------------------------------------------------------"""
# squaring the elements in the array
array3 = array ** 2

print('{} is the mean of the array after being squared.'.format(array3.mean()))

print('{} is the standard deviation of the array.'.format(array3.std()))

"""------------------------------------------------------------------------
6.) A common statistical operation on a dataset is centering.
This means to adjust the data such that the mean of the data is 0.
This is done by subtracting the mean from each data point. 
Center the data set.
------------------------------------------------------------------------"""

centered_dataset = (array - array.mean())

print('{} is the centered data set'.format(centered_dataset))

"""------------------------------------------------------------------------
7.) Calculate the z-score for each data point.
------------------------------------------------------------------------"""

z_score = (array - array.mean()) / array.std()
print(f"Z-Score : {z_score}")

"""------------------------------------------------------------------------
More numpy Exercises
------------------------------------------------------------------------"""

# Setup

new_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""------------------------------------------------------------------------
Exercise 1 - Make a variable called
sum_of_a to hold the sum of all the numbers in above list
------------------------------------------------------------------------"""

a = np.array(new_array)

sum_of_a = a.sum()

print(f'Sum of the array is {sum_of_a}')

"""------------------------------------------------------------------------
Exercise 2 - Make a variable named min_of_a to
hold the minimum of all the numbers in the above list
------------------------------------------------------------------------"""

min_of_a = a.min()
print(f"The minimum of all the numbers in the list is {min_of_a} ")

"""------------------------------------------------------------------------
Exercise 3 - Make a variable named max_of_a to hold the max
number of all the numbers in the above list
------------------------------------------------------------------------"""

max_of_a = a.max()
print(f"The max of all numbers in the list is {max_of_a}")

"""------------------------------------------------------------------------
Exercise 4 - Make a variable named mean_of_a to hold the
average of all the numbers in the above list
------------------------------------------------------------------------"""

max_of_a = a.mean()
print(f"Mean of the values in the list are {max_of_a}")

"""------------------------------------------------------------------------
# Exercise 5 - Make a variable named product_of_a to hold the 
product of multiplying all the numbers in the above list together
------------------------------------------------------------------------"""

product_of_a = a.prod()
print(f"The product of the list is {product_of_a}")

"""------------------------------------------------------------------------
# Exercise 6 - Make a variable named squares_of_a. 
It should hold each number in a squared like [1, 4, 9, 16, 25...]
------------------------------------------------------------------------"""

squares_of_a = np.square(a)
print(f"Each number squared: {squares_of_a}")

"""------------------------------------------------------------------------
# Exercise 7 - Make a variable named odds_in_a. 
It should hold only the odd numbers
------------------------------------------------------------------------"""

odds_in_a = a[a in a % 2 == 1]
print(f"Odd numbers: {odds_in_a}")

"""------------------------------------------------------------------------
# Exercise 8 - Make a variable named evens_in_a.
 It should hold only the evens.
------------------------------------------------------------------------"""

evens_in_a = a[a in a % 2 == 0]
print(f"Even numbers: {evens_in_a}")

"""------------------------------------------------------------------------
## What about life in two dimensions? A list of lists is matrix, a table,
a spreadsheet, a chessboard...

## Setup 2: Consider what it would take to find the sum, min, max, average, sum,
product, and list of squares for this list of two lists.
------------------------------------------------------------------------"""

new_array2 = [[3, 4, 5], [6, 7, 8]]

b = new_array2

"""------------------------------------------------------------------------
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
**Hint, you'll first need to make sure that the "b" variable is a numpy array**
------------------------------------------------------------------------"""

"""sum_of_b = 0
for row in b:
    sum_of_b += sum(row)"""

sum_of_b = b.sum()
print(f"Refactored Sum: {sum_of_b}")
"""
# Exercise 2 - refactor the following to use numpy. 
"""

"""min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])"""

min_of_b = min(b)
print(f"Refactored min: {min_of_b}")

"""
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
"""

"""max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])"""

max_of_b = b.max()
print(f"Refactored max: {max_of_b}")
"""
# Exercise 4 - refactor the following using numpy to find the mean of b
"""

"""mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))"""

mean_of_b = b.mean()
print(f"Refactored mean: {mean_of_b}")

"""
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
"""

"""product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number"""

product_of_b = b.prod()
print(f"Refactored Product: {product_of_b}")

"""
# Exercise 6 - refactor the following to use numpy to find the list of squares
"""

"""squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number ** 2)"""

squares_of_b = np.square(b)

"""
# Exercise 7 - refactor using numpy to determine the odds_in_b

"""

odds_in_b = []
for row in b:
    for number in row:
        if number % 2 != 0:
            odds_in_b.append(number)

"""
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
"""

evens_in_b = []
for row in b:
    for number in row:
        if number % 2 == 0:
            evens_in_b.append(number)
