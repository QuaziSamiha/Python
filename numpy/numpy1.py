import numpy

# use a list to create a NumPy array:
arr = numpy.array([11, 33, 22, 44])
print(arr)

print(type(arr))

# NumPy is a Python library used for working with arrays.
# It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy stands for Numerical Python.

# Why Use NumPy?
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
# Arrays are very frequently used in data science, where speed and resources are very important.

# Which Language is NumPy written in?
# NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function.
# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method,
# and it will be converted into an ndarray:

# Use a tuple to create a NumPy array:
arr2 = numpy.array((3, 4, 4, 9))
print(arr2)
