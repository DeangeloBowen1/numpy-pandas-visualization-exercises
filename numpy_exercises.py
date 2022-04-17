import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

"""------------------------------------------------------------------------
1.) How many negative numbers are there?
------------------------------------------------------------------------"""
neg_num = len(a[a in a < 0])

print(f'{neg_num} negative numbers')

"""------------------------------------------------------------------------
2.) How many positive numbers are there?
------------------------------------------------------------------------"""
pos_num = len(a[a in a > 0])

print('{} positive numbers'.format(pos_num))

"""------------------------------------------------------------------------
3.) How many even positive numbers are there?
------------------------------------------------------------------------"""

pos_even = len(a[(a > 0) & (a % 2 == 0)])

print('{} even positive numbers'.format(pos_even))

"""------------------------------------------------------------------------
4.) if you were to add 3 to each data point, 
how many positive numbers would there be?
------------------------------------------------------------------------"""
# adding 3 to all the elements in the array

array2 = a + 3

new_even = len(array2[array2 > 0])

print('{} even numbers after 3 is added to the array'.format(new_even))

"""------------------------------------------------------------------------
4.) If you squared each number,
 what would the new mean and standard deviation be?
------------------------------------------------------------------------"""
# squaring the elements in the array
array3 = a ** 2

print('{} is the mean of the array after being squared.'.format(array3.mean()))

print('{} is the standard deviation of the array.'.format(array3.std()))
