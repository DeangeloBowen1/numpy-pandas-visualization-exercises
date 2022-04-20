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

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

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

max_of_b = max(b)
print(f"Refactored max: {max_of_b}")
"""
# Exercise 4 - refactor the following using numpy to find the mean of b
"""

"""mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))"""

mean_of_b = np.mean(b)
print(f"Refactored mean: {mean_of_b}")

"""# Exercise 5 - refactor the following to use numpy for calculating the product
# of all numbers multiplied together.

# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number"""

product_of_b = np.product(b)

print(f'Product of b: {product_of_b}')

"""# Exercise 6 - refactor the following to use numpy to find the list of squares

# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)"""

squares_of_b = np.square(b)

print(f'Squares of b: \n{squares_of_b}\n')

"""# Exercise 7 - refactor using numpy to determine the odds_in_b"""

odds_in_b = []
for row in b:
    for number in row:
        if number % 2 != 0:
            odds_in_b.append(number)

print(f'The {len(odds_in_b)} odds in b: \n{odds_in_b}\n')

"""# Exercise 8 - refactor the following to use numpy to filter only the even numbers"""
evens_in_b = []
for row in b:
    for number in row:
        if number % 2 == 0:
            evens_in_b.append(number)

print(f'The {len(evens_in_b)} evens in b: {evens_in_b}')

"""# Exercise 9 - print out the shape of the array b."""

print(f'Shape of b: {np.shape(b)}')

"""# Exercise 10 - transpose the array b."""
b_transposed = np.array(b).T
print(f'Transposed b: {b_transposed}')

"""# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)"""

b_reshape = np.reshape(b, (1, 6))

print(f'Reshaped b to {np.shape(b_reshape)}: {b_reshape}')

"""# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)"""

b_listed = np.reshape(b, (6, 1)).tolist()

print(f'Listed elements of b shaped as {np.shape(b_listed)}: {b_listed}')

"""# Setup 3"""

c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(c)

print(f'Array c: {c}')

"""# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c."""

sum_of_c = c.sum()
min_of_c = c.min()
max_of_c = c.max()
product_of_c = np.product(c)

print(f'Sum of c: {sum_of_c}')
print(f'Min of c: {min_of_c}')
print(f'Max of c: {max_of_c}')
print(f'Product of c: {product_of_c}')

"""# Exercise 2 - Determine the standard deviation of c."""

std_of_c = c.std()

print(f'Standard deviation of c: {std_of_c}')

"""# Exercise 3 - Determine the variance of c."""

var_of_c = c.var()

print(f'Variance of c: {var_of_c}')

"""# Exercise 4 - Print out the shape of the array c"""

print(f'Shape of c: {np.shape(c)}')

"""# Exercise 5 - Transpose c and print out transposed result."""

c_transposed = c.T

print(f'Transposed c: {c_transposed}')

"""# Exercise 6 - Multiply c by the c-Transposed and print the result."""

c_times_c_t = c * c.T

print(f'Multiplied c by c-Transposed: {c_times_c_t}')

"""# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
"""

print(f'Sum of c times c-Transposed: {c_times_c_t.sum()}')
assert c_times_c_t.sum() == 261

"""# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 
131681894400. """

print(f'Product of c times c-Transposed: {np.product(c_times_c_t)}')
assert np.product(c_times_c_t) == 131681894400

"""# Setup 4
"""
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(d)

print(f'Array d: {d}')

"""# Exercise 1 - Find the sine of all the numbers in d
"""
rads = np.pi / 180
d_rads = d * rads
d_sine = np.sin(d_rads)

print(f'Radians of d: {d_rads}')

print(f'Sines of d: {d_sine.round(8)}')

"""# Exercise 2 - Find the cosine of all the numbers in d
"""
d_cosine = np.cos(d_rads)

print(f'Cosines of d: {d_cosine.round(8)}')

"""# Exercise 3 - Find the tangent of all the numbers in d
"""
d_tangent = np.tan(d_rads)
d_tangent = d_tangent.clip(-100, 100)

print(f'Tangents of d (capped at +\\-100): {d_tangent.round(8)}')

"""# print(f'\nData Type of d_tangent: {type(d_tangent[0][0])}')
# print(f'\nData Type of d_sine: {type(d_sine[0][0])}')"""


"""# Exercise 4 - Find all the negative numbers in d
"""
d_negatives = d[d < 0]
print(f'Negatives in d: {d_negatives}')

"""# Exercise 5 - Find all the positive numbers in d"""

d_positives = d[d > 0]
print(f'Positives in d: {d_positives}')

"""# Exercise 6 - Return an array of only the unique numbers in d."""

unique_d = np.unique(d)

"""# Exercise 7 - Determine how many unique numbers there are in d."""

print(f'The {len(unique_d)} unique values in d: {unique_d}')

"""# Exercise 8 - Print out the shape of d."""

print(f'Shape of d: {np.shape(d)}')

"""# Exercise 9 - Transpose and then print out the shape of d."""

print(f'Transposed d: {d.T}')

"""# Exercise 10 - Reshape d into an array of 9 x 2"""

d_reshape = d.reshape(9, 2)

print(f'Reshaped d: {d_reshape}')
